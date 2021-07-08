# Generated by Django 3.2.5 on 2021-07-08 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_record_unique_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL),
        ),
    ]