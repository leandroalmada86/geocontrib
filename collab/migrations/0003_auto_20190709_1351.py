# Generated by Django 2.2 on 2019-07-09 13:51

import collab.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0002_auto_20190705_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customfield',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='featuretype',
            name='geom_type',
            field=models.CharField(choices=[('linestring', 'Ligne brisée'), ('point', 'Point'), ('polygon', 'Polygone')], default='boolean', max_length=50, verbose_name='Type de champs géometrique'),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(default='default.png', upload_to=collab.models.Project.thumbnail_dir, verbose_name='Illustration'),
        ),
        migrations.DeleteModel(
            name='CustomFieldValue',
        ),
    ]
