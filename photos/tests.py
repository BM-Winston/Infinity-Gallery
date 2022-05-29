from django.test import TestCase
from .models import Photos, Category, Location

class  PhotosTestCase(TestCase):
    # Set Up method
    def setUp(self):
        self.maldives=Photos(name='Find out why Malldives is popular', description='pristine beaches and sprawling greenery', category=Category(name='islands'), location=Location(name='Indian Ocean'))

        

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.maldives,Photos))


    # Testing save method
    def test_save_method(self):
        self.maldives.save_photos()
        photos = Photos.objects.all()
        self.assertTrue(len(photos) > 0)
