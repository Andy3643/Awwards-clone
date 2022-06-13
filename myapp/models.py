from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from PIL import Image

# Create your models here.
class Profile(models.Model):
    '''
    Model for user profile
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(blank=True)

    
    def __str__(self):
        return f'{self.user.username}Profile'
    @receiver(post_save,sender=User) 
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User) 
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()
    # def __str__(self):
    #     return f'{self.user.username} Profile'
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    

    #     img = Image.open(self.image.path) # Open image
        
    #     # resize image
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size) # Resize image
    #         img.save(self.image.path) #
    
    
class Project(models.Model):
    '''
    Model for uploaded projects
    '''
    title = models.CharField(max_length=40)
    description = models.TextField()
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='site_photos/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.title} Project'

class Rating(models.Model):
    '''
    This model will contain the ratings for diffrent categories
    '''
    design = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    usability = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    content = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.user.username} {self.project.title} Rating'






