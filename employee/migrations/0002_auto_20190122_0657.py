# Generated by Django 2.1.4 on 2019-01-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='no_bpjskes',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='No BPJS Kesehatan'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='no_bpjstk',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='No BPJS Ketenagakerjaan'),
        ),
    ]
