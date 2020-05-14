# Generated by Django 2.1.7 on 2020-02-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenderType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('isDeleted', models.BooleanField(default=False)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Gender Type (System Essential)',
                'verbose_name_plural': 'Gender Types (System Essential)',
            },
        ),
    ]
