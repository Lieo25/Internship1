# Generated by Django 4.2.13 on 2024-06-13 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Multilangapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_No', models.BigIntegerField(max_length=100)),
                ('train_name', models.CharField(max_length=100)),
                ('train_source', models.CharField(max_length=100)),
                ('train_destn', models.CharField(max_length=100)),
                ('arrivaldatatime', models.DateTimeField()),
                ('platformNo', models.IntegerField(max_length=100)),
            ],
        ),
    ]
