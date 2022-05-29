from django.shortcuts import render
from django.http  import HttpResponse

# HttpResponse returns a HttpResponse to the user.
def message(request):
    return render(request, 'index.html')