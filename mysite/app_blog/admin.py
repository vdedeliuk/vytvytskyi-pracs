from django.contrib import admin
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}
    fields = (
        ('name', 'slug'),
    )
admin.site.register(Category, CategoryAdmin)

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 1
    fields = ('image', 'title')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'main_page')
    list_filter = ['main_page']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Основна інформація', {
            'fields': (('title', 'slug'), 'description', 'pub_date', 'main_page')
        }),
        ('Текст статті', {
            'classes': ('collapse',),
            'fields': ('text',),
        }),
    )

    inlines = [ArticleImageInline]


admin.site.register(Article, ArticleAdmin)

