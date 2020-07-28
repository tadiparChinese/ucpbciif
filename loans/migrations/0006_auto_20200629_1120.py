# Generated by Django 2.1.7 on 2020-06-29 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0005_auto_20200629_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='borrower',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='borrowers.Borrower'),
            preserve_default=False,
        ),
    ]
