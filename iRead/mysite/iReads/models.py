from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class StoriesCat(models.Model):
    id=models.AutoField(primary_key=True)
    catName=models.CharField(max_length=25)
    catDesc=models.TextField()
    def __str__(self):
        return self.catName
    
class DiscussionCat(models.Model):
    id=models.AutoField(primary_key=True)
    catName=models.CharField(max_length=25)
    catDesc=models.TextField()
    def __str__(self):
        return self.catName
    

class StoriesThreads(models.Model):
    id=models.AutoField(primary_key=True)
    type=models.ForeignKey("StoriesCat", on_delete=models.CASCADE)
    author=models.CharField(max_length=100,default="skrb7f16")
    name=models.CharField(max_length=100)
    head=models.TextField()
    body=models.TextField()
    conclusion=models.TextField()
    def __str__(self):
        return self.name
    
class DiscussionThreads(models.Model):
    id=models.AutoField(primary_key=True)
    type=models.ForeignKey("DiscussionCat", on_delete=models.CASCADE)
    author=models.CharField(max_length=100,default="skrb7f16")
    name=models.CharField(max_length=100)
    head=models.TextField()
    body=models.TextField()
    conclusion=models.TextField()
    def __str__(self):
        return self.name


class Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    type=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    onpost=models.IntegerField()

class Contact(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    message=models.TextField()
    def __str__(self):
        return self.name
    



