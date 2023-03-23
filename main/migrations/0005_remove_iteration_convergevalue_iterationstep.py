# Generated by Django 4.1.7 on 2023-03-22 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_iteration_convergevalue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iteration',
            name='convergeValue',
        ),
        migrations.CreateModel(
            name='IterationStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=10000)),
                ('step', models.IntegerField(default=0)),
                ('iterationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.iteration')),
            ],
        ),
    ]
