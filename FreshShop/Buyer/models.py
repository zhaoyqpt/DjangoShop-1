from django.db import models
from django.db.models import Manager

class Buyer(models.Model):
    username = models.CharField(max_length=32,verbose_name="用户名")
    password = models.CharField(max_length=32,verbose_name="密码")
    email = models.EmailField(verbose_name="用户邮箱")
    phone = models.CharField(max_length=32,verbose_name="联系电话",blank=True,null=True)
    connect_address = models.TextField(verbose_name = "联系地址",blank=True,null=True)

class Address(models.Model):
    """
    收货地址
    """
    address = models.TextField(verbose_name = "收货地址")
    recver =  models.CharField(max_length=32,verbose_name="接收人")
    recv_phone = models.CharField(max_length=32,verbose_name="收件人电话")
    post_number = models.CharField(max_length=32,verbose_name="邮编")
    buyer_id = models.ForeignKey(to=Buyer,on_delete = models.CASCADE,verbose_name = "用户id")

class Order(models.Model):
    """
    订单表
    未支付   1
	待发货   2
	已发货   3
	已收货   4
	（已退货）  0
    """
    order_id = models.CharField(max_length = 32,verbose_name = "id订单编号")
    goods_count = models.IntegerField(verbose_name = "商品数量")
    order_user = models.ForeignKey(to = Buyer,on_delete = models.CASCADE,verbose_name = "订单用户")
    order_address = models.ForeignKey(to = Address,on_delete = models.CASCADE,verbose_name = "订单地址",blank=True,null=True)
    order_price = models.FloatField(verbose_name = "订单总价")
    order_status = models.IntegerField(default=1,verbose_name="订单状态")


class OrderDetail(models.Model):
    """
    订单详情表
    """
    order_id = models.ForeignKey(to = Order,on_delete = models.CASCADE,verbose_name="订单编号(多对一)")
    goods_id = models.IntegerField(verbose_name = "商品id")
    goods_name = models.CharField(max_length = 32,verbose_name = "商品名称")
    goods_price = models.FloatField(verbose_name = "商品价格")
    goods_number = models.IntegerField(verbose_name = "商品购买数量")
    goods_total = models.FloatField(verbose_name = "商品总价")
    goods_store = models.IntegerField(verbose_name = "商店id")
    goods_image = models.ImageField(verbose_name = "商品图片")

class Cart(models.Model):
    goods_name=models.CharField(max_length=32,verbose_name='商品名称')
    goods_price=models.FloatField(verbose_name='商品价格')
    goods_total=models.FloatField(verbose_name='商品小计')
    goods_number=models.IntegerField(verbose_name='商品数量')
    goods_picture=models.ImageField(upload_to='buyer/images',verbose_name='商品图片')
    goods_id=models.IntegerField(verbose_name='商品id')
    goods_store=models.IntegerField(verbose_name='商品店铺')
    user_id=models.IntegerField(verbose_name='用户id')

import datetime

class GoodsTypeManage(Manager):
    def addType(self,name,picture='buyer/images/page_1_10.jpg'):
        goods_type=GoodsType()
        goods_type.name=name
        now=datetime.datetime.now().strftime('%Y-%m-%d')
        goods_type.description='%s_%s'%(now,name)
        goods_type.picture=picture
        goods_type.save()
        return goods_type
class GoodsType(models.Model):
    name=models.CharField(max_length=32,verbose_name='商品类型名称')
    description=models.TextField(max_length=32,verbose_name='商品类型描述')
    picture=models.ImageField(upload_to='buyer/images')
    objects=GoodsTypeManage()

# Create your models here.
