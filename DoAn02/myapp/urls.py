from django.urls import path
from . import views
from .models import Phong, HopDong, KhachHang, TaiKhoan
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
    path('themphong/', views.them_phong, name='them_phong'),
    path('thong-bao/', views.thong_bao, name='thongbaomoi'),
    path('xemtinnhan/<int:lien_he_id>/',views.view_contact_detail, name='xemtinnhan'),

    # Thêm các URL patterns mới
    path('quan-ly-khach-hang/', views.quan_ly_khach_hang, name='quan_ly_khach_hang'),
    path('doanh-thu/', views.doanh_thu, name='doanh_thu'),
    path('dich-vu/', views.dich_vu, name='dich_vu'),
    path('hoa-don/', views.hoa_don, name='hoa_don'),
    path('quan-li-hop-dong/', views.quan_li_hop_dong, name='quan_li_hop_dong'),
    path('dang-xuat/', views.dang_xuat, name='dang_xuat'),
    # Thêm URL patterns cho quản lý tài khoản khách hàng
    path('tao-tai-khoan/<int:khach_hang_id>/', views.tao_tai_khoan, name='tao_tai_khoan'),
    path('chinh-sua-tai-khoan/<int:khach_hang_id>/', views.chinh_sua_tai_khoan, name='chinh_sua_tai_khoan'),
    path('cap-nhat-hoa-don/', views.cap_nhat_hoa_don, name='cap_nhat_hoa_don'),
    # URL patterns cho quản lý dịch vụ
    path('cap-nhat-dich-vu/', views.cap_nhat_dich_vu, name='cap_nhat_dich_vu'),
    path('delete-service/<int:dich_vu_id>/', views.xoa_dich_vu, name='xoa_dich_vu'),
    path('cap-nhat-gia-dien-nuoc/', views.cap_nhat_gia_dien_nuoc, name='cap_nhat_gia_dien_nuoc'),
    path('cap-nhat-chi-so-dien-nuoc/', views.cap_nhat_chi_so_dien_nuoc, name='cap_nhat_chi_so_dien_nuoc'),
    path('xoa-chi-so-dien-nuoc/<int:chi_so_id>/', views.xoa_chi_so_dien_nuoc, name='xoa_chi_so_dien_nuoc'),
    path('xoa-gia-dien-nuoc/<int:gia_id>/', views.xoa_gia_dien_nuoc, name='xoa_gia_dien_nuoc'),
    path('process-payment/<int:chi_so_id>/', views.process_payment, name='process_payment'),
    path('xem-hoa-don/<int:chi_so_id>/', views.xem_hoa_don, name='xem_hoa_don'),
    path('login-khach-hang/', views.login_khach_hang, name='login_khach_hang'),
    path('trang-chu-khach-hang/', views.trang_chu_khach_hang, name='trang_chu_khach_hang'),
    
    # Thêm các URL mới cho các view
    path('thong-tin/', views.k_thong_tin, name='thong_tin'),  # URL cho k_thongtin.html
    path('lien-he/', views.lien_he, name='lien_he'),        # URL cho k_lienhemail.html
    path('hop-dong/', views.k_hop_dong, name='hop_dong'),    # URL cho k_hopdong.html
    path('k-hoa-don/', views.k_hoa_don, name='k_hoa_don'),        # URL cho k_hoadon.html
    path('logout/', views.logout_khach_hang, name='logout_khach_hang'),
    path('contact/', views.submit_contact, name='contact_form'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment/return/', views.payment_return, name='payment_return'),
    path('payment/notify/', views.payment_notify, name='payment_notify'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)