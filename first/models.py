from django.db import models
from django import forms

# Create your models here.
#여기서 모델링
#class란 하나의 객체의 속성을 만들때 사용
class Pet(models.Model):
    species = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    price = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.title


class Person(models.Model):
    name = models.CharField(max_length = 100)
    major = models.CharField(max_length = 200)
    age = models.IntegerField()
    fav_movie = models.CharField(max_length = 500)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    genre = models.CharField(max_length = 100)
    name = models.CharField(max_length = 200)
    count = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    pname = models.CharField(max_length = 100)
    age = models.IntegerField()
    mname = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.mname
    
#모델링(설계)    
    
    
