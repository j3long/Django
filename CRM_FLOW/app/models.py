from django.db import models

# Create your models here.

#python的类
class Order(models.Model):
     id=models.AutoField(primary_key=True)
     odert_ype=models.CharField(max_length=32,null=True)
     order_id=models.CharField(max_length=32,null=True)
     name=models.CharField(max_length=50,null=True)
     mobile=models.CharField(max_length=32,null=True)
     address=models.CharField(max_length=200,null=True)
     sku=models.CharField(max_length=32,null=True)
     sku_qty=models.DecimalField(max_digits=8,decimal_places=2)
     sku_price=models.DecimalField(max_digits=8,decimal_places=2)
     subtotal=models.DecimalField(max_digits=8,decimal_places=2)
     #total=models.DecimalField(max_digits=8,decimal_places=2)
     order_stats=models.CharField(max_length=32,null=True)
     delivery_comp=models.CharField(max_length=32,null=True)
     delivery_numb=models.CharField(max_length=32,null=True)
     remark=models.CharField(max_length=200,null=True)
     order_date=models.CharField(max_length=32,null=True)
     delivery_date=models.CharField(max_length=32,null=True)
     touch_date=models.CharField(max_length=32,null=True)
     displace_old=models.CharField(max_length=32,null=True)
     displace_oldnum=models.DecimalField(max_digits=8,decimal_places=2)
     displace_delivery=models.CharField(max_length=32,null=True)
     displace_new=models.CharField(max_length=32,null=True)
     displace_newnum=models.DecimalField(max_digits=8,decimal_places=2)

class Book_single(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pub_date = models.DateField()
    publish = models.CharField(max_length=32)

    def __str__(self):
        return self.title