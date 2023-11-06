from django.db import models


# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_category = models.CharField(max_length=50)
    book_description = models.TextField(max_length=10000)
    book_rating = models.FloatField()
    book_image = models.ImageField(upload_to='images', default='images/none/noimg.jpg')

    def __str__(self):
        return self.book_name
