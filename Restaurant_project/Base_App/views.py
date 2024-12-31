from django.shortcuts import render

# Create your views here.
def homeView(request):
    return render(request, 'home.html')

def aboutView(request):
    return render(request, 'about.html')

def menuView(request):
    return render(request, 'menu.html')

def bookTableView(request):
    return render(request, 'book_table.html')



