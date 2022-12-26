from django.shortcuts import render
from django.forms import ValidationError
from rest_framework.serializers import *
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from product.models import products
import requests
from .serializer import productSerializer, productDetailSerializer
from rest_framework.response import Response

# Create your views here.
# a. Name b. Item Category c. Delivery Days d. Rating
# e. Price
# filter by name (using substring and not absolute string matching)
# get items with more than 'n' ratings, 'n' will be passed in the API as query parameter. Suppose 'n' is 3, then API should fetch all items with rating >=3
# Delivery Days less than 'n' (similar to rating but in opposite way)
# Sort by ascending / descending based on price. The API will have 'sort_type' which can have 'asc' or 'dsc' to determine type of sorting.
# @api_view(["GET"])
# def list_items(request,n):
#     query_parameters = request.query_params
#     Name = query_parameters.get("Name")
#     Category = query_parameters.get("Category")
#     Delivery_Time = query_parameters.get("Delivery_Time")
#     Rating  = query_parameters.get("Rating")
#     price = query_parameters.get("price")
#     product = products.objects.all().order_by('-price')
#     product = products.filter(product__contains="Name").filter(Rating>=n).filter(Delivery_Time<n)
#     serializer = productSerializer(product)
#     return Response(
#         dict(
#             Name = Name,
#             Category = Category,
#             Delivery_Time = Delivery_Time,
#             Rating = Rating,
#             price = price,
#         )
#     )

@api_view(["GET"])
def get_item_data(request,id):
    try:
        product = products.objects.get(id=id)
    except product.DoesNotExist:
        raise ValidationError(dict(detail="Sorry the item_id doesn't exist"))
    serializer = productDetailSerializer(product)
    return Response(dict(result=serializer))


# @api_view(["PATCH"])
# def buy_item(request, id):
#     query_parameters = request.query_params
#     Stock = query_parameters.get("Stock")
#     Sales_count = query_parameters.get("Sales_count")
#     product = products.objects.get(id=id)
#     product.update(
#         Stock=Stock-1,Sales_count=Sales_count+1
#     )
#     product.save(update_fields=[Stock,Sales_count])

@api_view(["DELETE"])
def delete_item(request, id):
    product= products.objects.get(id=id).delete()
    product.save()

@api_view(["POST"])
def Add_product(request):  
    Name = request.data.get("Name") 
    Category = request.data.get("Category") 
    Delivery_Time  = request.data.get("Delivery_Time")  
    Rating = request.data.get("Rating")
    Stock = request.data.get("Stock")
    price = request.data.get("price")
    created_at = request.data.get("created_at") 
    Sales_count= request.data.get("Sales_count")
    products.objects.create(  
        Name =  Name,
        Category = Category,
        Delivery_Time = Delivery_Time,
        Rating = Rating,
        Stock = Stock,
        price = price, 
        created_at = created_at,
        Sales_count = Sales_count
    )  
    return Response(dict(result=True))

# updated_rating = ((sales * current_rating) + input_rating ) / (sales + 1)
# @api_view(["PATCH"])
# def rate_product(request,id,input_rating):
#     query_parameters = request.query_params
#     Rating = query_parameters.get("Rating")
#     Sales_count = query_parameters.get("Sales_count")
#     product = products.objects.get(id=id)
#     product.update(
#         Rating=((Sales_count * input_rating) + input_rating ) / (Sales_count + 1)
#     )
#     product.save(update_fields=[Rating])

