from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import Person

# Create your models here.
class Employee(models.Model):
    CONTRACT_TYPE = (
        ('DW', 'Daily Worker'),
        ('Staff', 'Staff'),
        ('Unknown', 'Unknown')
    )
    reg_number = models.CharField(verbose_name=_("NIK"), max_length=9)
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


# TODO: add monitoring (database view ) for this model
class Contract(models.Model):
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
