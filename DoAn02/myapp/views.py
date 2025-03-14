from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import QuanLi, Phong, HopDong, KhachHang
from django.http import Http404
from django.utils import timezone
from datetime import datetime, timedelta

def login_view(request):
    if request.method == 'POST':
        SoDienThoaiDN = request.POST['SoDienThoaiDN']
        MatKhauDN = request.POST['MatKhauDN']
        try:
            quanli = QuanLi.objects.get(SoDienThoaiDN=SoDienThoaiDN)
            print(f"MatKhauDN from DB: {quanli.MatKhauDN}")
            print(f"Input MatKhauDN: {MatKhauDN}")
            if check_password(MatKhauDN, quanli.MatKhauDN):
                messages.success(request, 'Đăng nhập thành công!')
                return redirect('menu')
            else:
                messages.error(request, 'Sai mật khẩu! (Debug: Check hash mismatch)')
                return redirect('login')
        except QuanLi.DoesNotExist:
            messages.error(request, 'Số điện thoại không tồn tại!')
            return redirect('login')
    return render(request, 'dangnhap.html')

def menu(request):
    phong_list = Phong.objects.all()
    rooms_data = []
    today = timezone.now().date()
    
    for index, phong in enumerate(phong_list, start=1):
        hop_dong = HopDong.objects.filter(PhongID=phong.PhongID, TrangThaiHopDong='HoatDong').first()
        khach_hang = hop_dong.KhachHangID if hop_dong else None
        
        trang_thai = "Chưa thuê"
        class_trang_thai = "chua-thue"
        hop_dong_id = None
        if hop_dong:
            hop_dong_id = hop_dong.HopDongID
            if hop_dong.NgayKetThuc < today:
                trang_thai = "Hết Hạn"
                class_trang_thai = "het-han"
            elif (hop_dong.NgayKetThuc - today).days <= 30:
                trang_thai = "Sắp Hết Hạn"
                class_trang_thai = "sap-het-han"
            else:
                trang_thai = "Đang Hoạt Động"
                class_trang_thai = "active"
        
        room_info = {
            'stt': index,
            'phong_id': phong.PhongID,
            'day_phong': phong.DayPhong,
            'so_phong': phong.SoPhong,
            'gia_phong': phong.GiaPhong,
            'ten_khach_hang': khach_hang.HoTenKhachHang if khach_hang else 'Chưa có',
            'so_dien_thoai': khach_hang.SoDienThoai if khach_hang else 'Chưa có',
            'trang_thai': trang_thai,
            'class_trang_thai': class_trang_thai,
            'hop_dong_id': hop_dong_id,  # Đảm bảo có hop_dong_id
        }
        rooms_data.append(room_info)
    
    context = {'rooms': rooms_data}
    return render(request, 'menu.html', context)

def room_info(request, phong_id):
    try:
        phong = Phong.objects.get(PhongID=phong_id)
        hop_dong = HopDong.objects.filter(PhongID=phong_id, TrangThaiHopDong='HoatDong').first()
        khach_hang = hop_dong.KhachHangID if hop_dong else None
        context = {
            'rooms': [{
                'stt': 1,
                'phong_id': phong.PhongID,
                'day_phong': phong.DayPhong,
                'so_phong': phong.SoPhong,
                'gia_phong': phong.GiaPhong,
                'ten_khach_hang': khach_hang.HoTenKhachHang if khach_hang else 'Chưa có',
                'so_dien_thoai': getattr(khach_hang, 'SoDienThoai', 'Chưa có') if khach_hang else 'Chưa có',
            }]
        }
        return render(request, 'menu.html', context)
    except Phong.DoesNotExist:
        raise Http404("Phòng không tồn tại")

    # phong = Phong.objects.get(PhongID=phong_id)
    
    # if request.method == 'POST':
    #     # Lưu thông tin KhachHang
    #     khach_hang = KhachHang.objects.create(
    #         HoTenKhachHang=request.POST['ho_ten_khach_hang'],
    #         SoDienThoai=request.POST['so_dien_thoai'],
    #         CMND_CCCD=request.POST.get('cmnd_cccd', ''),
    #         NgaySinh=request.POST.get('ngay_sinh') or None,
    #         GioiTinh=request.POST['gioi_tinh'],
    #         TinhThanhPho=request.POST.get('tinh_thanh_pho', ''),
    #         QuanHuyen=request.POST.get('quan_huyen', ''),
    #         PhuongXa=request.POST.get('phuong_xa', ''),
    #         DiaChiChiTiet=request.POST.get('dia_chi_chi_tiet', ''),
    #         CongViec=request.POST.get('cong_viec', ''),
    #         NgayCapCMND=request.POST.get('ngay_cap_cmnd') or None,
    #         NoiCapCMND=request.POST.get('noi_cap_cmnd', ''),
    #         AnhMatTruoc=request.FILES.get('anh_mat_truoc'),
    #         AnhMatSau=request.FILES.get('anh_mat_sau')
    #     )

    #     # Tính ngày kết thúc dựa trên thời hạn hợp đồng
    #     ngay_vao_o = datetime.strptime(request.POST['ngay_vao_o'], '%Y-%m-%d').date()
    #     thoi_han = request.POST['thoi_han_hop_dong']
    #     if thoi_han == '3 tháng':
    #         ngay_ket_thuc = ngay_vao_o + timedelta(days=90)
    #     elif thoi_han == '6 tháng':
    #         ngay_ket_thuc = ngay_vao_o + timedelta(days=180)
    #     elif thoi_han == '8 tháng':
    #         ngay_ket_thuc = ngay_vao_o + timedelta(days=240)
    #     elif thoi_han == '1 năm':
    #         ngay_ket_thuc = ngay_vao_o + timedelta(days=365)
    #     elif thoi_han == '2 năm':
    #         ngay_ket_thuc = ngay_vao_o + timedelta(days=730)
    #     elif thoi_han == '3 năm':
    #         ngay_ket_thuc = ngay_vao_o + timedelta(days=1095)
    #     elif thoi_han == '4 năm':
    #         ngay_ket_thuc = ngay_vao_o + timedelta(days=1460)
    #     elif thoi_han == '5 năm':
    #         ngay_ket_thuc = ngay_vao_o + timedelta(days=1825)
    #     elif thoi_han == '6 năm':
    #         ngay_ket_thuc = ngay_vao_o + timedelta(days=2190)
    #     else:
    #         ngay_ket_thuc = request.POST.get('ngay_ket_thuc') or (ngay_vao_o + timedelta(days=365))

    #     # Lưu thông tin HopDong
    #     hop_dong = HopDong.objects.create(
    #         PhongID=phong,
    #         KhachHangID=khach_hang,
    #         SoLuongThanhVien=request.POST['member_count'],
    #         ThoiHanHopDong=thoi_han,
    #         NgayVaoO=ngay_vao_o,
    #         NgayKetThuc=ngay_ket_thuc,
    #         SoTienPhong=request.POST['so_tien_phong'],
    #         SoTienCoc=request.POST['so_tien_coc'],
    #         ChuKyThuTien=request.POST['chu_ky_thu_tien'],
    #         GhiChuHopDong=request.POST['ghi_chu_hop_dong'],
    #         TrangThaiHopDong='HoatDong'
    #     )

    #     # Cập nhật trạng thái phòng
    #     phong.TrangThaiPhong = 'DaThue'
    #     phong.save()

    #     messages.success(request, 'Thêm hợp đồng thành công!')
    #     return redirect('menu')

    # context = {'phong': phong}
    # return render(request, 'themhopdong.html', context)

def chinh_sua_phong(request, phong_id):
    try:
        phong = Phong.objects.get(PhongID=phong_id)
        if request.method == 'POST':
            # Logic chỉnh sửa phòng (sẽ thêm sau nếu bạn cần)
            messages.success(request, 'Phòng đã được chỉnh sửa!')
            return redirect('menu')
        context = {'phong': phong}
        return render(request, 'chinhsuaphong.html', context)
    except Phong.DoesNotExist:
        raise Http404("Phòng không tồn tại")

def xoa_phong(request, phong_id):
    try:
        phong = Phong.objects.get(PhongID=phong_id)
        phong.delete()
        messages.success(request, 'Phòng đã được xóa!')
        return redirect('menu')
    except Phong.DoesNotExist:
        raise Http404("Phòng không tồn tại")
    
def them_phong(request):
    if request.method == 'POST':
        day_phong = request.POST['day_phong']
        so_phong = request.POST['so_phong']
        gia_phong = request.POST['gia_phong']
        dien_tich = request.POST['dien_tich']
        mo_ta = request.POST.get('mo_ta', '')
        tien_ich = request.POST.getlist('tien_ich')

        Phong.objects.create(
            DayPhong=day_phong,
            SoPhong=so_phong,
            GiaPhong=gia_phong,
            DienTich=dien_tich,
            MoTaPhong=mo_ta,
            TrangThaiPhong='ConTrong',
            TienIch=tien_ich
        )
        messages.success(request, 'Thêm phòng thành công!')
        return redirect('menu')
    
    return render(request, 'themphong.html')

def them_hop_dong(request, phong_id):
    try:
        phong = Phong.objects.get(PhongID=phong_id)
    except Phong.DoesNotExist:
        messages.error(request, 'Phòng không tồn tại!')
        return redirect('menu')
    
    if request.method == 'POST':
        # Lưu thông tin KhachHang
        khach_hang = KhachHang.objects.create(
            HoTenKhachHang=request.POST['ho_ten_khach_hang'],
            SoDienThoai=request.POST['so_dien_thoai'],
            SoCCCD=request.POST.get('CMND_CCCD', ''),  # Sửa tên từ CMND_CCCD thành SoCCCD
            NgaySinh=datetime.strptime(request.POST['ngay_sinh'], '%Y-%m-%d').date() if request.POST.get('ngay_sinh') else None,
            GioiTinh=request.POST['gioi_tinh'],
            TinhThanh=request.POST.get('tinh_thanh_pho', ''),
            QuanHuyen=request.POST.get('quan_huyen', ''),
            PhuongXa=request.POST.get('phuong_xa', ''),
            DiaChiCuThe=request.POST.get('dia_chi_chi_tiet', ''),
            CongViec=request.POST.get('cong_viec', ''),
            NgayCapCCCD=datetime.strptime(request.POST['ngay_cap_cmnd'], '%Y-%m-%d').date() if request.POST.get('ngay_cap_cmnd') else None,
            NoiCapCCCD=request.POST.get('noi_cap_cmnd', ''),
            CCCDMT=request.FILES.get('anh_mat_truoc'),
            CCCDMS=request.FILES.get('anh_mat_sau')
        )

        # Tính ngày kết thúc dựa trên thời hạn hợp đồng
        ngay_vao_o = datetime.strptime(request.POST['ngay_vao_o'], '%Y-%m-%d').date()
        thoi_han = request.POST['thoi_han_hop_dong']
        if thoi_han == '3 tháng':
            ngay_ket_thuc = ngay_vao_o + timedelta(days=90)
        elif thoi_han == '6 tháng':
            ngay_ket_thuc = ngay_vao_o + timedelta(days=180)
        elif thoi_han == '8 tháng':
            ngay_ket_thuc = ngay_vao_o + timedelta(days=240)
        elif thoi_han == '1 năm':
            ngay_ket_thuc = ngay_vao_o + timedelta(days=365)
        elif thoi_han == '2 năm':
            ngay_ket_thuc = ngay_vao_o + timedelta(days=730)
        elif thoi_han == '3 năm':
            ngay_ket_thuc = ngay_vao_o + timedelta(days=1095)
        elif thoi_han == '4 năm':
            ngay_ket_thuc = ngay_vao_o + timedelta(days=1460)
        elif thoi_han == '5 năm':
            ngay_ket_thuc = ngay_vao_o + timedelta(days=1825)
        elif thoi_han == '6 năm':
            ngay_ket_thuc = ngay_vao_o + timedelta(days=2190)
        else:
            ngay_ket_thuc = request.POST.get('ngay_ket_thuc') or (ngay_vao_o + timedelta(days=365))

        # Lưu thông tin HopDong
        hop_dong = HopDong.objects.create(
            PhongID=phong,
            KhachHangID=khach_hang,
            NgayBatDau=ngay_vao_o,
            NgayKetThuc=ngay_ket_thuc,
            TienDatCoc=request.POST['so_tien_coc'],
            ChuKy=request.POST['chu_ky_thu_tien'],
            TrangThaiHopDong='HoatDong'
        )

        # Cập nhật trạng thái phòng
        phong.TrangThaiPhong = 'DaThue'
        phong.save()

        messages.success(request, 'Thêm hợp đồng thành công!')
        return redirect('menu')

    context = {'phong': phong, 'phong_id': phong_id}
    return render(request, 'themhopdong.html', context)

def xem_chi_tiet_hop_dong(request, hop_dong_id):
    try:
        # Lấy hợp đồng dựa trên HopDongID
        hop_dong = HopDong.objects.get(HopDongID=hop_dong_id)
        khach_hang = hop_dong.KhachHangID
        phong = hop_dong.PhongID
        
        context = {
            'hop_dong': hop_dong,
            'khach_hang': khach_hang,
            'phong': phong,
        }
        return render(request, 'xemchitiethopdong.html', context)
    except HopDong.DoesNotExist:
        messages.error(request, 'Hợp đồng không tồn tại!')
        return redirect('menu')