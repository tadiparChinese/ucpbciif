# Generated by Django 2.1.7 on 2020-10-06 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('borrowers', '0023_remove_branch_clientsince'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='branch',
            field=models.ForeignKey(blank=True, default=6, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='borrowerBranch', to='borrowers.Branch'),
        ),
    ]