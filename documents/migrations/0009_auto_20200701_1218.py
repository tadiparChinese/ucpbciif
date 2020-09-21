# Generated by Django 2.1.7 on 2020-07-01 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0008_document_parentdocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='loan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loanDocuments', to='loans.Loan'),
        ),
    ]
