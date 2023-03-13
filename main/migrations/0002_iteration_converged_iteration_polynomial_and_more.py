# Generated by Django 4.1.7 on 2023-03-13 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iteration',
            name='converged',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='iteration',
            name='polynomial',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='iteration',
            name='threshold',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='iteration',
            name='currentIteration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='iteration',
            name='maxIteration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='iteration',
            name='startValue',
            field=models.FloatField(default=0.0),
        ),
    ]
