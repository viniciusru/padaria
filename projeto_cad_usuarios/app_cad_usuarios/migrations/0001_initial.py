# Generated by Django 4.2.7 on 2023-11-20 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id_usuarios', models.AutoField(primary_key=True, serialize=False)),
                ('Nome', models.TextField(max_length=100)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
