# Generated by Django 4.0.2 on 2022-02-08 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_category_catdesc_alter_category_catimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BRAName', models.CharField(max_length=40)),
                ('BRADesc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VARName', models.CharField(max_length=40)),
                ('VARDesc', models.TextField()),
            ],
        ),
    ]
