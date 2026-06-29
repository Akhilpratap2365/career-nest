from django.contrib import admin
from.models import *
# Register your models here.
class tblcontactAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","message")
admin.site.register(tblcontact,tblcontactAdmin)

class tblgalleryAdmin(admin.ModelAdmin):
    list_display=("title","picture")
admin.site.register(tblgallery,tblgalleryAdmin)

class tblteamAdmin(admin.ModelAdmin):
    list_display=("name","picture","post","experience")
admin.site.register(tblteam,tblteamAdmin)

class tblcityAdmin(admin.ModelAdmin):
    list_display=("id","name","picture")
admin.site.register(tblcity,tblcityAdmin)

class tblcategoryAdmin(admin.ModelAdmin):
    list_display=("id","name","picture")
admin.site.register(tblcategory,tblcategoryAdmin)

class tblcompanyAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","department","city","owner","logo","type","detail","url","startdate","active","isimp","ispaid")
admin.site.register(tblcompany,tblcompanyAdmin)

class tblseekerAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","password","qualification","exp","company","resume","salary","esalary","picture","regdate")
admin.site.register(tblseeker,tblseekerAdmin)

class tbljobAdmin(admin.ModelAdmin):
    list_display=("company","title","description","jobtype","city","category","minsalary","maxsalary","prefgender","exp","skills","vacany","lastdate","startdate","active")
admin.site.register(tbljob,tbljobAdmin)

class tblapplyAdmin(admin.ModelAdmin):
    list_display=("job","seeker","date","cvselected","interview","hired","rejected")
admin.site.register(tblapply,tblapplyAdmin)

