from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import Person

# Create your models here.
class Employee(models.Model):
    reg_number = models.CharField(verbose_name=_("NIK"), max_length=9)
    person = models.ForeignKey(Person, verbose_name=_("Person"),
                               on_delete=models.CASCADE, limit_choices_to={'status': 'hired'})
    no_bpjstk = models.CharField(verbose_name=_("No BPJS Ketenagakerjaan"), max_length=20,
                                 null=True, blank=True)
    no_bpjskes = models.CharField(verbose_name=_("No BPJS Kesehatan"), max_length=20,
                                  null=True, blank=True)

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("2.1. Employee List")

    def __str__(self):
        return '{} - {}'.format(self.reg_number, self.person.name)

    @staticmethod
    def autocomplete_search_fields():
        return ('id__iexact', 'person__name__icontains',)


class Contract(models.Model):
    CONTRACT_TYPE = (
        ('DW', 'Daily Worker'),
        ('Staff', 'Staff')
    )
    employee = models.ForeignKey(Employee, verbose_name=_("Employee"), on_delete=models.CASCADE)
    no_contract = models.CharField(verbose_name=_("Contract number"), max_length=20, null=True, blank=True)
    start_date = models.DateField(verbose_name=_("Start date"))
    end_date = models.DateField(verbose_name=_("End date"))
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