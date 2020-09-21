# Generated by Django 2.1.7 on 2020-07-14 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_payment_outstandingbalance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=24),
        ),
        migrations.AlterField(
            model_name='payment',
            name='outStandingBalance',
            field=models.DecimalField(decimal_places=2, max_digits=24),
        ),
        migrations.AlterField(
            model_name='payment',
            name='overPayment',
            field=models.DecimalField(decimal_places=2, max_digits=24),
        ),
        migrations.AlterField(
            model_name='payment',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=24),
        ),
    ]
