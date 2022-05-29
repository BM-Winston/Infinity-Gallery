from django.shortcuts import render
from django.http  import HttpResponse

# HttpResponse returns a HttpResponse to the user.
def message(request):
    return HttpResponse('This is the Infinity-Gallery. Classic photos for you.')