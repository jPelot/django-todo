# Generated by Django 5.0 on 2023-12-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_item_user_alter_item_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='due',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]