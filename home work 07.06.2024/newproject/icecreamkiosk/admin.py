from django.contrib import admin
from .models import Parent, Child, IceCream, IceCreamKiosk, IceCreamKioskIceCream, ParentChild

class ParentChildInline(admin.TabularInline):
    model = ParentChild
    extra = 1  

class ParentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email', 'get_children')
    search_fields = ('first_name', 'last_name', 'email')
    inlines = [ParentChildInline]  

    def get_children(self, obj):
        return ", ".join([child.name for child in obj.children.all()])
    get_children.short_description = 'Дети'

class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'favorite_toy', 'get_parents')
    search_fields = ('name', 'favorite_toy')
    inlines = [ParentChildInline] 

    def get_parents(self, obj):
        return ", ".join([parent.first_name + " " + parent.last_name for parent in obj.parents.all()])
    get_parents.short_description = 'Родители'

class IceCreamAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'price', 'quantity')
    search_fields = ('flavor',)

class IceCreamKioskAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

class IceCreamKioskIceCreamAdmin(admin.ModelAdmin):
    list_display = ('kiosk', 'ice_cream', 'quantity')
    search_fields = ('kiosk__name', 'ice_cream__flavor')

admin.site.register(Parent, ParentAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(IceCreamKiosk, IceCreamKioskAdmin)
admin.site.register(IceCreamKioskIceCream, IceCreamKioskIceCreamAdmin)
