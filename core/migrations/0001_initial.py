# Generated by Django 3.2 on 2021-04-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcm_token', models.TextField()),
                ('notification_text', models.TextField()),
                ('notification_icon', models.ImageField(upload_to='media')),
            ],
        ),
    ]
