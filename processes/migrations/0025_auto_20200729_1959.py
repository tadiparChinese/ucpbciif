# Generated by Django 2.1.7 on 2020-07-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0024_output_callbacklink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='position',
            field=models.ManyToManyField(blank=True, related_name='positions', to='committees.Position'),
        ),
    ]
