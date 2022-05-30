from django.shortcuts import render
from django.http  import HttpResponse
from .models import Photos

# HttpResponse returns a HttpResponse to the user.
def photos(request):
    photos = Photos.objects.all()
    return render(request, 'index.html',{"photos": photos})
    
def search_results(request):
    if photos in request.GET and request.GET['photos']:
        search_term = request.GET.get('photos')
        searched_photos = Photos.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'index.html',{"message":message,"photos":searched_photos})

    else:
        message = "You have not searched for photos"
        return render(request,'index.html',{"message":message})


