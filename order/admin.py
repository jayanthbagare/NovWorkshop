from django.contrib import admin
from order.models import material,Order
from django.contrib import messages

@admin.action(description="Pick the Order")
def pick_order(modeladmin,request,queryset):
	for obj in queryset:
		if(obj.product.stock > obj.quantity and obj.stage == "OR"):
			new_stock = obj.product.stock - obj.quantity
			obj.product.stock = new_stock
			obj.stage = "PI"
			obj.product.save()
			obj.save()
		elif(obj.stage== "PI"):
			 messages.add_message(request, messages.INFO, 'Order already Picked')
		else:
			messages.add_message(request,messages.ERROR,'Something went wrong')

@admin.action(description="Pack the Order")
def pack_order(modeladmin,request,queryset):
	for obj in queryset:
		if(obj.stage == "PI"):
			packing_material = material.objects.filter(is_packing = True)
			for pack_obj in packing_material:
				packing_price = obj.product.packing_material * pack_obj.price
				obj.packing_price = packing_price
			obj.stage = "PA"
			obj.save()
			messages.add_message(request,messages.INFO,f'Order Packed with price {packing_price}')
		else:
			messages.add_message(request,messages.ERROR,'Order Should be Picked before Packing')




# Register your models here.
class MaterialAdmin(admin.ModelAdmin):
	search_fields = ['code','long_text']
	list_display = ('code','long_text','price','stock','is_packing')

class OrderAdmin(admin.ModelAdmin):
	autocomplete_fields = ['product']
	list_display = ('id','deliver_date','stage')
	actions=[pick_order,pack_order]

admin.site.register(material,MaterialAdmin)
admin.site.register(Order,OrderAdmin)