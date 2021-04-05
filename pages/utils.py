from django.db import transaction
from django_rq import job

from .models import Content


@job
def increment(pk):
    with transaction.atomic():
        counter = Content.objects.get(pk=pk)
        counter.counter += 1
        counter.save()
    return True
