# Generated by Django 2.0.3 on 2018-05-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20180521_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score_date',
            field=models.DateField(),
        ),
    ]
