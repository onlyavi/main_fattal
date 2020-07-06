
# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import  static
# from inventory1.views import homepage_view, about_view, add_newitem_view, list_items_view, update_items,delete_items, under_construction, StockFSearch_view,  import_excel_view
# from inventory1.views import test_forms1, item_issue_view

urlpatterns = [
 
  
    path('about/', about_view, name='about'),
    path('add_newitem/', add_newitem_view, name='add_newitem'),
    path('testforms/', test_forms1, name='test_forms1'),
    path('list_items/', list_items_view, name='list_items_view'),

]