# Generated by Django 4.0.4 on 2022-05-25 16:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_comentario_post_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]