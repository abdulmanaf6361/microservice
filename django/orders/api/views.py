from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .models import Order
from .tasks import send_email
import json
from django.core import serializers


# TODO: add here your API Views
@api_view(http_method_names=["POST"])
def add_order(request):
    print(request.data)
    total_price = 0
    customer_name = request.data.get("customer_name")
    customer_email = request.data.get("customer_email")
    products_id = request.data.get("products_id", [])

    items = []

    for product_id in products_id:
        print(product_id)
        try:
            response = requests.get(f"http://nginx/api/v1/products/fetch/?prod_id={product_id}").json()
            print(response)

            if response and isinstance(response, list) and len(response) > 0:
                product_info = response[0]
                total_price += float(product_info.get("price", 0))

                items.append({
                    "item_name": product_info.get("name", ""),
                    "item_description": product_info.get("description", ""),
                    "item_price": product_info.get("price", 0),
                })
            else:
                return Response({"message": f"Product with id={product_id} not found"}, status=404)

        except requests.exceptions.RequestException as e:
            return Response({"message": f"Error fetching product information: {str(e)}"}, status=500)

    new_order = Order.objects.create(customer_name=customer_name, customer_email=customer_email, items=items, total=total_price)
    send_email.delay(email=customer_email, total=total_price, name=customer_name)

    return Response({"message": "Order successfully created! You'll get an email soon"}, status=201)