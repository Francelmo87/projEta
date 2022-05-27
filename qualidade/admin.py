from django.contrib import admin
from .models import Stage, Parameter, Eta1


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = (
        'decanted',
        'treated',
    )


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(Eta1)
class Eta1Admin(admin.ModelAdmin):
    list_display = (
        'date',
        'hour',
        'parameter',
    )
    search_fields = ('date',)
    list_filter = ('date',)
