# Generated by Django 2.1.7 on 2020-06-05 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20200602_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='code',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
