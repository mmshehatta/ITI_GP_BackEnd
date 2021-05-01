from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254, unique=True)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media' , null=True , blank=True)
    is_admin = models.BooleanField(default=False) 

    # phone = PhoneField(blank=True, help_text='Contact phone number')
    # image = models.ImageField(upload_to='users/UserProfile/images' , null=True , blank=True)


    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



    # def __str__(self):
    #     return '%s' % self.user

    # def create_profile(sender, **kwargs):
    #     if kwargs['created']:
    #         user_profile = UserProfile.objects.create(user=kwargs['instance'])
    # post_save.connect(create_profile, sender=User)

