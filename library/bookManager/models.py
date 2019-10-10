from django.db import models

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=20)
    author_age = models.IntegerField()
    author_sex = models.CharField(max_length=10)

    def __str__(self):
        return "%s the author" % self.author_name


class Publish(models.Model):
    publish_name = models.CharField(max_length=20)
    publish_phone = models.CharField(max_length=20)
    publish_address = models.CharField(max_length=50)

    def __str__(self):
        return "%s the publish" % self.publish_name


class Book(models.Model):
    book_name = models.CharField(max_length=50)
    book_price = models.FloatField()
    book_pubdate = models.DateTimeField()
    book_author = models.ManyToManyField(Author)
    book_publish = models.ForeignKey(Publish, on_delete=models.CASCADE)

    def __str__(self):
        return "%s the book" % self.book_name

