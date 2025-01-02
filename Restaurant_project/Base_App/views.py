from django.shortcuts import render
from Base_App.models import BookTable,AboutUs,feedback,ItemList,Items

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

def bookTableView(request):
    return render(request, 'book_table.html')

def feedbackView(request):
    review = feedback.objects.all()
    return render(request, 'feedback.html',{'review':review})



