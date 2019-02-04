from django.db import models

# Create your models here.
class Data(models.Model):
    AREA_UNIT_CHOICES = (
        ('SqFt', 'Square Feet'),
    )

    HOME_TYPE = (
        ('SFAM', "Single Family"),
        ('CONDO', "Condominium"),
        ('APRT', 'Apartment'),
        ('DPLX', 'Duplex'),
        ('MISC', 'Miscellaneous'),
        ('MFAM', 'Multi Family 2 To 4'),
        ('VCRL', 'Vacant Residential Land'),
    )
    id = models.AutoField(primary_key=True)
    area_unit = models.CharField(default=None, blank=True, null=True, max_length=4, choices=AREA_UNIT_CHOICES)
    bathrooms = models.DecimalField(default=None, blank=True, null=True, max_digits=4, decimal_places=1)
    bedrooms = models.PositiveSmallIntegerField(default=None, blank=True, null=True)
    home_size = models.PositiveIntegerField(default=None, blank=True, null=True)
    home_type = models.CharField(default=None, blank=True, null=True, max_length=75, choices=HOME_TYPE)
    last_sold_date = models.DateField(default=None, blank=True, null=True)
    last_sold_price = models.PositiveIntegerField(default=None, blank=True, null=True)
    link = models.URLField(default=None, blank=True, null=True)
    price = models.PositiveIntegerField(default=None, blank=True, null=True)
    property_size = models.PositiveIntegerField(default=None, blank=True, null=True)
    rent_price = models.PositiveIntegerField(default=None, blank=True, null=True)
    rentzestimate_amount = models.PositiveIntegerField(default=None, blank=True, null=True)
    rentzestimate_last_updated = models.DateField(default=None, blank=True, null=True)
    tax_value = models.PositiveIntegerField(default=None, blank=True, null=True)
    tax_year = models.PositiveSmallIntegerField(default=None, blank=True, null=True)
    year_built = models.PositiveSmallIntegerField(default=None, blank=True, null=True)
    zestimate_amount = models.PositiveIntegerField(default=None, blank=True, null=True)
    zestimate_last_updated = models.DateField(default=None, blank=True, null=True)
    zillow_id = models.CharField(default=None, blank=True, null=True, max_length=10)
    address = models.CharField(default=None, blank=True, null=True, max_length=255)
    city = models.CharField(default=None, blank=True, null=True, max_length=255)
    state = models.CharField(default=None, blank=True, null=True, max_length=2)
    zipcode = models.CharField(default=None, blank=True, null=True, max_length=5)
    def __str__(self):
        title = self.address + ', ' + self.city +  ', ' + self.state + ' ' + self.zipcode
        return title
    class Meta:
        verbose_name_plural = "Data"

