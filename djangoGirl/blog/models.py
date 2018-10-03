from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# making some Other Table for learing...


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


# class PersonShirt(models.Model):
#     SHIRT_SIZES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )
#     name = models.CharField(max_length=60)
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, null = True)


class Musician(models.Model):
    first_name=models.CharField(max_length = 50)
    last_name=models.CharField(max_length = 50)
    instrument=models.CharField(max_length = 100)

    def __str__(self):
        return self.first_name


class Album(models.Model):
    artist=models.ForeignKey(Musician, on_delete = models.CASCADE)
    name=models.CharField(max_length = 100)
    release_date=models.DateField()
    num_stars=models.IntegerField()


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)