from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    '''
    Model for user profile
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    
class Project(models.Model):
    '''
    Model for uploaded projects
    '''
    title = models.CharField(max_length=40)
    description = models.TextField()
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='site_photos/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.title} Project'








