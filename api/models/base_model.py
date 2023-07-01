from django.db import models

class BaseModel(models.Model):
    """"""
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
        default_permissions = ('add', 'change', 'delete', 'view')