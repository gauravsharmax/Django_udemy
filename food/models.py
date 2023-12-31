from django.db import models

# Create your models here.
class Item(models.Model):
    def __str__(self) -> str:
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField() 
    item_image = models.CharField(max_length=500, default="https://cdn.dribbble.com/users/1515327/screenshots/4328124/cooking_loader_2_still.gif?resize=400x0")