from django.db import models

class Photos(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    location =models.ForeignKey('Location',on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
    def save_photo(self):
        self.save()
    
 


class Category(models.Model):
    name = models.CharField(max_length=40)


class Location(models.Model):
    name = models.CharField(max_length=40)

   
    
