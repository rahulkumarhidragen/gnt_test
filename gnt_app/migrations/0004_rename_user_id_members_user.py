# Generated by Django 5.0.4 on 2024-04-12 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gnt_app', '0003_tbl_member_members'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='user_id',
            new_name='user',
        ),
    ]
