# Generated by Django 3.2.7 on 2022-01-17 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Furigana', models.CharField(max_length=100)),
                ('Tell', models.IntegerField(blank=True, null=True)),
                ('Mail', models.EmailField(max_length=100)),
                ('Birthday', models.CharField(max_length=20)),
                ('Adress', models.CharField(max_length=100)),
            ],
        ),
    ]
