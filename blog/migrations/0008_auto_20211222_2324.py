# Generated by Django 3.1 on 2021-12-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20211222_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.TextField(max_length=50),
        ),
    ]
