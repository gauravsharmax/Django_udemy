from . import views
from django.urls import path

urlpatterns = [
    #/food/
    path('',views.index,name='index'),
    #/food/1
    path('<int:item_id>/',views.details,name='detail'),
    #/food/item
    path('item/',views.item, name="item"),
] 