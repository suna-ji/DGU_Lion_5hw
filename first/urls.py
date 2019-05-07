from django.contrib import admin
from django.urls import path
from . import views
# 각각의 templates를 구동할 views를 불러옵니다.
# 우리는 MVT 중 V! views 를 통해 T! templates를 불러오는 거니까!

urlpatterns = [
    path('',views.movie_list, name = "movie_list"),
    path('input_info/', views.input_info, name = "input_info"),
    path('movie_list/', views.movie_list,name ="movie_list"),
    path('review_list/', views.review_list, name = "review_list"),
    path('edit/<int:id>/',views.edit, name = "edit"),
    path('update/<int:id>', views.update, name = "update"),
    path('delete/<int:id>', views.delete, name = "delete"),
]
