# Generated by Django 3.0.3 on 2020-05-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200507_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='ch',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ManyToManyField(related_name='choice', to='app.Questions'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice',
            field=models.CharField(max_length=50),
        ),
    ]
