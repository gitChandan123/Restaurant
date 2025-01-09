"""
URL configuration for Restaurant_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Base_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView,name="Home"),
    # the below path is 
    path('book_table/', login_required(bookTableView, login_url='/login/'), name='Book_Table'),
    path('menu/', menuView,name='Menu'),
    path('about/', aboutView,name='About'),
    path('feedback/', login_required(feedbackView, login_url='/login/'), name='Feedback_Form'),
    # path('login_register/', login_register,name='Login_Register'),
    path('login/', user_login,name='Login'),
    path('register/', user_register,name='Register'),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
