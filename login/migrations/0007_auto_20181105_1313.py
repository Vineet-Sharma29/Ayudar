# Generated by Django 2.1.3 on 2018-11-05 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0006_auto_20181105_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=15, unique=True)),
                ('course_name', models.CharField(max_length=30, unique=True)),
                ('credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='course_taken_by',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('semester', models.CharField(max_length=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.course_details')),
            ],
        ),
        migrations.CreateModel(
            name='professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100, unique=True)),
                ('fullname', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_description', models.CharField(max_length=150)),
                ('professor_photo', models.ImageField(upload_to='')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.professor')),
            ],
        ),
        migrations.AddField(
            model_name='course_taken_by',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.professor'),
        ),
    ]