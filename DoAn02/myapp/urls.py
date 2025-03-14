from django.urls import path
from . import views
from .models import Phong, HopDong, KhachHang
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login'),
    path('menu/', views.menu, name='menu'),  # Thêm URL cho menu
    path('room/<int:phong_id>/', views.room_info, name='room_info'),
    path('themhopdong/<int:phong_id>/', views.them_hop_dong, name='them_hop_dong'),
    path('xemchitiethopdong/<int:hop_dong_id>/', views.xem_chi_tiet_hop_dong, name='xem_chi_tiet_hop_dong'),
    path('chinhsua/<int:phong_id>/', views.chinh_sua_phong, name='chinh_sua_phong'),
    path('xoa/<int:phong_id>/', views.xoa_phong, name='xoa_phong'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)