from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),

    path('dashboard/', views.dashboard, name='dashboard'),  

    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),

    path('coding-awareness/', views.coding_awareness, name='coding_awareness'),
    path('project-guidance/', views.project_guidance, name='project_guidance'),
    path('hackathons/', views.hackathons, name='hackathons'),
    path('jobs-internships/', views.jobs_internships, name='jobs_internships'),
    path('roadmaps/', views.roadmaps, name='roadmaps'),
]