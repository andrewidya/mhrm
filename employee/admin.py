from django.contrib import admin

from import_export.admin import ImportExportMixin

from employee.models import Employee, Contract

# Register your models here.
class ContractInline(admin.TabularInline):
    model = Contract
    exclude = ('created_date',)
    extra = 0


@admin.register(Employee)
class EmployeeAdmin(ImportExportMixin, admin.ModelAdmin):
    fieldsets = (
        ('2.1. Employee Information', {
            'fields': (('reg_number', 'person'), ('no_bpjstk', 'no_bpjskes')),
        }),
    )
    list_display = ('reg_number', 'person', 'no_bpjstk', 'no_bpjskes')

    raw_id_fields = ('person',)
    autocomplete_lookup_fields = {
        'fk': ['person'],
    }
    inlines = [ContractInline]


@admin.register(Contract)
class ContractAdmin(ImportExportMixin, admin.ModelAdmin):
    fieldsets = (
        ('2.1. Employee information', {
            'fields': ('employee',),
        }),
        ('2.2. Contract information', {
            'fields': (('no_contract', 'type'), ('start_date', 'end_date'), ('created_date', 'sign_date', )),
        }),
    )

    raw_id_fields = ('employee',)
    autocomplete_lookup_fields = {
        'fk': ['employee'],
    }
