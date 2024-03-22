from django.db import models

class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    CHOICE_1 = "test1"
    CHOICE_2 = 'test2'
    ITEM_GROUPS = {
        CHOICE_1: "test1",
        CHOICE_2: "test2"
    }
    item_group = models.CharField(
        choices=ITEM_GROUPS,
        default=CHOICE_1
    )
    KILO = "Kilogram"
    MILI = "Miligram"
    UNITS = {
        KILO: "Kilogram",
        MILI: "Miligram"
    }
    unit_of_measurement = models.CharField(
        choices=UNITS,
        default=KILO
    )
    quantity = models.IntegerField()
    price_without_vat = models.IntegerField()
    status = models.CharField(max_length=50)
    storage_location = models.CharField(max_length=50, blank=True, null=True)
    contact_person = models.CharField(blank=True, null=True)
    photo = models.CharField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        """Return string representation of the id"""
        return f"{self.item_id}"
class TmaRequests(models.Model):
    request_id = models.AutoField(primary_key=True)
    employee_name = models.CharField()
    item = models.ForeignKey(Items, on_delete=models.CASCADE, blank=True, null=True)
    KILO = "Kilogram"
    MILI = "Miligram"
    UNITS = {
        KILO: "Kilogram",
        MILI: "Miligram"
    }
    unit_of_measurement = models.CharField(
        choices=UNITS,
        default=KILO
    )
    quantity = models.IntegerField()
    price_without_vat = models.IntegerField()
    comment = models.CharField(blank=True, null=True)
    DENIED = "Denied"
    APPROVED = "Approved"
    NEW = "New"
    ITEM_STATUS = {
        DENIED: "Denied",
        APPROVED: "Approved",
        NEW: "New"
    }
    status = models.CharField(
        choices=ITEM_STATUS,
        default=NEW,
        null=True)

    class Meta:
        verbose_name_plural = 'TmaRequests'