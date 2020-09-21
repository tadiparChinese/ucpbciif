# Generated by Django 2.1.7 on 2020-08-02 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0008_auto_20200730_0614'),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('committee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewedNotifcations', to='committees.Committee')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificationViewers', to='notifications.Notification')),
            ],
        ),
    ]