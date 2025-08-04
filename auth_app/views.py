from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

from django.contrib.auth import login,logout
from .middlewares import auth,guest
# from .models import UserProfile
#random referal code
import string
import random

def generate_referral_code(length=8):
   characters=string.ascii_uppercase+string.digits
   return ''.join(random.choices(characters,k=length))
   
# Create your views here.
def home(request):
   return render(request,'layouts/home.html')
@guest
def register_view(request):
  if request.method=='POST':
    form=UserCreationForm(request.POST)
    if form.is_valid():
      user=form.save()
      referral_code=generate_referral_code()
      
      print(referral_code)
      login(request,user)
      return redirect('dashboard')
  else:
    initial_data={'username':'','password1':'','password2':''}
    form=UserCreationForm(initial=initial_data)
  return render(request,'auth/register.html',{'form':form})  

@guest
def login_view(request):
  if request.method=='POST':
      form=AuthenticationForm(request,data=request.POST)
      if form.is_valid():
        user=form.get_user()
        print("User:", user)
        login(request,user)
        return redirect('dashboard')
        # return render(request,'layouts/dashboard.html')
        # return render(request,'layouts/dashboard.html')
      else:
            print("Form errors:", form.errors)  
  else:
      initial_data={'username':'','password':''}
      form=AuthenticationForm(initial=initial_data)
  return render(request,'auth/login.html',{'form':form})  

@auth
def dashboard_view(request):
      # profile=UserProfile.objects.get(user=request.user)
      return render(request,'layouts/dashboard.html')
def logout_view(request):
  logout(request)
  return render(request,'auth/logout.html')
  # return redirect('login')