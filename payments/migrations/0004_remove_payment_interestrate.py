# Generated by Django 2.1.7 on 2020-07-13 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20200713_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='interestRate',
        ),
    ]
