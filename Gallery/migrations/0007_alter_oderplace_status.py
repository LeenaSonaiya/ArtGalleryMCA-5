# Generated by Django 4.0.3 on 2022-08-08 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0006_alter_oderplace_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oderplace',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('On the Way', 'On the way'), ('Delivered', 'Deliverd'), ('Cancle', 'Cancle')], default='Pending', max_length=200),
        ),
    ]
