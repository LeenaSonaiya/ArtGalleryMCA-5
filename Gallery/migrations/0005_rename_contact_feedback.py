# Generated by Django 4.0.3 on 2022-08-07 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0004_alter_customer_state'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='feedback',
        ),
    ]
