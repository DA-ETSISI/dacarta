# Generated by Django 4.1.3 on 2025-02-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carta', '0008_remove_carta_etiqueta_carta_subdelegacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='carta',
            name='estado',
            field=models.CharField(choices=[('NoLeido', 'No leido'), ('Leido', 'Leido'), ('NoTramitable', 'No tramitable')], default='NoLeido', max_length=100),
        ),
    ]
