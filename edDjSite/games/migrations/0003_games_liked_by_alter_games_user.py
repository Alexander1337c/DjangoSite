# Generated by Django 5.0.3 on 2024-03-15 07:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_games_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_games', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='games',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]
