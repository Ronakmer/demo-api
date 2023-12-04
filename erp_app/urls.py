from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('product',views.ProductViewSet)

from .views import *

from django.conf import settings
from django.conf.urls.static import static

from erp_app.demos import *

urlpatterns = [
    path('', views.index, name="erp_app"),
    ###################################################################################################
    path('view_api/<int:pk>', views.pro_det, name="pro_det"),  # ek data
    path('view_api/', views.pro_det1, name="pro_det1"),    # malti data
    ###################################################################################################
    path('ab_api/', include(router.urls),name='ab_api'),    # add data
    ###################################################################################################
    # RegisterUser
    path('RegisterUser/', RegisterUser.as_view()),

  ###################################################################################################


        #****************************** FINAL ******************************#
   
    path('all_data/', views.all_data, name="all_data"),  # all data
    path('add_data/', views.studentAdd, name="studentadd"),  # add data

    path('update_data/', views.studentUpdate, name="studentupdate"), # updata data
    path('delete_data/', views.studentdelete, name="studentdelete"), # delete data

    # path('update-student/<str:pk>/', views.studentUpdate, name="studentupdate"),

    path('student-view/<str:pk>/', views.studentView, name="studentview"),

    path('login/', views.loginuser, name="loginuser"),
    path('logins/', views.getUser, name="getuser"),

    path('logout/', views.logoutuser, name="logoutuser"),

    path('resetpassword/', views.ResetPassword, name="ResetPassword"),

    path('sendotp/', views.sendotp, name="sendotp"),
    path('createotp/', views.createotp, name="createotp"),

    path('forgetpassword/', views.forgetPassword, name="forgetPassword"),

    path('registeruser/', views.registeruser, name="registeruser"),
    path('cart_add/', views.cart_add, name="cart_add"),

    # path('verify_otp/', views.verify_otp, name="verify_otp"),
###################################################################################################
  
    path('demo_view_data/', views.demo_view_data, name="demo_view_data"),
    # path('sendotps/', views.sendotps, name="sendotps"),
    # path('fo/', views.fo, name="fo"),





    

    path('demos/', demos, name="demos"),
    # path('fo/', demos, name="demos"),





    path('homeadd/', homeadd, name="homeadd"),
    path('homeshow/', homeshow, name="homeshow"),
    path('homeupdate/<str:pk>/', homeupdate, name="homeupdate"),
    path('homedelete/<str:pk>/', homedelete, name="homedelete"),




    path('demo1/', demo1, name="demo1"),
    path('send-otp/<str:phone_number>', send_otp, name='send_otp'),
    path('verify-otp/<str:phone_number>/<str:otp>/', verify_otp, name='verify_otp'),



]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



