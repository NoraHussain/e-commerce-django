# Generated by Django 4.0.2 on 2022-02-08 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_pdname_product_prdname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDCost',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='product cost'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCreatedAt',
            field=models.DateTimeField(verbose_name='created at '),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDDesc',
            field=models.TextField(verbose_name='product description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDName',
            field=models.CharField(max_length=100, verbose_name='product name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDPrice',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='product price'),
        ),
    ]