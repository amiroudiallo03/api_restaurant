# Generated by Django 4.0.2 on 2022-02-17 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0002_remove_commande_menu_commande_menus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='menus',
        ),
        migrations.AddField(
            model_name='commande',
            name='menu',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='menu_commande', to='restaurantapp.menu'),
            preserve_default=False,
        ),
    ]
