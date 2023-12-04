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
#######################################################################################################





# Create your views here.

def index(request):
    return HttpResponse("💥💥💥💥 WELCOME TO THE API 💥💥💥💥")

#########################################################################################################

# ek data get................................





def pro_det(request,pk):
    print('++++++')
    pro=Product.objects.get(id=pk)
    # pro=Product.objects.get.all()
    print(pro,'==================')
    serializer =ProductSerializer(pro)
    # print(serializer,'+++++++++++++++++++++++++')
    data= JSONRenderer().render(serializer.data)
    # print(data,'-------')
    return HttpResponse(data,content_type='application/json')
#########################################################################################################



#  all data get

def pro_det1(request):
    print('++++++')
    pro=Product.objects.all()
    # pro=Product.objects.get.all()
    print(pro,'==================')
    serializer =ProductSerializer(pro,many=True)
    # print(serializer,'+++++++++++++++++++++++++')
    data= JSONRenderer().render(serializer.data)
    print(data,'-------')
    return HttpResponse(data,content_type='application/json')





#########################################################################################################

#  simpel add data



# @csrf_exempt 
class ProductViewSet(viewsets.ModelViewSet):
    print('-------------')
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


#########################################################################################################

# ragister user using token

class RegisterUser(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)

            return Response({'status':403 , 'errors': serializer.errors , 'messge': 'not valid'})
        
        serializer.save()
        
        user=User.objects.get(username=serializer.data['username'])
        token_obj , _ =Token.objects.get_or_create(user=user)


        return Response({'status':200 , 'errors': serializer.data ,'token' : str(token_obj) , 'messge': 'valid'})





#########################################################################################################


# headers={ 'user-agent': 'I am a BOT script' }   
# 'Access-Control-Allow-Origin'
# ****** crude ******




@api_view(['GET'])
def studentView(request, pk):
    try :
        student = Product.objects.get(id=pk)
        serialstudent = ProductSerializer(student, many=False)
        return JsonResponse({
            'status':200,
            'students':serialstudent.data,
        })
    except :
        return JsonResponse({'status':400})
# ****************************************************************************************

@api_view(['GET'])
def all_data(request):
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





# @csrf_exempt
# # @api_view(['POST'])
# def studentAdd(request):
#     try:

#         print(request.FILES,'000000000000')
#         # request.POST['product_image'] = request.FILES['product_image']   #=========== 
#         # print(request.POST)
        
#         # serialdata = ProductSerializer(data=request.data)
#         serialdata = Product()
#         serialdata.name=request.POST.get('product_category')
#         serialdata.file=request.FILE['product_image']
#         # serialdata = ProductSerializer(data=request.POST)
#         # serialdata = Product(request.POST,request.FILES)data=request.data
#         print(serialdata,'55555555555555555555555555555') 
#         if serialdata.is_valid():


#             serialdata.save()
        
#         return JsonResponse({
#             'status':200,
#             'student':serialdata.data,
#             'message':'Student added successfully'  
#         })

#     except Exception as e:
#         print(e,'22222222222222222')
#         return JsonResponse({'status':400}) 

import json

@api_view(['POST'])
def studentAdd(request):
    # try:
            
        if request.method == 'POST':  
            product_id=request.data.get('product_id')
            product_name=request.data.get('product_name')
            product_category=request.data.get('product_category')
            # username=request.data.get('username')
            # password=request.data.get('password')
            product_image=request.FILES.getlist('product_image')
            
            # print(product_name,product_image,'00000000000000000000000000000000000000000000000')

            if product_id is not None and product_name is not None and product_category is not None and product_image is not None:
                # print('11111111111111111111111111111111111111111111111111111111111111')
                # user=Product.objects.filter(userName=userName)   #===============================
                # if not user.exists():
                for i in product_image:
                    # Product.objects.create(product_image=i)
                    # print(i,'000000000000000')
                    #  logUser.product_image=i
                    # logUser.product_image=json.dumps(i)
                    # a.append(i)

                    # logUser.product_image=i
                    # print('2222222222222222222222')
                    # logUser.save()
                    
                    a=Product()
                    print('000000000000')
                    a.product_image=i
                    print('1111111111111111111')
                    a.save()
                    print(a,'aaaaaaaaaaaaaaaaaa')
             

                logUser=Product()
                print('333333333333333333333333333')
                logUser.product_id=product_id
                logUser.product_name=product_name
                logUser.product_category=product_category
                logUser.product_image=a
                print(logUser.product_image,'aaaaaaaaaaaaaaaa')
                print('44444444444444444444444444444')
                logUser.save()
                print('5555555555555555555555555')
                # logUser.username=username
                # logUser.password=password
                # logUser.save()
                # for i in product_image:
                #     logUser.product_image=i
           
                    # print(logUser.product_image,'3333333333333333333333')
                
                return JsonResponse({'status':200,'message':'user add successfully 👻👻👻'})
                # else:
                #     return JsonResponse({'status':404,'message':'user name exists'})
            else:
                return JsonResponse({'status':400,'message':'plz provide valid data'})
            
        else:
            return Response({'status':400})


    # except:
    #     return Response({'status':400})




# @api_view(['POST'])
# def studentUpdate(request, pk):
#     try :
#         student = Product.objects.get(id=pk)
#         serialstudent = ProductSerializer(instance=student, data=request.data)

#         if serialstudent.is_valid():
#             serialstudent.save()
            
#         return Response({
#             'status':200,
#             'student':serialstudent.data,
#             'message':'Updated successfully'
#         })

#     except :
#         return Response({'status':400})


@csrf_exempt 
@api_view(['POST'])
def studentUpdate(request):
    try :
        # print('*********',request.POST.get('product_id'))
        pk=request.data.get('pk')
        pId=request.data.get('product_id')
        pName=request.data.get('product_name')
        pCategory=request.data.get('product_category')
        product_image=request.FILES['product_image']

        print(pk,pId,'0000000000000000000000000')

        if pk == None or pId == None or pName == None or pCategory == None or product_image == None:

            return JsonResponse({'status':404 , 'message':'provide all data'})
        else:
            product=Product.objects.filter(pk=pk)
            if product.exists():
                product=product.first()
                productSerial=ProductSerializer(instance=product, data=request.data)
                print(productSerial,'00000000000000000000000000')
                # product.product_id=pId
                # product.product_name=pName
                # product.product_category=pCategory
                if productSerial.is_valid():
                    productSerial.save()
                        
                    return JsonResponse({
                        'status':200,
                        'student':productSerial.data,
                        'message':'Updated successfully'
                    })
                else:
                    return JsonResponse({'status':404 , 'message':'valid data enter ' })
            else:
                return JsonResponse({'status':404 , 'message':'Product not found ' })

    except :
        return JsonResponse({'status':400})
        
 




# @api_view(['DELETE'])
# def studentdelete(request, pk):
#     try:

#         student = Product.objects.get(id=pk)      
#         student.delete()
        
#         students = Product.objects.all()
#         serialstudents = ProductSerializer(students, many=True)
        
#         return Response({
#             'status':200,
#             'student':serialstudents.data,
#             'message':'Student Deleted successfully'
#         })

#     except:
#         return Response({'status':400})



@csrf_exempt 
@api_view(['DELETE'])
def studentdelete(request):
    try:
        pk=request.data.get('pk')
        # print('55555555555555')
        if pk == None :
            return JsonResponse({'status':404 , 'message':'provide pk'})
        else:
            product = Product.objects.filter(pk=pk)
            if product.exists():
                product.first().delete()
                return JsonResponse({'status':200, 'message':'product Deleted successfully'  })
            else:
                return JsonResponse({'status':404 , 'message':'product not found'})
    except:
        return JsonResponse({'status':400})

#########################################################################################################

# *****************************************   Login   *********************************************


@csrf_exempt  
# @api_view(['POST']) 
def getUser(request):  
    return JsonResponse({'status':200, 'user':request.user.username})



@csrf_exempt 
@api_view(['POST']) 
def loginuser(request,format=None):  
    # if request.method == 'POST':
        print(request.data)
    # return JsonResponse (request.data)
        username = request.data.get('username')
        password = request.data.get('password')

        # username = request.data['username']
        # password = request.data['password']

        # username = request.POST['username']
        # password = request.POST['password']
        print(request)
        print(request.POST,'00000000000000000000000')
        print(username,password,'7777777777777777')

        if username is not None and password is not None:
            # if user is not None
            if len(password)>7:
                user = authenticate(username =username, password=password)
                if user is not None:
                    login(request, user)
                    # messages.success(request, 'Successfully Logged In') 
                    return JsonResponse({'status':200, 'message':'login successfully','user':request.user.username,'type':'True'})
                else:
                    return JsonResponse({'status':404, 'message':'user or password not match','type':'False'})
            else:
                return JsonResponse({'status':404, 'message':'Enter password 8 number','type':'False'})
        else:
            return JsonResponse({'status':404, 'message':'Enter id and password','type':'False'})
    # else:
    #     return JsonResponse({'status':404, 'message':'page not found'  })


@csrf_exempt
def logoutuser(request):
# if request.method == 'POST':
    # pageView(request)
    logout(request)
    # messages.success(request, 'Successfully Logged Out')
    return JsonResponse({'status':200, 'message':'logout successfully','user':request.user.username,'type':'True' })
    # try:
    #     return redirect(request.GET.get('return'))
    # except:
    #     return redirect('/')
# else:
    # pageView(request, True)
    # return render(request, '404.html') 
    # return JsonResponse({'status':404, 'message':'page not found'  }) 








############################################################################################################

# *************************   login   //  username and email  *************************************


# @csrf_exempt 
# @api_view(['POST']) 
# def loginuser(request):  
#     # if request.method == 'POST':
#         print(request.data)
#     # return JsonResponse (request.data)
#         username = request.data.get('username')
#         password = request.data.get('password')

#         # username = request.data['username']
#         # password = request.data['password']

#         # username = request.POST['username']
#         # password = request.POST['password']
#         print(request)
#         print(request.POST,'00000000000000000000000')
#         print(username,password,'7777777777777777')

#         if username is not None and password is not None:
#             # if user is not None

#             if len(password)>7:
#                 try:
#                     user = authenticate(username =User.objects.get(email=username),password=password)
#                     print(user,'00000000000')
#                     if user is not None:
#                         login(request, user)
#                         # messages.success(request, 'Successfully Logged In') 
#                         return JsonResponse({'status':200, 'message':'login successfully','user':request.user.username,'type':'True'})
#                     else:
#                         return JsonResponse({'status':404, 'message':'user or password not match','type':'False'})

#                 except:
#                     user = authenticate(username =username, password=password)
#                     if user is not None:
#                         login(request, user)
#                         # messages.success(request, 'Successfully Logged In') 
#                         return JsonResponse({'status':200, 'message':'login successfully','user':request.user.username,'type':'True'})
#                     else:
#                         return JsonResponse({'status':404, 'message':'user or password not match','type':'False'})
#             else:
#                 return JsonResponse({'status':404, 'message':'Enter password 8 number','type':'False'})
#         else:
#             return JsonResponse({'status':404, 'message':'Enter id and password','type':'False'})
#     # else:
#     #     return JsonResponse({'status':404, 'message':'page not found'  })







############################################################################################################

# *************************   ResetPassword  //  forgetPassword  *************************************


def createotp():
    # print('566560')
    d='01234546789'
    otp=''
    for i in range(6): 
        otp+=d[math.floor(random.random()*10)]
    return otp

@csrf_exempt
def sendotp(request):
    if request.user.is_authenticated:
        mail=request.user.email    #find mail for db
        # print(mail,'====================')
        if mail!=None:
            send_otp=createotp()
            db_otp=otp()
            db_otp.user=request.user
            db_otp.otp=send_otp
            # ****.db nu otp =***
            db_otp.save()
            a=settings.EMAIL_HOST_USER
            send_mail('OTP for Erp',f'Here is your OTP:{send_otp} for reset password',settings.EMAIL_HOST_USER,[mail])
            # send_mail('OTP for Erp',f'Here is your OTP:{send_otp} for reset password',settings.EMAIL_HOST_USER,[a])
            # ('subject','massege','sender mail','list of resever') 
            return JsonResponse({'status':200, 'message':'otp send'})
        else:
            return JsonResponse({'status':200, 'message':'mail is not set'})
    else:
        return JsonResponse({'status':200, 'message':'plz login '})


@csrf_exempt 
# @api_view(['POST'])
def forgetPassword(request):
    if request.method=="POST":
        
        username=request.POST.get('username')
        user_otp=request.POST.get('otp')
        password=request.POST.get('password')

        if user_otp is not None and password is not None and username is not None:
            user=User.objects.filter(username=username)   #find user
            print(user,'00000000000000000000000000000000')
            if user.exists():
                db_otp=otp.objects.filter(user=user.first())
                if db_otp.exists():
                    db_otp=db_otp.first()
                    if db_otp.otp==user_otp:
                        db_otp.delete()
                        user=user.first() 
                        
                        user.set_password(password)
                        user.save()
                        return JsonResponse({'status':200, 'message':'ResetPassword successfully'})
                    else:
                        return JsonResponse({'status':200, 'message':'otp not matched.....!!!'})
                else:
                    return JsonResponse({'status':200, 'message':'plz otp send.....!!!'})
            else:
                return JsonResponse({'status':200, 'message':'user not found.....!!!'})
        else:
            return JsonResponse({'status':200, 'message':'Enter data.....!!!'})
    else:
        return JsonResponse({'status':404})    
   

# @csrf_exempt 
# # @api_view(['POST'])
# def verify_otp(request):
 
#     if request.method=="POST":
#         username=request.POST.get('username')

        
#         user1=request.user.username
#         user=User.username.request('username')
#         if user is not None:
#             # pass
#             pk=request.data.get('pk')
#             usname=request.data.get('username')
#             return JsonResponse({'status':200,'message':'done data.....!!!'})
#         else:
#             return JsonResponse({'status':404})    
#     else:
#         return JsonResponse({'status':404})


@csrf_exempt 
# @api_view(['POST'])
def ResetPassword(request):
    
    # otp_fuc=sendotp()

    if request.method=="POST":
        uname=request.POST.get('username')
        new_password=request.POST.get('new_password')
        old_password=request.POST.get('old_password')
        if uname is not None and new_password is not None and old_password is not None:
            user=authenticate(username =uname, password=old_password)
            if user is not None:
                user.set_password(new_password)
                user.save()
                # login(request,user) # login rakhu hoy to 👍👍👍👍👍👍
                return JsonResponse({'status':200, 'message':'ResetPassword successfully 👻👻👻'})
            else:
                return JsonResponse({'status':200, 'message':'Password not matched.....!!!'})
        else:
            return JsonResponse({'status':200, 'message':'Enter data.....!!!'})
    else:
        return JsonResponse({'status':404})



############################################################################################################

# **************************************  RAJISTECION **************************************

#######################add data user and log_user

@csrf_exempt 
@api_view(['POST'])
def registeruser(request):
    # try:
    # if request.method=="POST":  
            username=request.data['username']
            password=request.data['password']
            mail=request.data['email']
            address=request.data['address']
            phone=request.data['number']        
            if username is not None and phone is not None and password is not None and mail is not None and address is not None:
                user=User.objects.filter(username=username)
                if not user.exists():
                    user=User()
                    user.username=username
                    user.email=mail
                    user.set_password(password) 
                    user.save()
                    logUser=log_user()
                    logUser.user=user # connect tabel 
                    logUser.address=address
                    logUser.number=phone
                    logUser.save()
                    
                    return JsonResponse({'status':200,'message':'user add successfully 👻👻👻'})
                else:
                    return JsonResponse({'status':404,'message':'user name exists'})
            else:
                return JsonResponse({'status':400,'message':'plz provide valid data'})
    # else:
    #     return JsonResponse({'status':404})        


@api_view(['GET'])
def demo_view_data(request):
    try:
        students = log_user.objects.all()
        serialstudents = Log_userSerializer(students,many=True)
        
        #  mail=request.user.email
        response = JsonResponse(
        {'students':serialstudents.data,
        'status':200,
        'message':'all data successfully'
        }
        
        )
        response["Access-Control-Allow-Origin"] = "*"
        
        return response
    except:
        return Response({'status':400})




############################################################################################################

# **************************************  CART **************************************

@csrf_exempt 
# @api_view(['POST'])
def cart_add(request):
    if request.method=="POST":  
        if request.user.is_authenticated:
            pk=request.POST.get('pk')
            if pk is not None:
                product=Product.objects.filter(pk=pk)
                if product.exists():
                    db_cart=user_cart()
                    db_cart.user=request.user
                    db_cart.product=product.first()
                    db_cart.save()

                    return JsonResponse({'status':200,'message':'data add successfully 👻👻👻'})
                else:
                    return JsonResponse({'status':404,'message':'product is not found'})
                
            else:
                return JsonResponse({'status':400,'message':'plz provide product id'})
        else:
            return JsonResponse({'status':400,'message':'login plz'})
    else:
        return JsonResponse({'status':404})        

    

####################################################################################################################

# **************************************  send otp using email **************************************


# @csrf_exempt
# # @api_view(['POST']) 
# def sendotps(request):
#     # if request.method == 'POST':
#         # if request.user.is_authenticated:
        
#         # email = request.data['email']
#         email = request.POST.get('email')
#         username=request.POST.get('username')

#         # mail=request.user.email    #find mail for db
#         # print(users,'====================')
#         print(email,'====================')
#         # users='ronak'
#         if email!=None:
#             send_otp=createotp()
#             db_otp=otp()
#             # db_otp.demo=username
#             db_otp.otp=send_otp
#             # ****.db nu otp =***
#             db_otp.save()
#             send_mail('OTP for Erp',f'Here is your OTP:{send_otp} for reset password',settings.EMAIL_HOST_USER,[email])
#             # ('subject','massege','sender mail','list of resever') 
#             return JsonResponse({'status':200, 'message':'otp send'})
#         else:
#             return JsonResponse({'status':404, 'message':'mail is not set'})
#     # else:
#     #     return JsonResponse({'status':200, 'message':'plz login '})
    

####################################################################################################################




# find user using phone number and etc....
# [[
# D = Details.objects.filter(phoneno=35567)
# X=D.first()
# X.user
# ]]


####################################################################################################################
@api_view(['POST'])
def homeadd(request):
	try:
			
		serialdata = homeSerializer(data=request.data)
		if serialdata.is_valid():
			serialdata.save()
                        
            

		return Response({
			'status':200,
			'homedata':serialdata.data,
			'message':'home added successfully'
		})

	except:
		return Response({'status':400})


@api_view(['GET'])
def homeshow(request):
    homedata = home.objects.all()
    serialhome = homeSerializer(homedata, many=True)
    return Response({
        'status':200,
        'homedata':serialhome.data,
		'message':'show all home data'
    })



@api_view(['DELETE'])
def homedelete(request, pk):
    try:

        homedata = home.objects.get(id=pk)
        homedata.delete()
        
        homedatas = home.objects.all()
        serialhome = homeSerializer(homedatas, many=True)
        
        return Response({
            'status':200,
            'homedata':serialhome.data,
            'message':'home Deleted successfully'
        })

    except:
        return Response({'status':400})



@api_view(['POST'])
def homeupdate(request, pk):
    try :
        homedata = home.objects.get(id=pk)
        serialhome = homeSerializer(instance=homedata, data=request.data)

        if serialhome.is_valid():
            serialhome.save()
            
        return Response({
            'status':200,
            'homedata':serialhome.data,
            'message':'driver successfully'
        })

    except :
        return Response({'status':400})
    


####################################################################################################################



import random
from django.http import JsonResponse
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

def send_otp(request, phone_number):
    # Validate the phone number using the phonenumbers library
    phone_number = phone_number.strip()
    print(phone_number,'00000000')
    validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+1234567890'")
    try:
        validator(phone_number)
    except ValidationError:
        return JsonResponse({'message': 'Invalid phone number'})

    # Generate a random 6-digit OTP
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

    # Store the OTP in the database
    myOTP.objects.create(phone_number=phone_number, otp=otp)

    # Replace this with code to send the OTP via SMS
    print(f"Sending OTP {otp} to {phone_number}")

    return JsonResponse({'message': 'OTP sent successfully'})


def verify_otp(request, phone_number, otp):
    otp_obj = myOTP.objects.filter(phone_number=phone_number, otp=otp).order_by('-created_at').first()
    if otp_obj:
        # You can add an expiry time check here
        # If OTP is valid, you can mark it as used or delete it
        otp_obj.delete()
        return JsonResponse({'message': 'OTP verified successfully'})
    else:
        return JsonResponse({'message': 'Invalid OTP'})




def demo1(request):
    return render(request,'demo.html')