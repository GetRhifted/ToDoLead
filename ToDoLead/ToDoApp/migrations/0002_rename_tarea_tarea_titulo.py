# Generated by Django 4.2.2 on 2023-06-20 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='Tarea',
            new_name='Titulo',
        ),
    ]
