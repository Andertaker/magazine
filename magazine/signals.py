from django.db.models.signals import post_save, post_delete
from django.utils import timezone


from project.celery import app
from . models import Discount, Product


@app.task(serializer='json')
def apply_discount(discount_id):
    discount = Discount.objects.get(id=discount_id)

    p = Product.objects.get(id=discount.object_id)
    p.discount_amount = discount.amount
    p.price_with_discount = p.price * (100 - discount.amount) / 100
    p.save()


def add_discount_task(sender, instance, **kwargs):
    # apply_discount.run(instance)
    apply_discount.apply_async(args=(instance.id,), eta=timezone.now())



post_save.connect(add_discount_task, Discount)
post_delete.connect(add_discount_task, Discount)
