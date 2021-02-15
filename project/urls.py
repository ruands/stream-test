"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from scores import api, views

urlpatterns = [
    path('', views.DashView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api/v1/scores/', api.TestScoreCreateView.as_view()),
    path('student/', views.StudentResultsView.as_view(), name="student"),
    path('subject/', views.SubjectResultsView.as_view(), name="subject"),
    path('test/', views.TestResultsView.as_view(), name="test")
]
