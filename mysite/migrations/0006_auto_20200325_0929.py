# Generated by Django 3.0.3 on 2020-03-25 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20200325_0807'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
