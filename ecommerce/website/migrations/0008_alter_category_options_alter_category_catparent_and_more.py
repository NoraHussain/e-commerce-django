# Generated by Django 4.0.2 on 2022-02-08 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_category_catparent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='CATParent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.category'),
        ),
        migrations.CreateModel(
            name='Product_Alternative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PALAlternatives', models.ManyToManyField(related_name='alternative_products', to='website.Product')),
                ('PALProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='website.product')),
            ],
        ),
    ]