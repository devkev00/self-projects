# Generated by Django 4.2.13 on 2024-07-09 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_num', models.IntegerField()),
                ('second_num', models.IntegerField()),
                ('operator', models.TextField()),
                ('result', models.IntegerField()),
            ],
        ),
    ]
