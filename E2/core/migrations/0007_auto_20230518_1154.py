# Generated by Django 3.1.2 on 2023-05-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230516_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='producto',
        ),
        migrations.AddField(
            model_name='carrito',
            name='producto',
            field=models.ManyToManyField(to='core.Producto'),
        ),
    ]