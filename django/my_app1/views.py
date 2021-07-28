from my_app1 import models
from django.shortcuts import render
from django.http import HttpResponse
from my_app1 import forms
from django.db.models import Avg

def add_musician(request):
    # new_form = forms.user_form()
    diction = {
        'text1' : 'This is a form made using django',

        # 'django_form' : new_form
    }

    # if request.method == 'POST':
    #     new_form = forms.user_form(request.POST)
    #     diction.update({'django_form' : new_form})

    #     if new_form.is_valid() : 
    #         userName = new_form.cleaned_data['userName']
    #         userEmail = new_form.cleaned_data['email']
    #         userDob = new_form.cleaned_data['userDob']

    #         diction.update({'userName' : userName})
    #         diction.update({'userEmail' : userEmail})
    #         diction.update({'userDob' : userDob})
    #         diction.update({'formSubmitted' : True})

    musicianForm = forms.MusicianForm()

    if request.method == "POST":
        musicianForm = forms.MusicianForm(request.POST)
        if musicianForm.is_valid():
            musicianForm.save(commit=True)
            return home(request)

    diction.update({'musicianForm' : musicianForm})         
    return render(request, 'my_app1/add_musician.html' , context=diction)

def home(request):
    musicians = models.Musician.objects.order_by("first_name")
    diction = {
        'musicians' : musicians,
        'sampleText' : "Filter : "
    }
    return render(request , "my_app1/index.html" , context=diction)

def add_album(request):
    albumForm = forms.AlbumForm()
    diction = {"form" : albumForm}

    if request.method == "POST":
        albumForm = forms.AlbumForm(request.POST)
        if albumForm.is_valid():
            albumForm.save(commit=True)
            return home(request)

    diction.update({"form" : albumForm})
    return render(request , 'my_app1/add_album.html' , context=diction)


def album_list(request , artist_id):
    album_list = models.Album.objects.filter(artist=artist_id).order_by('name' , 'release_date')
    artist_rating = models.Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))
    artist_info = models.Musician.objects.get(pk=artist_id)
    diction = {
        "artist_info":artist_info,
        "album_list":album_list,
        "artist_rating":artist_rating,
    }
    return render(request , 'my_app1/album_list.html', diction)
    
def edit_artist(request , artist_id):
    artist_info = models.Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST , instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request , artist_id)

    diction = {
        "musician_form" : form,
    }
    return render(request , 'my_app1/edit_artist.html' , diction)


def edit_album(request , album_id):
    album_info = models.Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)

    diction = {
        'album_form' : form
    }

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST , instance=album_info)
        if form.is_valid():
            form.save(commit=True)
            diction.update({'success' : "Successfully updated"})
    
    diction.update({"album_form" : form })

    return render( request , 'my_app1/edit_album.html' , diction)

def delete_album(request , album_id):
    album = models.Album.objects.get(pk=album_id).delete()
    diction = {
        "success" : "Successfully deleted!"
    }
    return render(request , 'my_app1/delete_album.html' , diction)

