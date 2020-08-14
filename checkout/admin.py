from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)


    fields = ('order_number', 'date', 'name', 'surname',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county',
              'total',)

    list_display = ('order_number', 'date', 'name', 'surname',
                    'total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
