# Generated by Django 2.1.7 on 2020-08-16 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0013_auto_20200729_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='isPaymentExtension',
            field=models.BooleanField(default=False),
        ),
    ]
