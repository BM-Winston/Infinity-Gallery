from django.shortcuts import render
from django.http  import HttpResponse
from .models import Photos

# HttpResponse returns a HttpResponse to the user.
def photos(request):
    photos = Photos.objects.all()
    return render(request, 'index.html',{"photos": photos})
    
def search_results(request):
    if 'photos' in request.GET and request.GET['photos']:
        search_term = request.GET.get('photos')
        items = Photos.search_image(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,'items':items})

    else:
        message = "No results found"
        return render(request,'search.html',{"message":message})


