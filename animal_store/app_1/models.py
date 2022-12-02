from django.db import models
from taggit.managers import TaggableManager
from django.core.validators import RegexValidator


letters = RegexValidator(r'^[a-zA-Z]*$', 'Only letters allowed!')

class Animal(models.Model):
    id = models.BigAutoField(primary_key=True)
    animalName = models.CharField(max_length=50, unique=True, validators=[letters])
    imageURl = models.CharField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    tags = TaggableManager()

    class Status(models.TextChoices):
        placed = 'placed'
        approved = 'approved'
        delivered = 'delivered'

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.placed)

    class Category(models.TextChoices):
        mammal = 'mammal'
        fish = 'fish'
        bird = 'bird'
        reptile = 'reptile'
        amphibian = 'amphibian'

    category = models.CharField(max_length=10, choices=Category.choices, default=Category.mammal)

