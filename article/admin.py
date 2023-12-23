from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'modified_date', 'created_date')
    # fields = ('title', 'content', 'modified_date', 'created_date', 'image')
    fields = ('title', 'content', 'slug', 'modified_date', 'created_date', 'image')
    readonly_fields = ('created_date', 'modified_date')
    list_filter = ('created_date', )
    date_hierarchy = 'created_date'
    list_display_links = ('id', 'title')
    # list_editable = ('title', )
    search_fields = ('title',)
    list_per_page = 25
    prepopulated_fields = {"slug": ("title",)}



admin.site.register(Article, ArticleAdmin)