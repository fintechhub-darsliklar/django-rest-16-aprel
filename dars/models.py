from django.db import models

# Create your models here.


class Telefon(models.Model):
    name = models.CharField(max_length=200)
    narx = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} {self.narx}"

# makemigrations, migrate



class Noutbook(models.Model):
    name = models.CharField(max_length=250)
    narx = models.IntegerField()


    def __str__(self):
        return f"{self.name} {self.narx}"

class TV(models.Model):
    narx = models.CharField(max_length=250)
    brend = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.narx} {self.brend}"