# Generated by Django 3.2 on 2021-04-27 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210427_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificationhistory',
            old_name='notification_body',
            new_name='notification_text',
        ),
    ]
