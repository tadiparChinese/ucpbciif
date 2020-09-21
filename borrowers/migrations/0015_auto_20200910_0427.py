# Generated by Django 2.1.7 on 2020-09-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrowers', '0014_auto_20200910_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='educationalAttainment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='grant',
            name='donor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='standingcommittee',
            name='department',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='standingcommittee',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
