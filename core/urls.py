from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.home, name="home"),
        path('edu', views.education, name="edu"),
        path('skills', views.skills, name="skills"),
        path('projects', views.projects, name="projects"),
        path('ex', views.experience, name="ex"),
        path('github', views.github, name="github"),
        path('resume', views.resume, name="resume"),
        path('linkedin', views.linkedin, name="linkedin"),
        path('medium', views.medium, name="medium"),
        path('contact', views.contact, name="contact"),
        path('jarvis-chat/', views.jarvis_chat, name='jarvis_chat'),
]