from django.db import models
from django.urls import reverse

# Create your models here.
class Year(models.Model):
    year=models.CharField(max_length=3)

    def __str__(self):
        return self.year
class Student(models.Model):

    name=models.CharField(max_length=30)
    rollnumber=models.CharField(max_length=11)
    branch=models.CharField(max_length=3)
    photo=models.ImageField()
    discription=models.CharField(max_length=6000)
    year=models.ForeignKey(Year,on_delete=models.CASCADE)

    def __str__(self):
        return self.name+"-"+self.rollnumber+"-"+self.year

    def get_absolute_url(self):
        return reverse('detail-s',kwargs={'pk':self.pk})





class Notification(models.Model):

    message=models.TextField()
    writeup=models.TextField()
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('see',kwargs={'pk':self.pk})


class Events(models.Model):
    name=models.CharField(max_length=20,default=None)
    type=models.CharField(max_length=20)
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=20)
    poster=models.ImageField()
    discription=models.TextField(null=True)

    def __str__(self):
        return self.type+"-"+self.discription

    def get_absolute_url(self):
        return reverse('event',kwargs={'pk':self.pk})


class BlogsWithoutMedia(models.Model):
    bloggername=models.CharField(max_length=20)
    blogsubject=models.CharField(max_length=40)
    blog=models.TextField()
    def __str__(self):
        return self.bloggername+"-"+self.blogsubject+"-"+self.blog

class BlogsWithMedia(models.Model):
    bloggername = models.CharField(max_length=20)
    blogsubject = models.CharField(max_length=40)
    blog = models.TextField()
    blogmedia=models.FileField()
    def __str__(self):
        return self.bloggername+"-"+self.blogsubject+"-"+self.blog
