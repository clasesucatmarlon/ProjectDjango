# Generated by Django 3.2.9 on 2021-11-09 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManageUserModels',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=200)),
                ('compañy', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
