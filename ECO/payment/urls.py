from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path('basket/', views.BasketView, name='basket'),
    path('pay_by_green/', views.payByGreenView, name='pay_by_green'),
    path('orderplaced/', views.order_placed, name='order_placed'),
    # path('error/', views.Error.as_view(), name='error'),
    # path('webhook/', views.stripe_webhook, name='webhook'),
]
