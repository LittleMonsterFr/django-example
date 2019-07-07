from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place


def index(request):
    place_list = Place.objects.all()
    context = {'place_list': place_list}
    return render(request, 'places/index.html', context)


def detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return render(request, 'places/detail.html', {'place': place})


def delete_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place.delete()
    return HttpResponseRedirect(reverse('places:index'))


def add_place(request):
    name = request.POST['name']
    latitude = float(request.POST['latitude'])
    longitude = float(request.POST['longitude'])
    p = Place(name=name, latitude=latitude, longitude=longitude)
    p.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('places:index'))

