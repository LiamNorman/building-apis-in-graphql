# Generated by Django 2.1.4 on 2019-04-27 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('podcasts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
