from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    price = models.FloatField()
    image_link = models.URLField(default="")

    def __str__(self):
        return f"Name: {self.name} \nEmail: {self.email}\nPhone: {self.phone} \nPrice: ${self.price}"

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='albums')

class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    source = models.URLField(default="")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')