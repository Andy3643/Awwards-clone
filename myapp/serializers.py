from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ["title","description","link","image"]
        
        
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic']

