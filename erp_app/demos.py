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


########################################################################################################
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
import sys,os
from django.contrib.auth.forms import PasswordChangeForm
import math,random

# from rest_framework import serializers,viewsets
# from .serializers import PersonSerializer,SpeciesSerializer,RoSerializer,MRSerializer
# from rest_framework import status






@api_view(['GET'])
def demos(request):
    print('🔥🔥------ALl DATA------🔥🔥')
    
    try:
        # if request.user.is_authenticated:

            students = Product.objects.all()
            serialstudents = ProductSerializer(students, many=True)
            # response["Access-Control-Allow-Origin"] = "*"
            # return Response.has_header('Access-Control-Allow-Origin', '*')
            
            # return Response({
            #     # 'status':200,
            #     'students':serialstudents.data,
            #     # 'Access-Control-Allow-Origin':'*'
            #     'headers': { 'Access-Control-Allow-Origin': '*'}
            #     # 'Access-Control-Allow-Origin': '*',
            #     # 
            # })

            response = JsonResponse(
            {'students':serialstudents.data,
            'status':200,
            'message':'all data successfully',
            'type':'True'
            }
            
            )
            response["Access-Control-Allow-Origin"] = "*"
            
            return response 
        # else:
        #     return JsonResponse({'status':404 , 'message':'plz login ','type':'False' })

    except:
        return JsonResponse({'status':400})


