from django.db import models
import uuid

class TransactionType(models.TextChoices):
    DEBITO = "Débito"
    BOLETO = "Boleto"
    CREDITO = "Crédito"
    FIN = "Financiamento"
    REC_EMP = "Recebimento Empréstimo"
    VENDAS = "Vendas"
    TED = "Recebimento TED"
    DOC = "Recebimento DOC"
    ALUG = "Aluguel"


class MovementStore(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    
    transaction_type = models.CharField(
        max_length=100,
        choices=TransactionType.choices,
        default=TransactionType.DEBITO
    )
    date_of_currence = models.CharField(max_length=11)
    transaction_value = models.DecimalField(max_digits=10, decimal_places=2)
    card = models.CharField(max_length=12)
    time = models.CharField(max_length=8)
    store = models.ForeignKey(
        "stores.Store",
        on_delete=models.CASCADE,
        related_name="movements_store"
    )

    doc_cnab = models.ForeignKey(
        'movements.Movement',
        on_delete=models.CASCADE,
        related_name='movement_list'
    )