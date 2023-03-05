from django.shortcuts import render

from django.views.generic import ListView, DetailView
from rest_framework import generics

from .models import Post
from .serializers import BlogSerializer


class BlogListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
