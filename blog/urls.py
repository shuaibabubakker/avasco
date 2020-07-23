from django.urls import path
from django.contrib import admin
from .views import *
from . import views

urlpatterns = [
    path('',views.home , name='blog-home'),
    path('about/', views.about, name='blog-about'),
    
    path('posts/',PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    path('gallery/', views.gallery, name='gallery'),
    path('members/', MemberListView.as_view(), name='members'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('timeline/',TimelineListView.as_view() , name='timeline'),
]