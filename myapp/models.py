from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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
    
     # Override the save method of the model
    def save(self):
        super().save()

        img = Image.open(self.image.path) # Open image
        
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) #
    
    
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








