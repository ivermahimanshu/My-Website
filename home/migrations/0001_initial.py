# Generated by Django 3.0.5 on 2020-04-25 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('ModelNo', models.CharField(max_length=100)),
                ('HDD', models.IntegerField()),
                ('RAM', models.IntegerField()),
                ('Cache', models.IntegerField()),
                ('Description', models.TextField()),
            ],
        ),
    ]
