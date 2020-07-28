# Generated by Django 2.1.7 on 2020-06-29 09:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('paymentCycle', models.PositiveIntegerField(default=720, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(720)])),
                ('remarks', models.TextField(blank=True, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now_add=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paymentPeriodCreatedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('days', models.PositiveIntegerField(default=720, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(720)])),
                ('remarks', models.TextField(blank=True, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now_add=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('createdBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='termCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('paymentPeriod', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='terms', to='loans.PaymentPeriod')),
            ],
        ),
        migrations.RemoveField(
            model_name='loan',
            name='loanAmount',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='loanName',
        ),
        migrations.AddField(
            model_name='loan',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='createdBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loanCreatedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='loan',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='dateUpdated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='interestRate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='loan',
            name='purpose',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='term',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loans', to='loans.Term'),
        ),
    ]
