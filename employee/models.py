from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _

from employee.managers import EmployeeManager
from core.models import Person

# Create your models here.
class BaseJobModel(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=45)
    description = models.TextField(verbose_name=_("Description"), blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return ('id__iexact', 'name__icontains',)


class Division(BaseJobModel):
    class Meta:
        verbose_name = _("2.6. Division")
        verbose_name_plural = _("2.6. Division")


class JobTitle(BaseJobModel):
    class Meta:
        verbose_name = _("2.3. Job Title")
        verbose_name_plural = _("2.3. Job Title")


class Department(BaseJobModel):
    class Meta:
        verbose_name = _("2.4. Departement")
        verbose_name_plural = _("2.4. Departement")


class JobRole(BaseJobModel):
    class Meta:
        verbose_name = _("2.5. Job Role")
        verbose_name_plural = _("2.5. Job Role")


class Employee(models.Model):
    CONTRACT_TYPE = (
        ('DW', 'Daily Worker'),
        ('Staff', 'Staff'),
        ('Unknown', 'Unknown')
    )
    reg_number = models.CharField(verbose_name=_("NIK"), max_length=9, unique=True)
    person = models.ForeignKey(
        Person, verbose_name=_("Person"), on_delete=models.CASCADE,
        limit_choices_to={'status': 'hired'}
    )
    no_bpjstk = models.CharField(
        verbose_name=_("No BPJS Ketenagakerjaan"), max_length=20, null=True, blank=True
    )
    no_bpjskes = models.CharField(
        verbose_name=_("No BPJS Kesehatan"), max_length=20, null=True, blank=True
    )
    date_of_hired = models.DateField(verbose_name=_("Date of hired"))
    type = models.CharField(
        verbose_name=_("Employment type"), choices=CONTRACT_TYPE, max_length=7, default='Unknown'
    )
    job_title = models.ForeignKey(
        JobTitle, verbose_name=_("Job title"),on_delete=models.PROTECT, null=True, blank=True
    )
    department = models.ForeignKey(
        Department, verbose_name=_("Department"), on_delete=models.PROTECT, null=True, blank=True
    )
    job_role = models.ForeignKey(
        JobRole, verbose_name=_("Job Role"), on_delete=models.PROTECT, null=True, blank=True
    )
    division = models.ForeignKey(
        Division, verbose_name=_("Division"), on_delete=models.PROTECT, null=True, blank=True
    )
    objects = EmployeeManager()

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("2.1. Employee List")

    def __str__(self):
        return '{} - {}'.format(self.reg_number, self.person.name)

    @staticmethod
    def autocomplete_search_fields():
        return ('id__iexact', 'person__name__icontains',)

    def contract_count(self):
        return self.contract_set.all().count()
    contract_count.short_description = _("Contract Count")

    def last_contract_end_date(self):
        if self.contract_set.exists():
            contract = self.contract_set.all().order_by('-end_date')[0]
            return contract.end_date
        return "-"
    last_contract_end_date.short_description = _("End Date")


class Contract(models.Model): # TODO: add monitoring (database view ) for this model
    CONTRACT_TYPE = (
        ('DW', 'Daily Worker'),
        ('Staff', 'Staff')
    )
    employee = models.ForeignKey(Employee, verbose_name=_("Employee"), on_delete=models.CASCADE)
    no_contract = models.CharField(
        verbose_name=_("Contract number"), max_length=20, null=True, blank=True
    )
    start_date = models.DateField(verbose_name=_("Start date"))
    end_date = models.DateField(verbose_name=_("End date"), null=True, blank=True)
    created_date = models.DateField(verbose_name=_("Date created"), default=date.today)
    sign_date = models.DateField(verbose_name=_("Sign date"), null=True, blank=True)
    type = models.CharField(verbose_name=_("Employment type"), choices=CONTRACT_TYPE, max_length=5)

    class Meta:
        verbose_name = _("Contract")
        verbose_name_plural = _("2.2. Contract List")

    def __str__(self):
        return '{} - {}'.format(self.employee.person.name, self.no_contract)

    @staticmethod
    def autocomplete_search_fields():
        return ('id__iexact', 'employee__person__name__icontains')
