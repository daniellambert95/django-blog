from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog, stock_app 
# Register your models here.


#this block is for posts
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = 'body'
    pass
admin.site.register(Blog, BlogAdmin)

#this block is for Admin
class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Area'
    login_template = 'blog/admin/login.html'

blog_site = BlogAdminArea(name='BlogAdmin')

#this block is for posts
class  SummerAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(models.Post, SummerAdmin)
blog_site.register(models.Post, SummerAdmin)

#this block is for stock_app
admin.site.register(stock_app)