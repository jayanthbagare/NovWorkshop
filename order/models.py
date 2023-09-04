from django.db import models

# Create your models here.
order_status = [("OR","Ordered"),("PI","Picked"),("PA","Packed"),("SP","Shipped")]

class material(models.Model):
	id = models.AutoField(primary_key=True,verbose_name="Id")
	code = models.CharField(max_length=3,blank=False,verbose_name="Material 3 Letter Code")
	long_text = models.TextField(verbose_name="Material Description")
	price = models.DecimalField(max_digits=5,decimal_places=2,verbose_name="Material Price")
	stock = models.SmallIntegerField(verbose_name="Current Stock")
	packing_material = models.SmallIntegerField(blank=True,null=True,verbose_name="Packing Material Reqd Qty")
	is_packing = models.BooleanField(verbose_name="Is this a packing material")

	def __str__(self):
		return self.long_text


class Order(models.Model):
	id = models.AutoField(primary_key=True,verbose_name="Order Id")
	product = models.OneToOneField(material,on_delete=models.CASCADE,related_name="material_of")
	quantity = models.SmallIntegerField(verbose_name="Quantity")
	unit_price = models.DecimalField(max_digits=5,decimal_places=2,verbose_name="Unit Price")
	packing_price = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True,verbose_name="Packing Price")
	shipping_price = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True,verbose_name="Shipping Price")
	shipping_reference = models.CharField(max_length=30,blank=True,null=True,verbose_name="Shipping Reference from ShipRocket")
	deliver_date = models.DateField(blank=True,null=True,verbose_name="Delivery Date")
	stage = models.CharField(max_length=2,choices=order_status)


