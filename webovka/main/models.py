from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=10, choices=[("M", "Male"), ("F", "Female")], blank=True, null=True)
    birth_date = models.DateField(default="Unknown", blank=True, null=True)
    birthplace = models.CharField(default="Unknown", max_length=200, blank=True, null=True)
    education = models.TextField(default="Unknown", max_length=2000, blank=True, null=True)
    work = models.CharField(default="Unknown", max_length=50, blank=True, null=True)
    hobbies = models.TextField(default="Unknown", max_length=2000, blank=True, null=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)
    photos = models.ImageField(upload_to="photos/", blank=True, null=True)
    contact = models.EmailField(default="Unknown", blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    marital_status = models.CharField(max_length=20)
    deceased = models.BooleanField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

class Family(models.Model):
    name = models.CharField(max_length=100)
    introduction = models.CharField(max_length=200, blank=True, null=True)
    commentary = models.TextField(max_length=5000, blank=True, null=True)
    common_photos = models.ImageField(upload_to="photos/siblings/", blank=True, null=True)
    person = models.ForeignKey(Person, related_name="family", on_delete=models.CASCADE())

class Relative(models.Model):
    name = models.CharField(max_length=100)
    family = models.ForeignKey(related_name="family", family=Family)
    relation_type = models.CharField(max_length=50)
