# Generated by Django 2.1.7 on 2019-03-02 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestboy', '0006_auto_20190302_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]