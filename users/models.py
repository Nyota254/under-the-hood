from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    '''
    This model will create fields for user profile
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg',upload_to='profile_pics')
    number = models.IntegerField()
    id_number = models.IntegerField()
    bio = models.TextField()
