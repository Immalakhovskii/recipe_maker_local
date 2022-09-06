# Generated by Django 2.2.19 on 2022-09-05 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220905_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='first address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrator'), ('user', 'User')], default='user', max_length=15, verbose_name='role'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber', to=settings.AUTH_USER_MODEL, verbose_name='subscriber'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to=settings.AUTH_USER_MODEL, verbose_name='subscription'),
        ),
    ]