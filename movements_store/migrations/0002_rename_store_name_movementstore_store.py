# Generated by Django 4.1.3 on 2022-11-25 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movements_store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movementstore',
            old_name='store_name',
            new_name='store',
        ),
    ]