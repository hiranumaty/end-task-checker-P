from django.contrib.auth.models import(
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
# Create your models here.


class UserManager(BaseUserManager):
    """Managerクラス"""
    use_in_migrations = True

    def _create_user(self, user_id, password, **extra_fields):
        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, user_id, password, **extra_fields):
        extra_fields.setdefault('is_activate', True)
        extra_fields.setdefault('is_adminAccess', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(user_id, password, **extra_fields)

    def create_superuser(self, user_id, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_activate', True)
        extra_fields.setdefault('is_adminAccess',True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(user_id, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """拡張ユーザーモデル"""
    class Meta:
        db_table = 'users'
        verbose_name = 'ログインユーザー'
        verbose_name_plural = 'ログインユーザー'
    user_id = models.CharField(
        verbose_name='ユーザーID',
        primary_key=True,
        editable=True,
        unique=True,
        max_length=5)
    is_activate = models.BooleanField(verbose_name='ログイン権限', default=False)
    #管理者ページへのアクセスを許すか
    is_adminAccess = models.BooleanField(verbose_name='管理ページ権限', default=False)
    #このシステムを使うのを許すか
    is_staff = models.BooleanField(verbose_name='システム使用権限', default=False)
    is_superuser = models.BooleanField(verbose_name='管理者特権', default=False)

    email = models.EmailField(verbose_name='メールアドレス', blank=False, null=True,)
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['is_activate','is_adminAccess','is_staff']
    objects = UserManager()

    def __str__(self):
        """表示の変更"""
        return self.user_id
