from django.db import models

# Create your models here.
class ItemList(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name
    
class Items(models.Model):
    Item_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList,related_name='name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Items/')
    
class AboutUs(models.Model):
    Description = models.TextField()
class feedback(models.Model):
    user_name = models.CharField(max_length=50)
    Rating = models.IntegerField()
    Message = models.TextField(blank=False)
    
class BookTable(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone_number = models.IntegerField()    
    total_person = models.IntegerField()
    Booking_date =  models.DateField()
    
    
    
