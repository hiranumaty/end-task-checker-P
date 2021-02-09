# Generated by Django 2.2.5 on 2021-02-09 04:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeptsMaster',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='所属コード')),
                ('deploy_name', models.CharField(max_length=30, verbose_name='部署名')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Depts',
            },
        ),
        migrations.CreateModel(
            name='TasksMaster',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='タスクコード')),
                ('Task_name', models.CharField(max_length=30, verbose_name='タスク名')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Tasks',
            },
        ),
    ]
