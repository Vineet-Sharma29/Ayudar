# Generated by Django 2.1.2 on 2018-12-04 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0004_auto_20181116_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizresult',
            name='classaverage',
        ),
        migrations.AddField(
            model_name='quiz',
            name='classaverage',
            field=models.FloatField(blank=True, null=True),
        ),
    ]