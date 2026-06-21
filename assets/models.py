from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Asset(models.Model):

    item_id = models.CharField(max_length=50)

    item_name = models.CharField(max_length=100)

    category = models.CharField(max_length=100)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.item_name