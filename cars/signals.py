from django.db.models.signals import *
from django.dispatch import receiver
from cars.models import *
from django.db.models import *
from openai_api.client import *


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = "Bio gerada automaticamente"

@receiver(post_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    car_inventory_update()