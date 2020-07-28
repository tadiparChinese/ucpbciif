# Generated by Django 2.1.7 on 2020-07-09 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0012_auto_20200709_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditline',
            name='interestRate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='creditline',
            name='purpose',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='creditline',
            name='security',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='creditline',
            name='term',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creditLines', to='loans.Term'),
        ),
    ]
