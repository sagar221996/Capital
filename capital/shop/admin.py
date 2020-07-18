from django.contrib import admin
from .models import Shirt,Pant



# Register your models here.

class ShirtAdmin(admin.ModelAdmin):
    list_display = ['Name','Contact','Status']
    list_filter = ['Status']
    search_fields=['Name']
    actions=('Done','Delivered','Inprogress')

    def Done(self,request,queryset):
        queryset.update(Status='Done')
        self.message_user(request,'status of {} have been changed to Done',format(count))
    
    def Delivered(self,request,queryset):
        queryset.update(Status='Delivered')
    
    
    def Inprogress(self,request,queryset):
        queryset.update(Status='Inprogress')

admin.site.register(Shirt,ShirtAdmin),
admin.site.register(Pant,ShirtAdmin)

