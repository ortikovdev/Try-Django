from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    UNIT = (
        (0, "Kilogram"),
        (1, "Gram"),
        (2, "Litre"),
        (3, "Piece"),
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
