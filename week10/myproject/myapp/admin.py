from django.contrib import admin

from myapp.models import Profile, Item, Order_Item

class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)

class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)

class Order_ItemAdmin(admin.ModelAdmin):
    list_display_links = ('profile',)
    list_display = ('profile','item','quantity')
    list_editable = ('item','quantity')
admin.site.register(Order_Item, Order_ItemAdmin)