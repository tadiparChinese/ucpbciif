# Generated by Django 2.1.7 on 2020-07-29 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0034_auto_20200729_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='amortizationitem',
            name='daysAdvanced',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='amortizationitem',
            name='daysExceed',
            field=models.PositiveIntegerField(default=0),
        ),
    ]