from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.forms import modelform_factory, modelformset_factory, inlineformset_factory

from .forms import NameForm, SongForm
from .models import Song, Playlist


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("song:get_name") + "?name=" + form.cleaned_data["your_name"])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "song/name.html", {"form": form})


def song(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("song:song"))
    else:
        form = SongForm()

    return render(request, "song/song.html", {"form": form})
