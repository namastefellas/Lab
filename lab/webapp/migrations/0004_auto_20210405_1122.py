# Generated by Django 3.1.7 on 2021-04-05 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20210405_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='User Name')),
                ('phone', models.IntegerField(verbose_name='Phone Number')),
                ('adress', models.CharField(max_length=200, verbose_name='Adress')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_o', to='webapp.order', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='o_product', to='webapp.product', verbose_name='Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.ManyToManyField(blank=True, related_name='products', through='webapp.ProductOrder', to='webapp.Order', verbose_name='Order'),
        ),
    ]