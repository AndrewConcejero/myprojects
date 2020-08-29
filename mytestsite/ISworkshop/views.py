from django.shortcuts import render
from .models import ProfilePage

# Create your views here.
def index(request):
  posts = ProfilePage.objects.all()
  return render(request, 'ISworkshop/profilepage.html', {'posts': posts})
  
def form(request):

  return render(request, 'ISworkshop/profilepageforms.html', {})

