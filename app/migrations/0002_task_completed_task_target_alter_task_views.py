# Generated by Django 5.0.3 on 2024-03-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='target',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='task',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]