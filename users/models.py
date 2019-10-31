from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    '''
    This model will create fields for user profile
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg',upload_to='profile_pics')
    number = models.IntegerField(default=0)
    id_number = models.IntegerField(default=0)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
