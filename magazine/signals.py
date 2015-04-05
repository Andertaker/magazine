from django.db.models.signals import post_save, post_delete
from django.utils import timezone


from project.celery import app
from . models import Discount
from . tasks import apply_discount



def add_discount_task(sender, instance, **kwargs):
    if instance.date_begin <= timezone.now():
        apply_discount.run(instance.id)
    else:
        apply_discount.apply_async(args=(instance.id,), eta=instance.date_begin)

    if instance.date_end:
        apply_discount.apply_async(args=(instance.id,), eta=instance.date_end)





post_save.connect(add_discount_task, Discount)
# post_delete.connect(delete_discount_task, Discount) # TODO: add discount delete task
