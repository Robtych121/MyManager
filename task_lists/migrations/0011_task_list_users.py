# Generated by Django 3.0.7 on 2020-06-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_lists', '0010_task_list_sort_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_List_Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('perm_view', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=25)),
                ('perm_add', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=25)),
                ('perm_edit', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=25)),
                ('perm_delete', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=25)),
            ],
        ),
    ]
