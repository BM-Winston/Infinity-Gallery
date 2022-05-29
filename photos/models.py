from django.db import models

class Photos(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    location =models.ForeignKey('Location',on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
    def save_photos(self):
        self.save()
    
 


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

   
    
