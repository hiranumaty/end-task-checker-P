# Generated by Django 3.2.2 on 2021-05-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_adminAccess',
            field=models.BooleanField(default=False, verbose_name='管理ページ権限'),
        ),
    ]
