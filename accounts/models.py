from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique= True)
    bio = models.CharField(max_length=500,blank=True)
    Is_author = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile/', blank= True,null=True )

    REQUIRED_FIELDS =['email']

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    dob = models.DateField(null=True,blank=True)
    image = models.ImageField(upload_to='profile/', blank= True,null=True )

    def __str__(self):
        return self.user.username