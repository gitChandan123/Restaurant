from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class ItemList(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name
    
class Items(models.Model):
    Item_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    Category = models.ForeignKey(ItemList,related_name='name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Items/')
    
    def __str__(self):
        return self.Item_name
    
class AboutUs(models.Model):
    Description = models.TextField()
    
class feedback(models.Model):
    user_name = models.CharField(max_length=50)
    Rating = models.IntegerField()
    Message = models.TextField(blank=False)
    c_image = models.ImageField(upload_to='Items/',default='/')
    def __str__(self):
        return self.user_name
    
    
class BookTable(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone_number = models.IntegerField()    
    total_person = models.IntegerField()
    Booking_date =  models.DateField()
    
    def __str__(self):
        return self.Name
    
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    
class Register(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.username
    
    
