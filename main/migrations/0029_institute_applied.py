# Generated by Django 3.2.12 on 2023-02-08 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0028_consultancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='institute_applied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('institute_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('opening_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.openings')),
            ],
        ),
    ]
