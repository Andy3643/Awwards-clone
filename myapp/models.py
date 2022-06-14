from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    '''
    Model for user profile
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # profile_pic = models.ImageField(upload_to='site_photos/')
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
    
    
    
class Project(models.Model):
    '''
    Model for uploaded projects
    '''
    title = models.CharField(max_length=40)
    description = models.TextField()
    link = models.CharField(max_length=255)
    image = CloudinaryField('image')
    #image = models.ImageField(upload_to='site_photos/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.title} Project'

    # def save_post(self):
    #     self.save()

    # def delete_post(self):
    #     self.delete()

    # @classmethod
    # def all_projects(cls):
    #     return cls.objects.all()


    # @classmethod
    # def search_projects(cls,title):
    #     return cls.objects.filter(title__icontains=title).all()




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






