# Generated by Django 3.0.5 on 2020-05-30 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_lists', '0007_auto_20200530_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
