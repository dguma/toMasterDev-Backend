from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Posts(models.Model):
    name = models.CharField(max_length=150)
    # date = models.DateField(blank=True)
    title = models.CharField(max_length=250)
    description= RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Subjects(models.Model):
    focus = models.CharField(max_length=255)
    focusDefinition = models.TextField()
    focusContent = RichTextField()
    focusLinks = models.CharField(max_length=255, blank=True)
    focusImages = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.focus

class User(models.Model):
    firstName = models.CharField(max_length=155)
    lastName = models.CharField(max_length=155)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=155)


    def __str__(self):
        return self.firstName
