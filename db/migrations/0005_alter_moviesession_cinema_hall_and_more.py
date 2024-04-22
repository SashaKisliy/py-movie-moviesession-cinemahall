# Generated by Django 4.0.2 on 2024-04-22 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_alter_moviesession_show_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesession',
            name='cinema_hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='halls', to='db.cinemahall'),
        ),
        migrations.AlterField(
            model_name='moviesession',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='db.movie'),
        ),
    ]
