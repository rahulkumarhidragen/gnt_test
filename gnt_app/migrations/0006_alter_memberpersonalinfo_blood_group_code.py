# Generated by Django 5.0.4 on 2024-04-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gnt_app', '0005_memberaddress_membernomineeinfo_memberpaymentinfo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberpersonalinfo',
            name='blood_group_code',
            field=models.CharField(max_length=25),
        ),
    ]
