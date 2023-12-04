from django.contrib import admin
from erp_app.models import Product,log_user,user_cart,otp,ProductStock
from erp_app.models import *




admin.site.register(Product)
admin.site.register(log_user)
admin.site.register(otp)
admin.site.register(user_cart)
admin.site.register(ProductStock)
# admin.site.register(order)
admin.site.register(home)
admin.site.register(home_image)