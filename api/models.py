from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Poziva /users -> SELECT * FROM users -> Python ORM objekat (objekat iz baze sa rez.)
# Python ORM objekat -> Serializer -> JSON -> Klijent


# Poziva API
# Dobijamo podatke u vidu JSON-a
# [ Poziv ] -> Serializer -> [ JSON => Python list ]
