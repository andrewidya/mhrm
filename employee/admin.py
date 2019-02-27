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
            'fields': (
                ('reg_number', 'person'), ('no_bpjstk', 'no_bpjskes'), ('date_of_hired', 'type')
            ),
        }),
    )
    list_display = (
        'reg_number', 'person', 'no_bpjstk', 'no_bpjskes', 'contract_count', 'type',
        'last_contract_end_date'
    )
    list_filter = ('type', )
    readonly_fields = ('type', )
    list_per_page = 20
    search_fields = ('person__name', 'reg_number')
    raw_id_fields = ('person',)
    autocomplete_lookup_fields = {
        'fk': ['person'],
    }
    inlines = [ContractInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        obj = form.instance
        if obj.contract_set.exists():
            contract = obj.contract_set.all().order_by('-end_date')[0]
            obj.type = contract.type
            obj.save()


@admin.register(Contract)
class ContractAdmin(ImportExportMixin, admin.ModelAdmin):
    fieldsets = (
        ('2.1. Employee information', {
            'fields': ('employee',),
        }),
        ('2.2. Contract information', {
            'fields': (
                ('no_contract', 'type'), ('start_date', 'end_date'), ('created_date', 'sign_date', )
            ),
        }),
    )
    readonly_fields = ('created_date',)
    raw_id_fields = ('employee',)
    autocomplete_lookup_fields = {
        'fk': ['employee'],
    }
