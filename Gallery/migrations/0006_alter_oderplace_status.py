# Generated by Django 4.0.3 on 2022-08-07 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0005_rename_contact_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oderplace',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('On the Way', 'On the way'), ('Delivered', 'Deliverd'), ('Cancle', 'Cancle')], default='Panding', max_length=200),
        ),
    ]
