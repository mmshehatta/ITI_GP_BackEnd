# Generated by Django 3.2 on 2021-04-26 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('needs', '0003_need_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='need',
            name='name',
        ),
    ]