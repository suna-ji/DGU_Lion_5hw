from django.shortcuts import render, redirect
from django import forms
from .models import Pet, Product,Person,Movie,Review
import pdb
from tkinter import *
import tkinter.messagebox


# # Create your views here.

def movie_list(request):
    if request.method =="POST":
        mname = request.POST.get("title", "")
        return render(request,'first/input_info.html',{'mname':mname})
    return render(request,'first/movie_list.html')    


def review_list(request):
    about_time_reviews = Review.objects.filter(mname = "어바웃타임")
    perfect_stranger_reviews = Review.objects.filter(mname = "완벽한 타인")
    real_reviews = Review.objects.filter(mname = "리얼")
    wall_e_reviews = Review.objects.filter(mname = "월E")
    return render(request,'first/review_list.html',{'about_time_reviews':about_time_reviews,
    'perfect_stranger_reviews':perfect_stranger_reviews,'real_reviews':real_reviews,'wall_e_reviews':wall_e_reviews})    


def input_info(request):
    if request.method =="POST":
       mname = request.POST.get('mname')
       pname = request.POST.get('pname')
       age = request.POST.get('age')
       description = request.POST.get('description')
       review= Review(mname = mname, pname = pname, age = age, description = description)
       review.save()
       return redirect('review_list')
    return render(request,'first/input_info.html')
     

def edit(request, id):
    review = Review.objects.get(pk = id)
    return render(request,'first/edit.html', {'review':review}) 
    

def update(request,id):
    if request.method == "POST":
        review = Review.objects.get(pk = id)
        mname=  request.POST.get('mname')
        pname = request.POST.get('pname')
        age = request.POST.get('age')
        description =  request.POST.get('description')
        review.mname = mname
        review.pname = pname
        review.age = age
        review.description = description
        review.save()
        return redirect('review_list')
        

def delete(request,id):
    if request.method == "POST":
        review = Review.objects.get(pk = id)
        review.delete()
        return redirect('review_list')