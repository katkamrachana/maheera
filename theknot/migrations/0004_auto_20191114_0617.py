# Generated by Django 2.2.7 on 2019-11-14 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theknot', '0003_auto_20191114_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='additional_guests',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
