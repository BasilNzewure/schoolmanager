from django.db import models
from pytz import timezone
import datetime
from django.utils import timezone


# Create your models here.

class AuthorBooks(models.Model):
    title = models.CharField("Book Title", max_length=200)
    edition = models.CharField("Edition", max_length=200, default = "11th Edition")
    author = models.CharField("Author", max_length=200, default = "Basil Isaac Nzewure")
    publication_yr = models.DateField("Publication Year", default = timezone.now())
    publisher = models.CharField("Publisher", max_length=200, default="Bin Binary Publishers")
    cover = models.ImageField("Book Cover")


    def __strt__(self):
        return f"{self.title}, {self.edition}, {self.author}, {self.publication_yr}, {self.publisher}, {self.cover}"

