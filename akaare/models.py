from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User_ID(models.Model):
    """ this is django in build user model which contains 
       1- username, email,password,first name ,last name
       2- on_delete=models.CASCADE if user is deleated all the information 
        related to him will be deleated automatically"""
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    """this phone validator will only work for indian numbers
        if you want to handel multiple international numbers import 
        django's phonenumber model"""
    #phone_regex=RegexValidator(
    #   regex=r'^\+?91?\d{10}$'
    #)
    #phone_number=models.CharField(validators=[phone_regex],max_length=10)
    phone_number=models.PhoneNumberField(unique=True,region='IN')

    age=models.IntegerField(max_length=150)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    mothername=models.models.CharField(_(""), max_length=50)

    def __str__(self):
        return self.user.username
    
