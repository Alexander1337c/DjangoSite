from django.db import models

# Create your models here.


class Games(models.Model):
    title = models.CharField(max_length=255)
    descr = models.TextField()
    photo = models.ImageField(upload_to='imgs/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
