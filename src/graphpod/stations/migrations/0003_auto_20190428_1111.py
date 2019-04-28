# Generated by Django 2.1.4 on 2019-04-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='station',
            name='followers',
            field=models.IntegerField(null=True),
        ),
    ]