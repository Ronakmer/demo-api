from rest_framework import serializers
from .models import Product,log_user,user_cart,home

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


# class ProductSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Product
# 		fields = '__all__'
#     def validate(self,data):
#         print(data,'999999999999999999999')
#         if data['product_id'] == 100:
#             raise serializers.ValidationError('id is 100')
#         return data
#     # product_id = serializers.CharField(max_length=50, default="")
#     # product_name = serializers.CharField(max_length=50, default="")
#     # product_category = serializers.CharField(max_length=30, default="")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
  

class Log_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = log_user
        fields = '__all__'
  

class User_cartSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_cart
        fields = '__all__'



# class ProductSerializer1(serializers.Serializer):
# 	# class Meta:
# 	# 	model = User
# 	# 	fields = ('first_name','last_name', 'username', 'password')
#     product_id = serializers.CharField(max_length=50, default="")
#     product_name = serializers.CharField(max_length=50, default="")
#     product_category = serializers.CharField(max_length=30, default="")






class homeSerializer(serializers.ModelSerializer):
    class Meta:
        model = home
        fields = '__all__'







































































