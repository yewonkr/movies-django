from django.contrib import admin

from .models import Actress, Movies, ItemCode, Category

# Register your models here.

class ActressAdmin(admin.ModelAdmin):
    list_display = ("__str__", "birth", "height", "debut")
    # filter_horizontal = ("movies",)
    list_filter = [
        ("name", admin.EmptyFieldListFilter),
    ]
    search_fields = ("name", "enName",)

class MoviesAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    search_fields = ("id", "title",)
    filter_horizontal = ("actress",)
    
class ItemCodeAdmin(admin.ModelAdmin):
    list_display = ("__str__", )
    # filter_horizontal = ("movies",)

    #  (admin.E020) The value of 'filter_horizontal[0]' must be a many-to-many field.


admin.site.register(Category) 
admin.site.register(Actress, ActressAdmin)
admin.site.register(Movies, MoviesAdmin)
admin.site.register(ItemCode, ItemCodeAdmin)

