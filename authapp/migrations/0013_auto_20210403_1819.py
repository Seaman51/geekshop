# Generated by Django 3.1.6 on 2021-04-03 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_auto_20210403_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
