# Generated by Django 2.1.7 on 2020-07-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0010_auto_20200722_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='principalBalance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
            preserve_default=False,
        ),
    ]
