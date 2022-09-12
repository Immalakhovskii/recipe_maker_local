# Generated by Django 2.2.19 on 2022-09-10 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20220911_0111'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='favorite',
            name='user can favorite recipe just once',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='favorite_recipe',
            new_name='recipe',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='fan',
            new_name='user',
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='user can favorite recipe just once'),
        ),
    ]