from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import markdown
from datetime import timedelta
from django.utils import timezone

def home_view(request):
    last_week = timezone.now() - timedelta(days=7)
    posts = Post.objects.filter(created_at__gte=last_week).order_by('-created_at')
    return render(request, 'home/home.html', {'posts': posts})

def about_view(request):
    return render(request, 'home/about.html')
