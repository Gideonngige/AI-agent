from chat_app.models import Customer, Sale

def get_total_customers():
    return Customer.objects.count()


def get_total_sales():
    total = sum(
        sale.amount
        for sale in Sale.objects.all()
    )

    return float(total)