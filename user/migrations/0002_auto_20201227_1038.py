# Generated by Django 3.1.1 on 2020-12-27 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users_Manage',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='title',
            new_name='name',
        ),
    ]
