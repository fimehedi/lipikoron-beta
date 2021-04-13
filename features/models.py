from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class page(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=100)
    body = RichTextUploadingField()

    def __str__(self):
        return self.title


class event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    poster = models.ImageField()
    url = models.URLField()

    def __str__(self):
        return self.title


class live(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    thumbnail = models.ImageField()
    url = models.URLField()

    def __str__(self):
        return self.title


class teamProfile(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    picture = models.ImageField()

    class Meta:
        verbose_name_plural = "Team"

    def __str__(self):
        return self.name


class meme(models.Model):
    title = models.CharField(max_length=100)
    meme = models.ImageField()

    def __str__(self):
        return self.title


class quote(models.Model):
    author = models.CharField(max_length=50)
    quotation = models.TextField(max_length=75)

    def __str__(self):
        return self.quotation
