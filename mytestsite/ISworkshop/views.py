from django.shortcuts import render, redirect
from .models import ProfilePage
from .forms import UpdateProfileForm

def index(request):
  posts = ProfilePage.objects.get(student_number=12345)
  return render(request, 'ISworkshop/profilepage.html', {'posts': posts})
  
def form(request):
  post = ProfilePage.objects.get(student_number=12355)
  if request.method == "POST":
    profile_form = UpdateProfileForm(request.POST, request.FILES, instance=post)
    if profile_form.is_valid():
      profile_form.save()
      return redirect("profilepageforms")
  else:
    profile_form = UpdateProfileForm(instance=post)
  
  return render(request, 'ISworkshop/profilepageforms.html', {"profile_form":profile_form})

