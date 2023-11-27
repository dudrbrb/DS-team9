from django.contrib import admin
from .models import Member, Major1, Major2, Tag

class MajorAdmin1(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    
class MajorAdmin2(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# /admin 에서 관리할 수 있는 데이터베이스
admin.site.register(Member)
admin.site.register(Major1, MajorAdmin1)
admin.site.register(Major2, MajorAdmin2)
admin.site.register(Tag, TagAdmin)