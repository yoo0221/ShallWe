"""ShallWe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from MainApp import views
from AccountApp import views as accviews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', accviews.register, name='register'),
    path('login/', accviews.login, name='login'),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('search/filtered', views.filtered, name='filtered'),
    path('setprofile/', views.setprofile, name='setprofile'),    
    path('themaselect/', views.themaselect, name='themaselect'),   
    path('logout/',accviews.logout, name='logout'),
    path('thema/', views.thema, name='thema'),   
    path('promise/', views.promise, name='promise'),
    path('meet/', views.meet, name="meet"), 
    path('register/complete', accviews.register_complete, name="register_complete"),
    path('chat/', views.chat, name="chat"),
    path('thema2/', views.thema2, name="thema2"), 
    path('detailProfile/', views.detail_profile, name="detail_profile"), 
    path('specialThema/', views.special_thema, name="special_thema"),
    path('remind/', views.remind, name="remind"), 
    path('preview/', views.preview, name="preview"), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
