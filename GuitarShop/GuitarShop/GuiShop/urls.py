from django.urls import path
from GuiShop.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from cart.views import *

urlpatterns = [
    path('index/<slug:cat_slag>/', RenderIndex, name='category'),
    path("product/<slug:post_slug>/", RenderProduct, name='product'),
    path("cart/", cart_detail, name='cart')

]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
