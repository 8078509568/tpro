# Generated by Django 4.2.2 on 2023-10-30 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-04-16'),
            preserve_default=False,
        ),
    ]
