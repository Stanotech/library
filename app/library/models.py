from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('author', on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    available = models.BooleanField(default=True)

class author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.title
