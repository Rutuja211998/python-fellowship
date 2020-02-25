from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth.models import User
import jwt
from django.core.mail import send_mail
from django_short_url.views import get_surl
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django_short_url.views import ShortURL
from .forms import RegistrationForm, LoginForm, ForgotPasswordForm, ResetForm
from .redis import Redis
redis = Redis()


class RegistrationView(APIView):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        response = {
            "success": False,
            "message": "something went wrong!",
            "data": []
        }

        username = request.data['username']
        email = request.data['email']
        password = request.data['password']

        user_obj = User(username=username, password=password, email=email)

        user_obj.set_password(password)

        user_obj.is_active = False
        user_obj.save()

        token = jwt.encode({'id': user_obj.id}, 'secret', algorithm='HS256').decode('utf-8')
        surl = get_surl(token)

        surl = surl.split('/')

        message = render_to_string('activation.html', {
            'user': user_obj,
            'domain': get_current_site(request).domain,
            'token': surl[2]
        })
        subject = f'activation link from {get_current_site(request).domain}',
        from_email = 'tikhilerutuja321@gmail.com',
        to_email = ['tikhilerutuja321@gmail.com']
        send_mail(subject, message, 'tikhilerutuja321@gmail.com', ['tikhilerutuja321@gmail.com'], fail_silently=False)

        response["message"] = "Successfully registered."
        response["success"] = True

        return JsonResponse(data=response, status=status.HTTP_201_CREATED)


def activate(request, token):

    response = {
        "success": 'Success',
        "message": "Your account is activated!",
        "data": []
    }
    short_obj =ShortURL.objects.get(surl=token)
    token = short_obj.lurl
    payload = jwt.decode(token, 'secret', algorithm='HS256')
    id = payload['id']
    user = User.objects.get(pk=id)

    if user:
        user.is_active = True
        user.save()
        response = {
            "success": 'Success',
            "message": "Your account is activated successfully!"
        }
        return JsonResponse(data=response, status=status.HTTP_200_OK)
    else:
        return JsonResponse(data=response, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        response = {
            "success": 'fail',
            "message": "Unable to login",
            "data": []
        }
        # import pdb
        # pdb.set_trace()
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username=username)
        if user is not None:
            token = jwt.encode({'id': user.id}, 'secret').decode('utf-8')
            response = {
                "success": 'Success',
                "message": "Successfully login!",
                "data": [token]
            }
            redis.set(user.id, token)
            return JsonResponse(data=response, status=status.HTTP_200_OK)
        else:
            return JsonResponse(data=response, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):

    def post(self, request):
        # import pdb
        # pdb.set_trace()
        token = request.META['HTTP_TOKEN']
        print(token)
        payload = jwt.decode(token, 'secret', algorithm='HS256')
        user_id = payload.get('id')
        redis.delete(user_id)

        response = {
            "success": 'Success',
            "message": "User logged out!",
            "data": []
        }

        return JsonResponse(data=response, status=status.HTTP_200_OK)


class ForgotPassword(APIView):

    def get(self, request, *args, **kwargs):
        form = ForgotPasswordForm()
        return render(request, 'reset.html', {'form': form})

    def post(self, request):
        form = ForgotPasswordForm(data=request.data)
        response = {
            "success": 'Fail',
            "message": "User not found!",
            "data": []
        }
        email = request.data['email']
        user_obj = User(email=email)
        token = jwt.encode({'id': user_obj.id}, 'secret', algorithm='HS256').decode('utf-8')
        surl = get_surl(token)
        surl = surl.split('/')

        message = render_to_string('forgot.html', {
            'user': user_obj,
            'domain': get_current_site(request).domain,
            'token': surl[2]
        })
        subject = f'Reset password link from {get_current_site(request).domain}',
        from_email = 'tikhilerutuja321@gmail.com',
        to_email = [user_obj.email]
        send_mail(subject, message, 'tikhilerutuja321@gmail.com', [user_obj.email], fail_silently=False)

        response["message"] = "Successfully reset!"
        response["success"] = True
        return render(request, 'signup.html')


class ResetPassword(APIView):
    def get(self, request, *args, **kwargs):
        form = ResetForm()
        return render(request, 'reset.html', {'form': form})

    def post(self, request, token):
        response = {
            "success": 'Fail',
            "message": "User not found!",
            "data": []
        }
        password = request.data['password']
        short_obj = ShortURL.objects.get(surl=token)
        token = short_obj.lurl
        payload = jwt.decode(token, 'secret', algorithms='HS256')
        user_id = payload.get('id')
        new_password = User(password=password)
        new_password.set_password(password)
        new_password.save()
        response = {
            "success": "Success",
            "message": "User password is reset successfully!",
            "data": []
        }
        return JsonResponse(data=response, status=status.HTTP_200_OK)