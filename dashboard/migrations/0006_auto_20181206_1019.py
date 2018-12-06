# Generated by Django 2.1.3 on 2018-12-06 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0005_auto_20181204_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz_enrollments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=30)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='enrollments',
            name='student_name',
            field=models.CharField(max_length=60),
        ),
    ]