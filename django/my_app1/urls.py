from django.conf.urls import url
from django.urls import path
from my_app1 import views

app_name = "my_app1"

urlpatterns = [
    path('' , views.home , name='Home'),
    path('add_musician/' , views.add_musician , name='AddMusician'),
    path('add_album/' , views.add_album , name='AddAlbum'),
    path('album_list/<int:artist_id>/' , views.album_list , name='AlbumList'),
    path('edit_artist/<int:artist_id>/' , views.edit_artist , name='EditArtist'),
    path('edit_album/<int:album_id>/' , views.edit_album , name='EditAlbum'),
    path('delete_album/<int:album_id>/' , views.delete_album , name='DeleteAlbum'),
]