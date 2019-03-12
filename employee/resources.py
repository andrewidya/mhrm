from django.utils.translation import ugettext_lazy as _

from import_export.resources import ModelResource
from import_export.fields import Field

from employee.models import Employee


class EmployeeExportResource(ModelResource):
    reg_number = Field(attribute='reg_number', column_name=_('NIK'))
    person_name = Field(attribute='person__name', column_name=_('Person'))
    bpjs_tk = Field(attribute='no_bpjstk', column_name=_('BPJS TK'))
    bpjs_kes = Field(attribute='no_bpjskes', column_name=_('BPJS KES'))
    date_of_hired = Field(attribute='date_of_hired', column_name=_('Date of hired'))
    is_permanent = Field(attribute='is_permanent', column_name=_('Permanent'))
    contract = Field(attribute='type', column_name=_('Contract type'))
    job_title = Field(attribute='job_title__name', column_name='Job Title')
    department = Field(attribute='department__name', column_name='Department')
    job_role = Field(attribute='job_role__name', column_name='Role')
    division = Field(attribute='division__name', column_name='Division')

    class Meta:
        model = Employee
        fields = (
            'reg_number', 'person_name', 'bpjs_tk', 'bpjs_kes',
            'date_of_hired', 'is_permanent', 'contract', 'job_title',
            'department', 'job_role', 'division'
        )
