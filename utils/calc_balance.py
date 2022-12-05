def calc_balance(transaction_type, transaction_value, current_value):

    if( 
        transaction_type=="Débito" or
        transaction_type=="Crédito" or
        transaction_type=="Recebimento Empréstimo" or
        transaction_type=="Vendas" or
        transaction_type=="Recebimento TED" or
        transaction_type=="Recebimento DOC"
    ):
        return current_value + transaction_value

    if(transaction_type=="Boleto" or transaction_type=="Financiamento" or transaction_type=="Aluguel"):
        return current_value - transaction_value

    