"""main_fattal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import  static
from inventory1.views import homepage_view, about_view, add_newitem_view, list_items_view, update_items,delete_items, under_construction, StockFSearch_view,  import_excel_view
from inventory1.views import test_forms1, item_issue_view
import inventory1.urls 

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', homepage_view, name='home'),
    path('about/', about_view, name='about'),
    path('add_newitem/', add_newitem_view, name='add_newitem'),
    path('testforms/', test_forms1, name='test_forms1'),
    path('list_items/', list_items_view, name='list_items_view'),
    #path('excel_upload/', excel_import_example, name='excel_import_example'),
    path('update_items/<str:pk>/', update_items, name="update_items"),
    #path('update_item', update_item, name="update_item"),
    #path(r'^delete_items/(?P<id>\d+)/delete$', delete_items, name='delete_items'),
    path('delete_items/<str:pk>/', delete_items, name='delete_items'),
    path('under_construction/', under_construction, name='under_construction'),
    path('full_search/', StockFSearch_view, name='StockFSearch_view'),
   # path('MEDIA_URL/', settings.MEDIA_URL ),
  
    path('excel_upload/', import_excel_view, name='import_excel_view'),
    path('index_issue/', item_issue_view, name='item_issue_view'),
    path('', include ('inventory1.urls'))
   # path('excel_upload1/', csv_view, name='csv_view'),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
