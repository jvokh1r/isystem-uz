# Generated by Django 4.0.6 on 2022-09-28 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=221)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('extra_phone', models.IntegerField()),
            ],
        ),
    ]
