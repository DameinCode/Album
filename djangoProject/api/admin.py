from django.contrib import admin

# Register your models here.

from api.models import Company, Vacancy


@admin.register(Vacancy)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'description', 'company',)
    # search_fields = ('name', 'price',)
    # list_filter = ('category',)


admin.site.register(Company)