from django.db import models
from django.urls import reverse
# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    def __str__(self):
        return  self.first_name + " " + self.last_name
    def get_absolute_url(self):
        return reverse('classBasedView:classDetail' , kwargs={'pk':self.pk})


class Album(models.Model):
    artist = models.ForeignKey(Musician , on_delete=models.CASCADE , related_name='album_list')
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    rating = (
        (1 , "worst"),
        (2 , "Bad"),
        (3 , "Not_Bad"),
        (4 , "Excellent"),
        (5 , "Good")
    )

    num_stars = models.IntegerField(choices=rating)

    def __str__(self):
        return "name: "+ self.name + ", Rating: " + str(self.num_stars)