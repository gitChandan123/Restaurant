from pyexpat.errors import messages
from django.shortcuts import redirect, render
from Base_App.models import BookTable,AboutUs,feedback,ItemList,Items,Login,Register
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect # type: ignore
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
# Create your views here.
def homeView(request):
    review = feedback.objects.all()
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'home.html',{'items':items,'list':list,'review':review})

def aboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html',{'data':data})

def menuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html',{'items':items,'list':list})


@login_required(login_url='/login/')
def bookTableView(request):    
    # print(f"Next parameter: {request.GET.get('next')}")
    return render(request, 'book_table.html')


@login_required(login_url='/login/')
def feedbackView(request):
    return render(request, 'feedback.html')

# user login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwaord = request.POST['password']
        user  = authenticate(request,username=username,passwaord=passwaord)
        
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html',{'form':form})