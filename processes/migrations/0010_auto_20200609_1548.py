# Generated by Django 2.1.7 on 2020-06-09 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('processes', '0009_step_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('isDefault', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now_add=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stepAttachmentCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachmentRequirements', to='processes.Step')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('isRequired', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now_add=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requirementsCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('subProcess', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processRequirements', to='processes.SubProcess')),
            ],
        ),
        migrations.RenameField(
            model_name='requirements',
            old_name='optional',
            new_name='isDefault',
        ),
        migrations.RemoveField(
            model_name='requirements',
            name='code',
        ),
        migrations.RemoveField(
            model_name='requirements',
            name='subProcess',
        ),
        migrations.AddField(
            model_name='requirements',
            name='isRequired',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='requirements',
            name='step',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='processes.Step'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='requirements',
            name='createdBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stepRequirementCreatedBy', to=settings.AUTH_USER_MODEL),
        ),
    ]
