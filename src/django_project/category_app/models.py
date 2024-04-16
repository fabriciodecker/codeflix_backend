from uuid import uuid4
from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4) #se não declarar o django cria um id inteiro
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    # nome da tabela
    class Meta: 
        db_table = "category"

    def __str__(self):
        return self.name