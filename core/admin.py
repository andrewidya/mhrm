from django.contrib import admin

from import_export.admin import ImportExportMixin, ExportActionMixin

from core.models import  Person, PersonFamily, Education

# Register your models here.
class PersonFamilyInline(admin.TabularInline):
    model = PersonFamily
    extra = 0
    classes = ('grp-collapse grp-open',)


class EducationInline(admin.TabularInline):
    model = Education
    extra = 0
    classes = ('grp-collapse grp-open',)


@admin.register(Person)
class PersonAdmin(ImportExportMixin, ExportActionMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'id_card', ('birth_city', 'birth_date')),
        }),
        ('Address Information', {
            'fields': ('address', ('city', 'phone', )),
        }),
        ('Others', {
            'fields': (('tax_account', 'bank_account'),
                       ('marital_status', 'status'))
        })
    )
    list_display = ('id_card', 'name', 'birth_date', 'marital_status',
                    'phone', 'bank_account', 'npwp', 'status')
    list_display_links = ('name', 'id_card')
    search_fields = ('name', 'id_card', 'phone', 'tax_account')
    list_filter = ('status', 'marital_status')
    list_per_page = 15
    inlines = [PersonFamilyInline, EducationInline]
