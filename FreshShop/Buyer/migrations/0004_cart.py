# Generated by Django 2.2.1 on 2019-07-30 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0003_order_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=32, verbose_name='商品名称')),
                ('goods_price', models.FloatField(verbose_name='商品价格')),
                ('goods_total', models.FloatField(verbose_name='商品小计')),
                ('goods_number', models.IntegerField(verbose_name='商品数量')),
                ('goods_picture', models.ImageField(upload_to='buyer/images', verbose_name='商品图片')),
                ('goods_id', models.IntegerField(verbose_name='商品id')),
                ('goods_store', models.IntegerField(verbose_name='商品店铺')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
            ],
        ),
    ]
