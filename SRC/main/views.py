from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from .models import Listing
from .forms import ListingForm
from users.forms import LocationForm
from django.contrib import messages


def main_view(request):
    return render(request, 'views/main.html' ,{"name":"AutoMax"})
@login_required   
def home_view(request):
    listings = Listings.objects.all()
    context = {
        'listings': listings
    }
    return render(request,'views/home.html')

@login_required
def list_view(request):
    
    if request.method=='POST':
        try:
            listing_form = ListingForm(request.POST,request.FILES)
            location_form = LocationForm()
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit = False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
            else:
                raise Exception()
        except Exception as e:
            messages.error(request, f'An error {e} occured trying to list.')
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()
        return render(request, 'views/list.html', {'listing_form':listing_form,'location_form':location_form})