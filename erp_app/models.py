from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone  

class Product(models.Model):
    product_id = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=50, default="")
    product_category = models.CharField(max_length=30, default="")
    username = models.CharField(max_length=50, default="") 
    password = models.CharField(max_length=50, default="") 
    # product_image =models.FileField() #  je path te kar vanu
    product_image =models.ImageField(upload_to="erp_app/img", default="") #  je path te kar vanu
    







class log_user(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    # username = models.CharField(max_length=50, default="")
    # password = models.CharField(max_length=50, default="")
    number = models.IntegerField(blank=True,null=True)
    # number= models.IntegerField()
    address = models.CharField(max_length=30, default="")


class otp(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    # demo = models.CharField(max_length=50, default="")
    otp = models.CharField(max_length=10, default="")
    date_time = models.DateTimeField(default=timezone.now)


class user_cart(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    # product_name = models.CharField(max_length=50, default="") 
    # product_price = models.CharField(max_length=50, default="")
    # product_category = models.CharField(max_length=50, default="")
    product=models.ForeignKey(to=Product,on_delete=models.CASCADE)
    


# usr = User()
# usr.username = 'asd'
# usr.set_password('sfsw')
# usr.save
# x = log_user()
# x.user.username
# x.user.email
# x.product_category




class ProductStock(models.Model):
    productId = models.CharField(max_length=50, default="")
    productVariant = models.CharField(max_length=50, default="")
    productPrice = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    # careatTime = models.DateTimeField(default=timezone.now)
    # updateTime=models.DateTimeField(default=timezone.now)


# class order(models.Model):
    
#     orderId = models.CharField(max_length=50, default="")
#     paymentMethod = models.CharField(max_length=50, default="")
#     tranctionId = models.CharField(max_length=50, default="")
#     tranctionNumber = models.IntegerField(default="")
#     gstTax = models.IntegerField(default="") 
#     orderCharge = models.IntegerField(default="") 
#     orderStatas= models.CharField(max_length=50, default="")
#     shipingInfo= models.CharField(max_length=50, default="")
#     billingInfo= models.CharField(max_length=50, default="")
#     paymentStatas=models.CharField(max_length=50, default="")
#     orderRating=models.IntegerField(default="")
    # orderComment=models.CharField(max_length=50, default="")
















class home(models.Model):
    name=models.CharField(max_length=30, default="")
    data=models.CharField(max_length=30, default="")







class home_image(models.Model):
    image_is = models.ForeignKey(home, on_delete=models.CASCADE)
    image = models.FileField(upload_to="erp_app/img")





class myOTP(models.Model):
    phone_number = models.CharField(max_length=15) 
    otps= models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
