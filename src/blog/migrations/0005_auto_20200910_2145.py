# Generated by Django 3.1.1 on 2020-09-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200910_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.TextField(max_length=120),
        ),
    ]
