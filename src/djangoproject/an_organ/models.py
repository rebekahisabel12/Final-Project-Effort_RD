from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

from chromatographyarch.domain.model import DomainAnalyticalMethod

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Instrument(models.Model):
    SECTION_CHOICES = [
        ('Solid', 'Solid'),
        ('Liquid', 'Liquid'),
        ('Gas', 'Gas'),
    ]
    manufacturer = models.CharField(max_length=100)
    sample_type = models.CharField(max_length=10, choices=SECTION_CHOICES)
    price_per_sample = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.manufacturer} - {self.sample_type}"


class Analytical_Method(models.Model):
    method_name = models.CharField(max_length=100, primary_key=True)
    method_description = models.TextField()
    sample_matrix = models.CharField(max_length=50)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    cost_per_sample = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.method_name}"

    class Meta:
        app_label = 'an_organ'

    @staticmethod
    def update_from_domain(domain_analyticalmethod: DomainAnalyticalMethod):
        try:
            analyticalmethod = Analytical_Method.objects.get(
                method_name=domain_analyticalmethod.method_name)
        except Analytical_Method.DoesNotExist:
            analyticalmethod = Analytical_Method(
                method_name=domain_analyticalmethod.method_name)

        analyticalmethod.method_name = domain_analyticalmethod.method_name
        analyticalmethod.method_description = domain_analyticalmethod.method_description
        analyticalmethod.sample_matrix = domain_analyticalmethod.sample_matrix
        analyticalmethod.instrument = domain_analyticalmethod.instrument
        analyticalmethod.cost_per_sample = domain_analyticalmethod.cost_per_sample
        analyticalmethod.save()

    def to_domain(self) -> DomainAnalyticalMethod:
        b = DomainAnalyticalMethod(
            method_name=self.method_name,
            method_description=self.method_description,
            sample_matrix=self.sample_matrix,
            instrument=self.instrument,
            cost_per_sample=self.cost_per_sample,
        )
        return b
