"""crud_master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from first import urls as first_urls
from . import views
import first.views as first_view
# from users import views

urlpatterns = [
    path('', first_view.movie_list),
    # path('', views.create_user),
    # 아무것도 없는 경로에서 앱안에 있는 views를 가져오고 싶다->import로 가져와서 사용하자!
    path('admin/', admin.site.urls),
    path('first/', include(first_urls)),
]
