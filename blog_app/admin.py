from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from blog_app.models import Category, Post, Tag


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget,
    )

    class Meta:
        model = Post
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_display = (
        'id',
        'title',
        'slug',
    )
    list_display_links = (
        'id',
        'title',
    )
    prepopulated_fields = {
        'slug': ('title',),
    }


class TagAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_display = (
        'id',
        'title',
        'slug',
    )
    list_display_links = (
        'id',
        'title',
    )
    prepopulated_fields = {
        'slug': ('title',),
    }


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    save_on_top = True
    save_as = True
    list_display = (
        'id',
        'title',
        'slug',
        'category',
        'author',
        'views',
        'created_at',
        'get_photo',
    )
    list_display_links = (
        'id',
        'title',
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'category',
        'tags',
    )
    readonly_fields = (
        'views',
        'created_at',
        'get_photo',
    )
    fields = (
        'title',
        'slug',
        'author',
        'category',
        'tags',
        'content',
        'photo',
        'get_photo',
        'views',
        'created_at',
    )
    prepopulated_fields = {
        'slug': ('title',),
    }

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50"')
        return 'No photo'

    get_photo.short_description = 'photo'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
