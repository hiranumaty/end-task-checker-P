# Generated by Django 3.1.6 on 2021-03-23 05:12

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True, verbose_name='ユーザーID')),
                ('is_activate', models.BooleanField(default=False, verbose_name='部門長権限')),
                ('is_staff', models.BooleanField(default=False, verbose_name='管理者権限')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='管理者特権')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='メールアドレス')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'ログインユーザー',
                'verbose_name_plural': 'ログインユーザー',
                'db_table': 'users',
            },
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
    ]
