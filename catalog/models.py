from django.db import models



class Phylum(models.Model):
    name = models.CharField(max_length=50)

class Class(models.Model):
    name = models.CharField(max_length=50)
    phylum = models.ForeignKey(Phylum)

class Order(models.Model):
    name = models.CharField(max_length=50)
    phylum = models.ForeignKey(Class)

class Family(models.Model):
    name = models.CharField(max_length=50)
    order = models.ForeignKey(Order)

class Genus(models.Model):
    name = models.CharField(max_length=50)
    family = models.ForeignKey(Family)

class Species(models.Model):
    name = models.CharField(max_length=50)
    family = models.ForeignKey(Genus)

class Animal(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images", blank=True)
    description = models.TextField(blank=True)
    species = models.ForeignKey(Species)