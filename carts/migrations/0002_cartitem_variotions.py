# Generated by Django 4.1.1 on 2022-10-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variotions',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]