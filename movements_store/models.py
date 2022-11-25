from django.db import models

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

    transaction_type = models.CharField(
        max_length=100,
        choices=TransactionType.choices,
        default=TransactionType.DEBITO
    )
    date_of_currence = models.CharField(max_length=8)
    transaction_value = models.DecimalField(max_digits=10, decimal_places=2)
    card = models.CharField(max_length=12)
    time = models.CharField(max_length=6)
    store_name = models.ForeignKey(
        "stores.Store",
        on_delete=models.CASCADE,
        related_name="movements_store"
    )