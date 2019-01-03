from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Person(models.Model):
    MARITAL = (
        ("S", _("Single")),
        ("M", _("Married")),
    )
    STATUS = (
        ("new", _("On Progress")),
        ("reject", _("Reject")),
        ("hired", _("Hired")),
        ("resign", _("Resign"))
    )
    name = models.CharField(verbose_name=_("Name"), max_length=50)
    birth_date = models.DateField(verbose_name=_("Date of birth"))
    birth_city = models.CharField(verbose_name=_("City of birth"), max_length=50)
    id_card = models.CharField(verbose_name=_("Identity card"), null=True, blank=True, max_length=20)
    phone = models.CharField(verbose_name=_("Phone number"), max_length=15, null=True, blank=True)
    address = models.CharField(verbose_name=_("Address"), max_length=125, null=True, blank=True)
    city = models.CharField(verbose_name=_("City"), max_length=30, null=True, blank=True)
    bank_account = models.CharField(verbose_name=_("Bank account"), max_length=20, null=True, blank=True)
    marital_status = models.CharField(verbose_name=_("Marital status"), choices=MARITAL, max_length=1)
    status = models.CharField(verbose_name=_("Status"), max_length=6, choices=STATUS,
                              help_text=_("Personal status for recruitment information like 'new', 'reject' or 'hired'"))
    tax_account = models.CharField(verbose_name=_("NPWP"), max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = _("Person Information")
        verbose_name_plural = _("1.1. Person Information")

    def __str__(self):
        return self.name

    def npwp(self):
        if self.tax_account:
            if len(self.tax_account) >= 13:
                t = self.tax_account
                return "{}.{}.{}.{}-{}.{}".format(t[:2], t[2:5], t[5:8], t[8], t[9:12], t[12:])
        return self.tax_account
    npwp.short_description = _("NPWP")


class PersonFamily(models.Model):
    RELATION = (
        ('istri', _("Istri")),
        ('suami', _("Suami")),
        ('anak', _("Anak")),
    )

    person = models.ForeignKey(Person, verbose_name=_("Person"), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_("Name"), max_length=40)
    birth_date = models.DateField(verbose_name=_("Date of birth"))
    birth_city = models.CharField(verbose_name=_("City of birth"), max_length=50)
    relationship = models.CharField(verbose_name=_("Relationship"), choices=RELATION, max_length=5)

    class Meta:
        verbose_name = _("Person Family")
        verbose_name_plural = _("1.2. Person Families")

    def __str__(self):
        return self.name


class Education(models.Model):
    GRADE = (
        ('sd', _("SD")),
        ('smp', _("SMP")),
        ('sma', _("SMA")),
        ('diploma', _("Diploma / Sederajat")),
        ('strata_1', _("S1")),
        ('strata_2', _("S2"))
    )

    person = models.ForeignKey(Person, verbose_name=_("Person"), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_("Name"), max_length=40)
    grade = models.CharField(verbose_name=_("Grade"), choices=GRADE, max_length=8)
    start_date = models.DateField(verbose_name=_("Date start"), null=True, blank=True)
    end_date = models.DateField(verbose_name=_("Date finish"), null=True, blank=True)
    location = models.CharField(verbose_name=_("City / Locatoin"), max_length=40, null=True, blank=True)

    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("1.3. Education")

    def __str__(self):
        return self.name
