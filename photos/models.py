from django.db import models

class Photos(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=40)
    

class Location(models.Model):
    name = models.CharField(max_length=40)
    
