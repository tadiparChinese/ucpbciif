# Generated by Django 2.1.7 on 2020-07-27 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0027_auto_20200727_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='dateReleased',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]