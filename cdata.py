import random
import datetime
import random
from django.db.models import NOT_PROVIDED
from django.db import models
from django.utils.timezone import now

def create_detail(model, force):
    fields = list(filter(
        lambda field:
        (not field.null
        and (field.default == NOT_PROVIDED or field.default == '')
        and not (hasattr(field, 'auto_now') and field.auto_now))
        or field.name in force
        , model._meta.fields
    ))
    related = {
        field.name: field.related_model for field in fields if field.related_model
    }
    alls = {}

    for field in fields:
        if field.primary_key: continue
        if field.related_model:
            col = field.name
            _all = related[col].objects.all()
            if not _all:
                create_data(related[col], i=2)
                _all = related[col].objects.all()
            alls[col]= random.choice(_all)
        elif field.choices:
            alls[field.column]= random.choice(field.choices)[0]
        elif field.default == '':
            alls[field.column] = '123456'
        else:
            if isinstance(field, models.DecimalField):
                alls[field.column] = random.random()*100
            elif isinstance(field, models.DateField):
                alls[field.column] = now()
            elif isinstance(field, models.DateTimeField):
                alls[field.column] = now()
            elif isinstance(field, models.IntegerField):
                alls[field.column] = random.randint(1,9)
            else:
                alls[field.column] = field.verbose_name + str(random.random()*1000)[:3]
    return alls


"""
model: Model object of installed applications
force: General case, the field will be excluded if it can be nullable or have default value
        this is a list of fields name of model, field won't be excluded if it in this list
i: Creating data times
"""
def create_data(model, force=[], i=1):
    for i in range(i):
        detail = create_detail(model, force)
        model(**detail).save()
