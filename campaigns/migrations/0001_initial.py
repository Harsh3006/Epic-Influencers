# Generated by Django 3.2.7 on 2021-10-15 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default=None, max_length=20, null=True)),
                ('lname', models.CharField(default=None, max_length=30, null=True)),
                ('gender', models.CharField(default=None, max_length=1, null=True)),
                ('language', models.CharField(default=None, max_length=20, null=True)),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, null=True, region=None, unique=True)),
                ('address', models.TextField(default=None, null=True)),
                ('address2', models.TextField(blank=True, default=None, null=True)),
                ('postalCode', models.CharField(default=None, max_length=6, null=True)),
                ('city', models.CharField(default=None, max_length=100, null=True)),
                ('state', models.CharField(default=None, max_length=50, null=True)),
                ('department', models.CharField(default=None, max_length=50, null=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]