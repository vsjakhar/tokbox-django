from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

# Create your views here.

def IndexView(request):
	return render(request,'common/index.html')
