from django.conf import settings
from django.db import models
from django.utils import timezone




class Persoana(models.Model):
    nume = models.CharField(max_length=200)
    prenume = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.prenume + " " + self.nume

class Domeniu(models.Model):
    nume = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nume

class Locatie(models.Model):
    nume = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nume

class Obiect(models.Model):
    nume = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nume

class Actiune(models.Model):
    domeniu = models.ForeignKey(Domeniu, on_delete=models.CASCADE)
    nume = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nume

class Activitate(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    actiune = models.ForeignKey(Actiune, on_delete=models.CASCADE,null=True)
    obiect = models.ForeignKey(Obiect, on_delete=models.CASCADE,null=True)
    nume = models.CharField(max_length=200)
    descriere = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nume