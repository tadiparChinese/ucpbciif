# Generated by Django 2.1.7 on 2020-07-01 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import processes.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0009_auto_20200701_1218'),
        ('processes', '0021_auto_20200622_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessRequirementAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=255)),
                ('fileAttachment', models.FileField(blank=True, null=True, upload_to=processes.models.process_attachment_directory_path)),
                ('description', models.TextField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now_add=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='processAttachmentCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentProcessRequirementAttachments', to='documents.Document')),
                ('processRequirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processRequirementAttachments', to='processes.ProcessRequirement')),
            ],
        ),
    ]
