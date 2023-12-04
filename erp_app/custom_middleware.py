
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Product,log_user,User,user_cart,user_cart,otp,ProductStock
from .serializers import ProductSerializer,UserSerializer,Log_userSerializer,User_cartSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token 
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate,update_session_auth_hash
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .serializers import *


from django.http import HttpResponsePermanentRedirect




# custom_middleware.py
from django.urls import is_valid_path

class NoTrailingSlashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path_info = request.path_info

        if not path_info.endswith('/') and not is_valid_path(path_info):
            path_info += '/'
            if request.method == 'GET':
                return HttpResponsePermanentRedirect(path_info)
            else:
                return HttpResponseRedirect(path_info)

        response = self.get_response(request)
        return response
