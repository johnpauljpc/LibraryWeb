# Generated by Django 4.0.6 on 2023-05-20 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
