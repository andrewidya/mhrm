# Generated by Django 2.1.4 on 2019-02-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20190227_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End date'),
        ),
    ]
