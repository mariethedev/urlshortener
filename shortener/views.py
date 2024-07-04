from django.shortcuts import render, redirect , get_object_or_404
import uuid
from .models import Url
from django.http import HttpResponse, JsonResponse , HttpResponseNotFound
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError



#First view that renders the index.html page

def index(request):
    
    return render(request, 'index.html')

#View responsible for creating the shortened url

def create(request):
    
    if request.method == 'POST':        #checks if request is a post method so it handles it
        
        link = request.POST.get('link','')     #stores the link the user types in the variable called link
        
        #Validating the URL:
        validator = URLValidator()
        
        try:
            validator(link)
            
        except ValidationError:
            return JsonResponse({'error': 'Invalid URL. Please enter a valid URL.'}, status= 400)
        
        
        #Checking if URL already exists: 
        existing_url = Url.objects.filter(link=link).first()
        
        if existing_url:
            return HttpResponse(existing_url.uuid)
        
        
        #Generate a new short URL if user input passes all the checks:
        uid = str(uuid.uuid4())[:5]     #generates a shorter uuid of 5 characters and stores it in the uid field
        
        new_url = Url(link = link , uuid = uid)    #stores the link and its respective uid in a variable called new_url
        new_url.save()                             #saves the new url field into the database
        
        return HttpResponse(uid)                   #returns the shortened url to the user
    
    
    
#View responsible for redirecting to the new url

def go(request, pk):
    
    url_details = get_object_or_404(Url, uuid = pk)       #Stores the link object whose uuid is equal to the search parameter
    return redirect(url_details.link)              #Redirects to the original link using the link atrribute

def favicon(request):
    return HttpResponseNotFound()