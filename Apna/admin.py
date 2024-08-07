from django.contrib import admin
from .models import Product,Cart,Payment,OrderPlaced,Address
@admin.register(Product)
# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','item_name','item_price','item_category','item_brand','item_image']
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']
@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity','ordered_date','status','payment']
@admin.register(Address)
class AddressModelAdmin(admin.ModelAdmin):
    list_display=['id','address','adress_2','city','zip','state','user']