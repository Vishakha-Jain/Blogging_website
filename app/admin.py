from django.contrib import admin
from .models import *
# Register your models here.

# for configuration of Category admin
# so basically here admin.ModelAdmin is used as a superclass to the child class CategoryAdmin. 
class CategoryAdmin(admin.ModelAdmin):
    # the below code is used for displaying while listing the data objects
    list_display=('image_tag','title','description','url','add_date')
    # it is defined using tuple.
    search_fields=('title',)


class PostAdmin(admin.ModelAdmin):
    # the below code is used for displaying while listing the data objects
    list_display=('title',)
    # it is defined using tuple.
    search_fields=('title',)
    list_filter=('cat',)
    # the below code is used for showing list on the admin panel
    list_per_page=50

# using the below code we can get admin class with custom CategoryAdmin functionality.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
