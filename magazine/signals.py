from django.db.models.signals import post_save, post_delete
from django.utils import timezone


from project.celery import app
from . models import Discount
from . tasks import apply_discount



def add_discount_task(sender, instance, **kwargs):
    run_now = False

    if instance.date_begin <= timezone.now():
        run_now = True
    else:
        apply_discount.apply_async(args=(instance.id,), eta=instance.date_begin)

    if instance.date_end and instance.date_end <= timezone.now():
        run_now = True
    else:
        apply_discount.apply_async(args=(instance.id,), eta=instance.date_end)


    if run_now:
        apply_discount.run(instance.id)


post_save.connect(add_discount_task, Discount)
# post_delete.connect(delete_discount_task, Discount) # TODO: add discount delete task
