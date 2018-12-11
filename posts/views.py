from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
# Create your views here.

class HomePageView(ListView):
	model=Post #tell which model we are using
	template_name="home.html" #tell the name of the template
	context_object_name="all_posts_list"
