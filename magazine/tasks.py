from project.celery import app
from . models import Discount, Product



@app.task(serializer='json')
def apply_discount(discount_id):
    d = Discount.objects.get(id=discount_id)

    if d.discount_object.__class__ == Product:
        products = Product.objects.all()
    else:
        products = d.discount_object.products.all()

    for p in products:
        p.recalc_discount_price()
        p.save()
