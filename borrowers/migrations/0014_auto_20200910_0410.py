# Generated by Django 2.1.7 on 2020-09-09 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrowers', '0013_auto_20200910_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background',
            name='cdaRegistrationDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
