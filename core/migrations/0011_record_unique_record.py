# Generated by Django 3.2.5 on 2021-07-07 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_habit_created_date'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='record',
            constraint=models.UniqueConstraint(fields=('habit_name', 'date'), name='unique_record'),
        ),
    ]
