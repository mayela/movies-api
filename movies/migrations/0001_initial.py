# Generated by Django 2.2 on 2019-04-24 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80, verbose_name='First name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last name')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('synopsis', models.TextField(verbose_name='Synopsis')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Year')),
                ('artists', models.ManyToManyField(blank=True, null=True, to='movies.Artist')),
            ],
        ),
    ]
