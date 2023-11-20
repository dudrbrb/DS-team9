from django.contrib import admin
from .models import Member, Major1

class MajorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

# /admin 에서 관리할 수 있는 데이터베이스
admin.site.register(Member)
admin.site.register(Major1, MajorAdmin)