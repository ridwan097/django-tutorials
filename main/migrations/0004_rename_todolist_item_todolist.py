# Generated by Django 3.2.6 on 2021-08-09 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_todolist_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='todoList',
            new_name='todolist',
        ),
    ]
