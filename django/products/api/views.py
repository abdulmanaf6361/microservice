import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


@api_view(http_method_names=["GET", "POST"])
def categories(request):
    if request.method == "POST":
        new_cat = Category.objects.create(name=request.data["category_name"])
    
    categories_lst = Category.objects.all()
    srlz = CategorySerializer(categories_lst, many=True)
    return Response(srlz.data)


@api_view(http_method_names=["GET"])
def products_fetch(request):
    cat_id = request.query_params.get("cat_id")
    prod_id = request.query_params.get("prod_id")

    if cat_id:
        products_list = Product.objects.filter(category__id=cat_id)
    elif prod_id:
        products_list = Product.objects.filter(id=prod_id)
    else:
        products_list = Product.objects.all()

    if products_list.exists():
        srlz = ProductSerializer(products_list, many=True)
        return Response(srlz.data, status=200)
    else:
        return Response({"message": "Sorry not found!"}, status=404)


@api_view(http_method_names=["POST"])
def products_create(request):
    try:
        category_id = request.data.get("cat_id")
        category = Category.objects.get(id=category_id)  # Retrieve Category instance
    except Category.DoesNotExist:
        return Response({"message": "Category does not exist"}, status=400)

    # Create new product instance
    new_prod = Product.objects.create(
        category=category,
        name=request.data.get("prod_name"),
        price=request.data.get("prod_price"),
        description=request.data.get("prod_description"),
    )
    return Response({"message": "Product added successfully"}, status=201)


@api_view(http_method_names=["DELETE"])
def products_delete(request):
    prod_id = request.query_params.get("prod_id")

    if not prod_id:
        return Response({"message": "prod_id parameter is required in the query string"}, status=400)

    try:
        product = Product.objects.get(id=prod_id)
    except Product.DoesNotExist:
        return Response({"message": "Product not found"}, status=404)

    product.delete()
    return Response({"message": "Product deleted successfully"}, status=204)