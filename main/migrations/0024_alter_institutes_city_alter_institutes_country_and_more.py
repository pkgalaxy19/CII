# Generated by Django 4.0 on 2023-01-26 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_openings_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutes',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='institutes',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='institutes',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
