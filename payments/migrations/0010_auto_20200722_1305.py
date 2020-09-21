# Generated by Django 2.1.7 on 2020-07-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0009_payment_interestpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='days',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='interest',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='principal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='totalToPay',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
            preserve_default=False,
        ),
    ]
