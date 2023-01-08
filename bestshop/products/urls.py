from django.urls import path

from bestshop.products.views import home, product_add, product_details, buy, product_delete, product_edit, \
    comment_product, rate_product

urlpatterns = (
    path('', home, name='home'),
    path('add/', product_add, name='add product'),
    path('details/<int:pk>', product_details, name='details product'),
    path('delete/<int:pk>', product_delete, name='delete product'),
    path('edit/<int:pk>', product_edit, name='edit product'),
    path('comment/<int:pk>', comment_product, name='comment product'),
    path('rate/<int:pk>', rate_product, name='rate product'),
    path('buy/<int:pk>', buy, name='buy'),
)
