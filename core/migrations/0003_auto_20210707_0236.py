# Generated by Django 3.2.5 on 2021-07-07 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_habit_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='date',
        ),
        migrations.AddField(
            model_name='record',
            name='date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habits', to='core.habit'),
        ),
    ]
