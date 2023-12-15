
from django.contrib import admin
from django.urls import path
from django.urls import include
from sales import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('user/', views.userinput),
    path('user/', views.userinput, name='userinput'),

    path('viewdata/', views.viewdata, name='viewdata'),

]


