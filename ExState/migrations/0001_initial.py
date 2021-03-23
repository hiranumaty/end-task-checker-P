# Generated by Django 3.1.6 on 2021-03-23 05:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MasterData', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExState',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('TargetMonth', models.CharField(max_length=6, verbose_name='対象年月')),
                ('toDoFlg', models.BooleanField(default=False, verbose_name='実行状況')),
                ('depart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MasterData.deptsmaster', verbose_name='部署')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MasterData.tasksmaster', verbose_name='タスク名')),
            ],
            options={
                'db_table': 'ExState',
            },
        ),
    ]
