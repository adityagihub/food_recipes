from django.contrib import admin
from items.models import recipe2


class rever(admin.ModelAdmin):
    listdiplay2 = ('rname','rdes','rpirce','img1')

# Register your models here.


admin.site.register(recipe2,rever)
