# Generated by Django 2.2.5 on 2019-12-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20191207_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]