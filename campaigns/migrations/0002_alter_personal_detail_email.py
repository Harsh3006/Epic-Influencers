# Generated by Django 3.2.7 on 2021-10-16 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_detail',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email')),
        ),
    ]