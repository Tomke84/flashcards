# Generated by Django 4.0.4 on 2024-09-19 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='answer',
            new_name='FR',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='question',
            new_name='NL',
        ),
    ]