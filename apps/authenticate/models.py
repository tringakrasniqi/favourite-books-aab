from django.db import models


class User(models.Model):
    """
        Klasa User e krijon table User ne databazen e aplikacionit. Klasa e trashegon Model qe vjen nga Django ORM
        rekorded 'updated_at' dhe 'created_at' jane te zakonshme dhe preferohen te vendosen ne cdo tabele, mirepo nuk jane te domosdoshme
    """
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=100)
    birthdate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
