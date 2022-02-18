from re import S
from django.db import models
from django.forms import DateTimeField

# Create your models here.




class Personne(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Personne'
        verbose_name_plural = 'Personnes'

    def __str__(self):
        return self.last_name

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
    
    def __str__(self):
        return self.name


class Commande(models.Model):
    personne = models.ForeignKey(Personne, related_name="commande_personne", on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, related_name="menu_commande", on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Commande'
        verbose_name_plural = 'Commandes'

    def __str__(self):
        return f"{self.personne}, {self.menu}"
    

    
    
