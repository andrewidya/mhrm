# Generated by Django 2.1.4 on 2019-02-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_auto_20190227_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='reg_number',
            field=models.CharField(max_length=9, verbose_name='NIK'),
        ),
    ]