from pyexpat.errors import messages
from django.shortcuts import redirect, render
from Base_App.models import BookTable,AboutUs,feedback,ItemList,Items
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse

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


@login_required
def bookTableView(request):    
    return render(request, 'book_table.html')


@login_required
def feedbackView(request):
    return render(request, 'feedback.html')

# View for login page
def loginView(request):
    next_url = request.GET.get('next', reverse('Feedback_Form'))  # Default to 'Feedback_Form' URL if no next param

    # If the user is already logged in, redirect them to the next URL
    if request.user.is_authenticated:
        return redirect(next_url) # next_url is the URL to redirect to after login

    # Handle form submission (POST request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate and log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                next_url = request.POST.get('next')
            # Redirect to the 'next' URL after login
            else:
                return redirect('feedback') # Redirect to the feedback page after login
    else:
        form = AuthenticationForm()  # Create an empty form if the request is not POST

    # Render the login page with the form
    return render(request, 'login.html', {'form': form})
