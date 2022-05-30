from django.db import models

class Photos(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    location =models.ForeignKey('Location',on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to= 'infinity_photo/', null=True)

   
    def save_photos(self):
        self.save()


    def delete_photo(self, photo_id):
        Photos.objects.filter(id= photo_id).delete()


    @classmethod
    def update_photo(cls, photo_id, updated_name):
        cls.objects.filter(id=photo_id).update(name = updated_name)

    @classmethod
    def get_photo_by_id(cls, photo_id):
        get_photo = cls.objects.get(pk = photo_id)
        return get_photo

    @classmethod
    def search_by_category(cls, search_term):
        photos = cls.objects.filter(category__icontains=search_term)
        return photos


    @classmethod
    def filter_by_location(cls, location):
        get_photos = cls.objects.filter(location = location)
        return get_photos


    def __str__(self):
        return self.name
    
    
 


class Category(models.Model):
    name = models.CharField(max_length=40)

    
    def save_category(self):
        self.save()
    
    def delete_category(self, category_id):
        Category.objects.filter(id= category_id).delete()

    @classmethod
    def update_category(cls, category_id, updated_name):
        updated = cls.objects.filter(id=category_id).update(name = updated_name)
        return updated

    def __str__(self) -> str:
        return f'{self.name}'


class Location(models.Model):
    name = models.CharField(max_length=40)


    def __str__(self) -> str:
        return f'{self.name}'

    def save_location(self):
        self.save()

    def delete_location(self, location_id):
        Location.objects.filter(id= location_id).delete()

    @classmethod
    def update_location(cls, location_id, updated_name):
        cls.objects.filter(id=location_id).update(name = updated_name)


   
    
