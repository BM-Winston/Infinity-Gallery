from django.db import models

class Photos(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=True)
    location =models.ForeignKey('Location',on_delete=models.DO_NOTHING, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to= 'infinity_photo/', null=True)

   
    def save_image(self):
        self.save()


    def delete_image(self):
        self.delete()
        
    def update_image(self, name,image, description, location,category):
        self.image = image,
        self.name = name,
        self.description = description,
        self.location = location,
        self.category = category
    
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.get(image_id = id)
        return image

    @classmethod
    def search_image(cls, search_term):
        image = Photos.objects.filter(category__name__icontains=search_term)
        return image


    @classmethod
    def filter_by_location(cls, location):
        image = cls.objects.filter(location__name__icontains=location)
       
        return image


    def __str__(self):
        return self.name
    
    
 


class Category(models.Model):
    name = models.CharField(max_length=40)

    
   
    def __str__(self):
        return self.name


    def save_category(self):
        return self.save()

    def delete_category(self):
        return self.delete()

    @classmethod
    def update_category(cls, id, name):
        cls.objects.filter(category_id=id).update(category_name=name)


class Location(models.Model):
    name = models.CharField(max_length=40)


    def __str__(self):
        return self.name


    def save_location(self):
        return self.save()

    def delete_location(self):
        return self.delete()

    @classmethod
    def update_location(cls, id, name):
        cls.objects.filter(location_id=id).update(location_name=name)



  

   
    
