# Generated by Django 4.2.3 on 2023-07-11 20:34

import api.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18, validators=[django.core.validators.MaxValueValidator(116), django.core.validators.MinValueValidator(18)])),
                ('height', models.CharField(default='5\'9"', max_length=10, validators=[api.validators.heightValidator])),
                ('bio', models.TextField(max_length=250)),
                ('pfp', models.ImageField(upload_to='profilePictures')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
