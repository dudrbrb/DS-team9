from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Major1, Major2, Tag


class CustomUserAdmin(UserAdmin):
    model = User
    # 유저 목록
    list_display =  ["name", "username"]

    # 유저 정보 관리 페이지 정보 입력창 추가
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':  ("name", "nickname", "birth", "tel", "studentID",  "major1","major2", "tag", "prof_image", "back_image", "open_profile", 'friends', 'my_like', 'you_liked')}),
        )

class MajorAdmin1(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    
class MajorAdmin2(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    

# /admin 에서 관리할 수 있는 데이터베이스
admin.site.register(Post)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Major1, MajorAdmin1)
admin.site.register(Major2, MajorAdmin2)
admin.site.register(Tag, TagAdmin)