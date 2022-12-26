from django.urls import path
from product.views import get_item_data, delete_item, Add_product
from . import views

urlpatterns = [
    # path("list_items", list_items, name="list_items"),
    path("<int:id>/get_item_data", get_item_data, name="get_item_data"),
    # path("<int:id>/buy_item", buy_item, name="buy_item"),
    path("<int:id>/delete_item",delete_item , name="delete_item"),
    # path("<int:id>/rate_product", rate_product, name="rate_product"),
    path("Add_product", Add_product, name="Add_product"),
]

