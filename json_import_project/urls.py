from django.contrib import admin
from django.urls import path, include
from book.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookView, 'book')

urlpatterns = [
    # route, view
    path('admin/', admin.site.urls),

    path('', books),    
    path('rest/get_books', rest_get_books, name='jason_books'),

    path('import_data', import_data, name='import_data'),
    path('rest/import_data', rest_import_data, name='json_import'),

    path('update_book/<id>', update_book, name='update_book'),
    path('rest/update_book/<id>', rest_update_book, name='json_update'),

    path('delete_book/<id>', delete_book, name='delete_book'),
    path('rest/delete_book/<id>', rest_delete_book, name='json_delete'),
    
    path('api/', include(router.urls)),
]
