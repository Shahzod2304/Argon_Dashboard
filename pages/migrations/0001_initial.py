# Generated by Django 5.0.2 on 2024-02-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_user', models.IntegerField()),
                ('Company_name', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('tulov', models.FloatField()),
                ('foyda', models.FloatField()),
                ('chiqim', models.FloatField()),
                ('product0', models.CharField(max_length=100)),
                ('firma', models.CharField(max_length=100)),
                ('foiz', models.FloatField()),
            ],
        ),
    ]