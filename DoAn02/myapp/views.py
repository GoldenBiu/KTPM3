from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import QuanLi, Phong, HopDong, KhachHang, TaiKhoan,DichVu, ChiSoDienNuoc, GiaDienNuoc
from django.http import Http404, HttpResponse
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Q, Sum
import random
import string
from decimal import Decimal
import json  # Ensure this import is at the top of your views.py

def login_view(request):
    if request.method == 'POST':
        SoDienThoaiDN = request.POST['SoDienThoaiDN']
        MatKhauDN = request.POST['MatKhauDN']
        try:
            quanli = QuanLi.objects.get(SoDienThoaiDN=SoDienThoaiDN)
            print(f"MatKhauDN from DB: {quanli.MatKhauDN}")
            print(f"Input MatKhauDN: {MatKhauDN}")
            if check_password(MatKhauDN, quanli.MatKhauDN):
                # Lưu thông tin quản lý vào session
                request.session['quan_li_id'] = quanli.QuanLiID
                request.session['ho_ten_quan_li'] = quanli.HoTenQuanLi
                request.session.set_expiry(86400)  # Session hết hạn sau 24 giờ
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
    # Khởi tạo queryset cơ bản
    phong_list = Phong.objects.all()
    rooms_data = []
    today = timezone.now().date()
    
    # Lấy tên quản lý từ session và debug
    ho_ten_quan_li = request.session.get('ho_ten_quan_li', '')
    print(f"Session data: {request.session.items()}")  # Debug session data
    print(f"Manager name from session: {ho_ten_quan_li}")  # Debug manager name
    
    # Lấy tất cả tham số tìm kiếm từ request
    search_params = {
        'search': request.GET.get('search', ''),
        'day': request.GET.get('day', ''),
        'so_phong': request.GET.get('so_phong', ''),
        'gia': request.GET.get('gia', ''),
        'trang_thai': request.GET.get('trang_thai', '')
    }

    # Lấy các giá trị duy nhất cho dropdown
    unique_days = Phong.objects.values_list('DayPhong', flat=True).distinct()
    unique_rooms = Phong.objects.values_list('SoPhong', flat=True).distinct()
    unique_prices = Phong.objects.values_list('GiaPhong', flat=True).distinct()

    # Kiểm tra xem có thực hiện tìm kiếm không
    has_search = any(search_params.values())
    if has_search:
        messages.success(request, 'Tìm kiếm thành công!')

    # Xây dựng điều kiện tìm kiếm
    search_conditions = Q()
    
    # Tìm kiếm theo text (nếu có)
    if search_params['search']:
        search_conditions |= (
            Q(SoPhong__icontains=search_params['search']) |
            Q(DayPhong__icontains=search_params['search']) |
            Q(hopdong__KhachHangID__HoTenKhachHang__icontains=search_params['search']) |
            Q(hopdong__KhachHangID__SoDienThoai__icontains=search_params['search']) |
            Q(TienIch__icontains=search_params['search']) |
            Q(DienTich__icontains=search_params['search'])
        )
    
    # Lọc theo dãy phòng
    if search_params['day'] and search_params['day'] != 'Tất cả':
        search_conditions &= Q(DayPhong=search_params['day'])
    
    # Lọc theo số phòng
    if search_params['so_phong'] and search_params['so_phong'] != 'Tất cả':
        search_conditions &= Q(SoPhong=search_params['so_phong'])
    
    # Lọc theo giá phòng
    if search_params['gia'] and search_params['gia'] != 'Tất cả':
        search_conditions &= Q(GiaPhong=search_params['gia'])
    
    # Lọc theo trạng thái
    if search_params['trang_thai']:
        if search_params['trang_thai'] == 'DaThue':
            search_conditions &= Q(TrangThaiPhong='DaThue')
        elif search_params['trang_thai'] == 'ConTrong':
            search_conditions &= Q(TrangThaiPhong='ConTrong')

    # Áp dụng tất cả điều kiện tìm kiếm
    if search_conditions:
        phong_list = phong_list.filter(search_conditions).distinct()

    # Xử lý dữ liệu phòng
    for index, phong in enumerate(phong_list, start=1):
        hop_dong = HopDong.objects.filter(PhongID=phong.PhongID, TrangThaiHopDong='HoatDong').first()
        khach_hang = hop_dong.KhachHangID if hop_dong else None
        
        # Xác định trạng thái và class
        trang_thai, class_trang_thai = "Chưa thuê", "chua-thue"
        if hop_dong:
            if hop_dong.NgayKetThuc < today:
                trang_thai, class_trang_thai = "Hết Hạn", "het-han"
            elif (hop_dong.NgayKetThuc - today).days <= 30:
                trang_thai, class_trang_thai = "Sắp Hết Hạn", "sap-het-han"
            else:
                trang_thai, class_trang_thai = "Đang Hoạt Động", "active"
        
        # Tạo thông tin phòng
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
            'hop_dong_id': hop_dong.HopDongID if hop_dong else None,
        }
        rooms_data.append(room_info)
    
    # Chuẩn bị context
    context = {
        'rooms': rooms_data,
        'unique_days': sorted(unique_days),
        'unique_rooms': sorted(unique_rooms),
        'unique_prices': sorted(unique_prices),
        'ho_ten_quan_li': ho_ten_quan_li,  # Thêm tên quản lý vào context
        **search_params  # Thêm tất cả tham số tìm kiếm vào context
    }
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
                'hop_dong_id': hop_dong.HopDongID if hop_dong else None,
                'ten_khach_hang': khach_hang.HoTenKhachHang if khach_hang else 'Chưa có',
                'so_dien_thoai': getattr(khach_hang, 'SoDienThoai', 'Chưa có') if khach_hang else 'Chưa có',
            }]
        }
        return render(request, 'menu.html', context)
    except Phong.DoesNotExist:
        raise Http404("Phòng không tồn tại")

def chinh_sua_phong(request, phong_id):
    try:
        phong = Phong.objects.get(PhongID=phong_id)
        if request.method == 'POST':
            phong.DayPhong = request.POST['day_phong']
            phong.SoPhong = request.POST['so_phong']
            phong.GiaPhong = request.POST['gia_phong']
            phong.DienTich = request.POST['dien_tich']
            phong.MoTaPhong = request.POST.get('mo_ta', '')
            phong.TrangThaiPhong = request.POST['trang_thai_phong']
            phong.save()
            messages.success(request, 'Phòng đã được chỉnh sửa!')
            return redirect('menu')
        context = {'phong': phong}
        return render(request, 'chinhsuaphong.html', context)
    except Phong.DoesNotExist:
        raise Http404("Phòng không tồn tại")

def xoa_phong(request, phong_id):
    try:
        phong = Phong.objects.get(PhongID=phong_id)
        
        # Kiểm tra xem phòng có đang ở trạng thái "ConTrong" không
        if phong.TrangThaiPhong == 'ConTrong':
            # Đây là lần xóa thứ hai (phòng đã ở trạng thái trống)
            # Tiến hành xóa phòng hoàn toàn
            phong.delete()
            messages.success(request, 'Phòng đã được xóa hoàn toàn khỏi hệ thống!')
            return redirect('menu')
        else:
            # Đây là lần xóa đầu tiên (phòng đang có hợp đồng)
            # Tìm các hợp đồng liên quan đến phòng
            hop_dong_list = HopDong.objects.filter(PhongID=phong.PhongID)
            
            # Xóa hợp đồng và khách hàng liên quan
            for hop_dong in hop_dong_list:
                khach_hang = hop_dong.KhachHangID
                # Xóa tài khoản liên quan đến khách hàng (nếu có)
                try:
                    tai_khoan = TaiKhoan.objects.get(KhachHangID=khach_hang)
                    tai_khoan.delete()
                except TaiKhoan.DoesNotExist:
                    pass
                
                # Xóa hợp đồng
                hop_dong.delete()
                
                # Xóa khách hàng
                khach_hang.delete()
            
            # Đặt lại trạng thái phòng về "ConTrong"
            phong.TrangThaiPhong = 'ConTrong'
            phong.save()
            
            messages.success(request, 'Đã xóa thông tin hợp đồng và khách hàng, phòng đã được đặt về trạng thái trống! Nhấn nút xóa lần nữa để xóa hoàn toàn phòng.')
            return redirect('menu')
    except Phong.DoesNotExist:
        raise Http404("Phòng không tồn tại")
    
def them_phong(request):
    if request.method == 'POST':
        try:
            day_phong = request.POST['day_phong']
            so_phong = request.POST['so_phong']
            gia_phong = request.POST['gia_phong']
            dien_tich = request.POST['dien_tich']
            mo_ta = request.POST.get('mo_ta', '')
            tien_ich = request.POST.getlist('tien_ich')

            # Tạo phòng mới
            phong = Phong.objects.create(
                DayPhong=day_phong,
                SoPhong=so_phong,
                GiaPhong=gia_phong,
                DienTich=dien_tich,
                MoTaPhong=mo_ta,
                TrangThaiPhong='ConTrong',
                TienIch=tien_ich
            )

            # Thêm thông báo thành công
            messages.success(request, 'Thêm phòng thành công!')
            
            # Thêm thông báo chi tiết
            messages.info(request, f'Thông tin phòng: Dãy {day_phong} - Phòng {so_phong} - Diện tích {dien_tich}m² - Giá {gia_phong}đ')
            
            return redirect('menu')
        except Exception as e:
            messages.error(request, f'Có lỗi xảy ra khi thêm phòng: {str(e)}')
            return redirect('them_phong')
    
    return render(request, 'themphong.html')

def them_hop_dong(request, phong_id):
    try:
        phong = Phong.objects.get(PhongID=phong_id)
        # Lấy thông tin quản lý từ session
        quan_li_id = request.session.get('quan_li_id')
        if not quan_li_id:
            messages.error(request, 'Vui lòng đăng nhập để thực hiện chức năng này!')
            return redirect('login')
            
        quan_li = QuanLi.objects.get(QuanLiID=quan_li_id)
        
        if request.method == 'POST':
            try:
                # Validate required fields
                required_fields = ['ho_ten_khach_hang', 'so_dien_thoai', 'gioi_tinh', 'ngay_vao_o', 'so_tien_phong', 'so_tien_coc', 'ghi_chu_hop_dong']
                for field in required_fields:
                    if not request.POST.get(field):
                        messages.error(request, f'Vui lòng điền đầy đủ thông tin bắt buộc!')
                        return redirect('them_hop_dong', phong_id=phong_id)

                # Lưu thông tin KhachHang
                khach_hang = KhachHang.objects.create(
                    HoTenKhachHang=request.POST['ho_ten_khach_hang'],
                    SoDienThoai=request.POST['so_dien_thoai'],
                    SoCCCD=request.POST.get('CMND_CCCD', ''),
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
                thoi_han = request.POST.get('thoi_han_hop_dong', '1 năm')
                
                # Tính ngày kết thúc dựa trên thời hạn
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
                    DayPhong=phong.DayPhong,
                    NgayBatDau=ngay_vao_o,
                    NgayKetThuc=ngay_ket_thuc,
                    ChuKy=request.POST.get('chu_ky_thu_tien', '1 tháng'),
                    TienDatCoc=request.POST.get('so_tien_coc', 0),
                    TrangThaiHopDong='HoatDong',
                    SoLuongThanhVien=request.POST.get('member_count', 1),
                    GhiChuHopDong=request.POST.get('ghi_chu_hop_dong', ''),
                    ThoiHanHopDong=thoi_han
                )

                # Cập nhật trạng thái phòng
                phong.TrangThaiPhong = 'DaThue'
                phong.save()

                # Thêm thông báo thành công
                messages.success(request, 'Hợp đồng đã được lưu thành công!')
                
                # Thêm thông báo chi tiết
                messages.info(request, f'Thông tin hợp đồng: Phòng {phong.DayPhong}{phong.SoPhong} - Khách hàng: {khach_hang.HoTenKhachHang} - Thời hạn: {thoi_han}')
                
                return redirect('menu')
                
            except Exception as e:
                messages.error(request, f'Có lỗi xảy ra khi thêm hợp đồng: {str(e)}')
                return redirect('them_hop_dong', phong_id=phong_id)

        context = {
            'phong': phong, 
            'phong_id': phong_id,
            'quan_li': quan_li
        }
        return render(request, 'themhopdong.html', context)
        
    except Phong.DoesNotExist:
        messages.error(request, 'Phòng không tồn tại!')
        return redirect('menu')
    except QuanLi.DoesNotExist:
        messages.error(request, 'Không tìm thấy thông tin quản lý!')
        return redirect('login')

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
    
def dang_xuat(request):
    # Xóa tất cả dữ liệu session
    request.session.flush()
    messages.success(request, 'Đăng xuất thành công!')
    return redirect('login')

def quan_ly_khach_hang(request):
    # Lấy tên quản lý từ session
    ho_ten_quan_li = request.session.get('ho_ten_quan_li', '')
    
    # Lấy tất cả khách hàng từ database
    khach_hang_list = KhachHang.objects.all()
    
    # Lấy tham số tìm kiếm từ URL
    search_query = request.GET.get('search', '')
    day = request.GET.get('day', '')
    so_phong = request.GET.get('so_phong', '')
    trang_thai = request.GET.get('trang_thai', '')
    
    # Lọc theo tìm kiếm
    if search_query:
        khach_hang_list = khach_hang_list.filter(
            Q(HoTenKhachHang__icontains=search_query) |
            Q(SoDienThoai__icontains=search_query)
        )
    
    # Lọc theo dãy phòng
    if day and day != 'Tất cả':
        khach_hang_list = khach_hang_list.filter(hopdong__DayPhong=day)
    
    # Lọc theo số phòng
    if so_phong and so_phong != 'Tất cả':
        khach_hang_list = khach_hang_list.filter(hopdong__PhongID__SoPhong=so_phong)
    
    # Lọc theo trạng thái tài khoản
    if trang_thai:
        if trang_thai == 'DaThue':  # Đã có tài khoản
            khach_hang_list = khach_hang_list.filter(tai_khoan__isnull=False)
        elif trang_thai == 'ConTrong':  # Chưa có tài khoản
            khach_hang_list = khach_hang_list.filter(tai_khoan__isnull=True)
    
    # Lấy danh sách dãy và phòng duy nhất từ tất cả phòng trong database
    unique_days = Phong.objects.values_list('DayPhong', flat=True).distinct()
    
    # Nếu đã chọn dãy, chỉ lấy số phòng của dãy đó
    if day and day != 'Tất cả':
        unique_rooms = Phong.objects.filter(DayPhong=day).values_list('SoPhong', flat=True).distinct()
    else:
        unique_rooms = Phong.objects.values_list('SoPhong', flat=True).distinct()
    
    # Chuẩn bị dữ liệu cho template
    khach_hang_data = []
    for khach_hang in khach_hang_list:
        # Lấy hợp đồng mới nhất của khách hàng
        hop_dong = HopDong.objects.filter(
            KhachHangID=khach_hang
        ).order_by('-NgayTaoHopDong').first()
        
        # Thêm thông tin khách hàng vào danh sách
        khach_hang_info = {
            'khach_hang_id': khach_hang.KhachHangID,
            'ho_ten': khach_hang.HoTenKhachHang,
            'so_dien_thoai': khach_hang.SoDienThoai,
            'DiaChiCuThe': khach_hang.DiaChiCuThe,
            'TinhThanh': khach_hang.TinhThanh,
            'QuanHuyen': khach_hang.QuanHuyen,
            'PhuongXa': khach_hang.PhuongXa,
            'has_account': hasattr(khach_hang, 'tai_khoan')
        }
        
        # Thêm thông tin phòng nếu có hợp đồng
        if hop_dong:
            khach_hang_info.update({
                'day_phong': hop_dong.DayPhong,
                'so_phong': hop_dong.PhongID.SoPhong,
                'dia_chi': hop_dong.PhongID.MoTaPhong
            })
        else:
            # Nếu không có hợp đồng, thêm giá trị mặc định
            khach_hang_info.update({
                'day_phong': 'Chưa có',
                'so_phong': 'Chưa có',
                'dia_chi': 'Chưa có'
            })
        
        khach_hang_data.append(khach_hang_info)
    
    context = {
        'khach_hang_list': khach_hang_data,
        'unique_days': sorted(unique_days),
        'unique_rooms': sorted(unique_rooms),
        'ho_ten_quan_li': ho_ten_quan_li,
        'search_query': search_query,
        'day': day,
        'so_phong': so_phong,
        'trang_thai': trang_thai
    }
    
    return render(request, 'HTML/quanlykhachhang.html', context)

def doanh_thu(request):
    # Get the current month and year
    current_month = timezone.now().month
    current_year = timezone.now().year

    # Initialize lists to hold monthly data
    monthly_revenue = []
    monthly_expenses = []

    # Loop through each month to gather historical data for the current year
    for m in range(1, 13):  # Loop through each month
        total_revenue = ChiSoDienNuoc.objects.filter(
            ThangNam=f"{m:02d}/{current_year}"
        ).aggregate(Sum('TongTien'))['TongTien__sum'] or 0

        total_expenses = 0
        chi_so_list = ChiSoDienNuoc.objects.filter(
            ThangNam=f"{m:02d}/{current_year}"
        )
        
        for chi_so in chi_so_list:
            if chi_so.TongDichVu:
                expenses = chi_so.TongDichVu - (chi_so.GiaDienMoi * chi_so.SoDienDaTieuThu + chi_so.GiaNuocMoi * chi_so.SoNuocDaTieuThu)
                total_expenses += expenses if expenses > 0 else 0  # Only add positive expenses

        monthly_revenue.append(float(total_revenue))  # Convert to float
        monthly_expenses.append(float(total_expenses))  # Convert to float

    # Get current month's revenue and expenses
    current_total_revenue = monthly_revenue[current_month - 1] if monthly_revenue else 0
    current_total_expenses = monthly_expenses[current_month - 1] if monthly_expenses else 0

    # Calculate total debt for the current month
    total_debt = ChiSoDienNuoc.objects.filter(
        ThangNam=f"{current_month:02d}/{current_year}"
    ).aggregate(Sum('TienNo'))['TienNo__sum'] or 0

    # Calculate yearly revenue and expenses for the last 7 years
    yearly_revenue = []
    yearly_expenses = []
    years = list(range(current_year - 6, current_year + 1))  # 7 years including current year (e.g., 2019-2025)

    for year in years:
        # Calculate total revenue for the year
        total_revenue_year = ChiSoDienNuoc.objects.filter(
            ThangNam__endswith=f"/{year}"
        ).aggregate(Sum('TongTien'))['TongTien__sum'] or 0

        # Calculate total expenses for the year
        total_expenses_year = 0
        chi_so_list_year = ChiSoDienNuoc.objects.filter(
            ThangNam__endswith=f"/{year}"
        )
        
        for chi_so in chi_so_list_year:
            if chi_so.TongDichVu:
                expenses = chi_so.TongDichVu - (chi_so.GiaDienMoi * chi_so.SoDienDaTieuThu + chi_so.GiaNuocMoi * chi_so.SoNuocDaTieuThu)
                total_expenses_year += expenses if expenses > 0 else 0

        yearly_revenue.append(float(total_revenue_year) / 1000000)  # Convert to millions for display
        yearly_expenses.append(float(total_expenses_year) / 1000000)  # Convert to millions for display

    context = {
        'monthly_revenue': json.dumps(monthly_revenue),  # Monthly data for bar charts
        'monthly_expenses': json.dumps(monthly_expenses),
        'current_total_revenue': current_total_revenue,
        'current_total_expenses': current_total_expenses,
        'total_debt': float(total_debt),
        'month': current_month,
        'year': current_year,
        'yearly_revenue': json.dumps(yearly_revenue),  # Yearly data for line chart
        'yearly_expenses': json.dumps(yearly_expenses),
        'years': json.dumps(years),  # List of years for labels
    }
    
    return render(request, 'HTML/doanhthu.html', context)

def dich_vu(request):
    # Lấy tất cả dịch vụ từ database
    services = DichVu.objects.all()
    
    # Lấy tên quản lý từ session
    ho_ten_quan_li = request.session.get('ho_ten_quan_li', '')
    
    # Get electricity and water prices from GiaDienNuoc model
    dien_price_record = GiaDienNuoc.objects.filter(LoaiDichVu='Dien').order_by('-NgayCapNhat').first()
    nuoc_price_record = GiaDienNuoc.objects.filter(LoaiDichVu='Nuoc').order_by('-NgayCapNhat').first()
    
    # Get prices from new model or fallback to DichVu
    if dien_price_record:
        dien_price = dien_price_record.GiaMoi
        dien_price_old = dien_price_record.GiaCu
    else:
        # Fallback to DichVu
        dien_service = DichVu.objects.filter(TenDichVu='Điện').first()
        dien_price = dien_service.GiaDichVu if dien_service else 100000
        dien_price_old = dien_service.GiaCuDichVu if dien_service and dien_service.GiaCuDichVu else 0
    
    if nuoc_price_record:
        nuoc_price = nuoc_price_record.GiaMoi
        nuoc_price_old = nuoc_price_record.GiaCu
    else:
        # Fallback to DichVu
        nuoc_service = DichVu.objects.filter(TenDichVu='Nước').first()
        nuoc_price = nuoc_service.GiaDichVu if nuoc_service else 80000
        nuoc_price_old = nuoc_service.GiaCuDichVu if nuoc_service and nuoc_service.GiaCuDichVu else 0
    
    # Get the most recent readings for display in the service page
    recent_readings = ChiSoDienNuoc.objects.all().order_by('-ThangNam', 'DayPhong', 'PhongID__SoPhong')[:5]
    
    # Prepare readings for display
    readings_data = []
    for reading in recent_readings:
        room_info = f"{reading.DayPhong}{reading.PhongID.SoPhong}"
        data = {
            'chi_so_id': reading.ChiSoID,  # Thêm ChiSoID để sử dụng cho liên kết
            'room_info': room_info,
            'period': reading.ThangNam,
            'old_electric': reading.ChiSoDienCu,
            'new_electric': reading.ChiSoDienMoi,
            'electric_usage': reading.SoDienDaTieuThu,
            'old_water': reading.ChiSoNuocCu,
            'new_water': reading.ChiSoNuocMoi,
            'water_usage': reading.SoNuocDaTieuThu,
            'total_amount': reading.TongTien,
            'status': 'Đã thanh toán' if reading.TrangThaiThanhToan == 'Y' else 'Chưa thanh toán'
        }
        readings_data.append(data)
    
    # Get all rooms for the dropdown
    phong_list = Phong.objects.all().order_by('DayPhong', 'SoPhong')
    
    # Get current year and month for default value
    current_date = timezone.now()
    current_month_year = current_date.strftime("%m/%Y")
    
    # Lịch sử giá điện nước
    dien_price_history = GiaDienNuoc.objects.filter(LoaiDichVu='Dien').order_by('-NgayCapNhat')[:5]
    nuoc_price_history = GiaDienNuoc.objects.filter(LoaiDichVu='Nuoc').order_by('-NgayCapNhat')[:5]
    
    context = {
        'ho_ten_quan_li': ho_ten_quan_li,
        'services': services,
        'dien_price': dien_price,
        'nuoc_price': nuoc_price,
        'dien_price_old': dien_price_old,
        'nuoc_price_old': nuoc_price_old,
        'recent_readings': readings_data,
        'phong_list': phong_list,
        'current_month_year': current_month_year,
        'dien_price_history': dien_price_history,
        'nuoc_price_history': nuoc_price_history,
    }
    
    return render(request, 'HTML/dichvu.html', context)

def cap_nhat_hoa_don(request):
    # Lấy tên quản lý từ session
    ho_ten_quan_li = request.session.get('ho_ten_quan_li', '')
    
    # Lấy tham số từ URL
    phong_id = request.GET.get('phong_id')
    thang_nam = request.GET.get('thang_nam')
    chi_so_id = request.GET.get('chi_so_id')
    
    # Khởi tạo biến chứa thông tin chỉ số điện nước
    chi_so = None
    phong = None
    hop_dong = None
    khach_hang = None
    
    # Nếu có chi_so_id, ưu tiên lấy theo chi_so_id
    if chi_so_id:
        try:
            chi_so = ChiSoDienNuoc.objects.get(ChiSoID=chi_so_id)
            phong = chi_so.PhongID
            thang_nam = chi_so.ThangNam
        except ChiSoDienNuoc.DoesNotExist:
            messages.error(request, 'Không tìm thấy thông tin chỉ số điện nước!')
            return redirect('dich_vu')
    # Nếu có phong_id và thang_nam, lấy theo phong_id và thang_nam
    elif phong_id and thang_nam:
        try:
            phong = Phong.objects.get(PhongID=phong_id)
            chi_so = ChiSoDienNuoc.objects.filter(PhongID=phong, ThangNam=thang_nam).first()
        except Phong.DoesNotExist:
            messages.error(request, 'Không tìm thấy thông tin phòng!')
            return redirect('dich_vu')
    
    # Nếu không có thông tin chi_so, chuyển hướng về trang dịch vụ
    if not chi_so and not phong:
        messages.error(request, 'Vui lòng chọn phòng và tháng năm để cập nhật hóa đơn!')
        return redirect('dich_vu')
    
    # Nếu không có chi_so nhưng có phòng, lấy giá điện nước mới nhất
    if not chi_so and phong:
        # Lấy giá điện nước mới nhất từ bảng GiaDienNuoc
        dien_price_record = GiaDienNuoc.objects.filter(LoaiDichVu='Dien').order_by('-NgayCapNhat').first()
        nuoc_price_record = GiaDienNuoc.objects.filter(LoaiDichVu='Nuoc').order_by('-NgayCapNhat').first()
        
        gia_dien = dien_price_record.GiaMoi if dien_price_record else 0
        gia_nuoc = nuoc_price_record.GiaMoi if nuoc_price_record else 0
        
        # Lấy chỉ số cũ từ tháng trước (nếu có)
        thang, nam = thang_nam.split('/')
        thang = int(thang)
        nam = int(nam)
        
        # Tính tháng trước
        thang_truoc = thang - 1
        nam_truoc = nam
        if thang_truoc == 0:
            thang_truoc = 12
            nam_truoc = nam - 1
        
        thang_nam_truoc = f"{thang_truoc:02d}/{nam_truoc}"
        
        # Lấy chỉ số của tháng trước
        chi_so_thang_truoc = ChiSoDienNuoc.objects.filter(
            PhongID=phong, 
            ThangNam=thang_nam_truoc
        ).first()
        
        # Tạo đối tượng chi_so mới (chưa lưu vào DB)
        chi_so = ChiSoDienNuoc(
            PhongID=phong,
            DayPhong=phong.DayPhong,
            ThangNam=thang_nam,
            ChiSoDienCu=chi_so_thang_truoc.ChiSoDienMoi if chi_so_thang_truoc else 0,
            ChiSoDienMoi=0,
            ChiSoNuocCu=chi_so_thang_truoc.ChiSoNuocMoi if chi_so_thang_truoc else 0,
            ChiSoNuocMoi=0,
            GiaDienMoi=gia_dien,
            GiaNuocMoi=gia_nuoc,
            TienPhong=phong.GiaPhong
        )
    
    # Lấy thông tin khách hàng (nếu có)
    if phong:
        hop_dong = HopDong.objects.filter(PhongID=phong, TrangThaiHopDong='HoatDong').first()
        if hop_dong:
            khach_hang = hop_dong.KhachHangID
    
    # Chuẩn bị context để hiển thị trên trang
    context = {
        'ho_ten_quan_li': ho_ten_quan_li,
        'chi_so': chi_so,
        'phong': phong or chi_so.PhongID,
        'hop_dong': hop_dong,
        'khach_hang': khach_hang,
        'thang_nam': thang_nam or chi_so.ThangNam
    }
    
    if request.method == 'POST':
        try:
            # Lấy dữ liệu từ form
            chi_so_dien_moi = request.POST.get('chi_so_dien_moi')
            chi_so_nuoc_moi = request.POST.get('chi_so_nuoc_moi')
            ten_phi_sua_chua = request.POST.get('ten_phi_sua_chua')
            tien_phi_sua_chua = request.POST.get('tien_phi_sua_chua', 0)
            
            # Cập nhật hoặc tạo mới record chỉ số điện nước
            if chi_so.ChiSoID:  # Đã có record
                chi_so.ChiSoDienMoi = int(chi_so_dien_moi) if chi_so_dien_moi else 0
                chi_so.ChiSoNuocMoi = int(chi_so_nuoc_moi) if chi_so_nuoc_moi else 0
                chi_so.SoDienDaTieuThu = int(chi_so.ChiSoDienMoi) - int(chi_so.ChiSoDienCu)
                chi_so.SoNuocDaTieuThu = int(chi_so.ChiSoNuocMoi) - int(chi_so.ChiSoNuocCu)
                
                # Tính tổng tiền
                tong_tien_dien = chi_so.SoDienDaTieuThu * chi_so.GiaDienMoi
                tong_tien_nuoc = chi_so.SoNuocDaTieuThu * chi_so.GiaNuocMoi
                chi_so.TongDichVu = tong_tien_dien + tong_tien_nuoc
                
                if ten_phi_sua_chua and tien_phi_sua_chua:
                    chi_so.TongDichVu += int(tien_phi_sua_chua)
                
                chi_so.TongTien = chi_so.TienPhong + chi_so.TongDichVu
                chi_so.save()
                
                messages.success(request, f'Cập nhật hóa đơn phòng {chi_so.PhongID.DayPhong}{chi_so.PhongID.SoPhong} tháng {chi_so.ThangNam} thành công!')
            else:  # Tạo mới
                # Lấy phòng
                phong = Phong.objects.get(PhongID=phong.PhongID)
                
                # Chuyển đổi dữ liệu nhập vào thành số nguyên
                chi_so_dien_moi_int = int(chi_so_dien_moi) if chi_so_dien_moi else 0 
                chi_so_nuoc_moi_int = int(chi_so_nuoc_moi) if chi_so_nuoc_moi else 0
                chi_so_dien_cu_int = int(chi_so.ChiSoDienCu) if chi_so.ChiSoDienCu else 0
                chi_so_nuoc_cu_int = int(chi_so.ChiSoNuocCu) if chi_so.ChiSoNuocCu else 0
                
                # Tính toán tiêu thụ và tổng tiền
                so_dien_tieu_thu = chi_so_dien_moi_int - chi_so_dien_cu_int
                so_nuoc_tieu_thu = chi_so_nuoc_moi_int - chi_so_nuoc_cu_int
                tong_tien_dien = so_dien_tieu_thu * chi_so.GiaDienMoi
                tong_tien_nuoc = so_nuoc_tieu_thu * chi_so.GiaNuocMoi
                tong_dich_vu = tong_tien_dien + tong_tien_nuoc
                
                if ten_phi_sua_chua and tien_phi_sua_chua:
                    tong_dich_vu += int(tien_phi_sua_chua)
                
                # Tạo record chỉ số điện nước mới
                chi_so_moi = ChiSoDienNuoc.objects.create(
                    PhongID=phong,
                    DayPhong=phong.DayPhong,
                    ThangNam=thang_nam,
                    ChiSoDienCu=chi_so_dien_cu_int,
                    ChiSoDienMoi=chi_so_dien_moi_int,
                    ChiSoNuocCu=chi_so_nuoc_cu_int,
                    ChiSoNuocMoi=chi_so_nuoc_moi_int,
                    SoDienDaTieuThu=so_dien_tieu_thu,
                    SoNuocDaTieuThu=so_nuoc_tieu_thu,
                    GiaDienCu=chi_so.GiaDienCu,
                    GiaDienMoi=chi_so.GiaDienMoi,
                    GiaNuocCu=chi_so.GiaNuocCu,
                    GiaNuocMoi=chi_so.GiaNuocMoi,
                    TienPhong=phong.GiaPhong,
                    TongDichVu=tong_dich_vu,
                    TongTien=phong.GiaPhong + tong_dich_vu,
                    TrangThaiThanhToan='N'  # 'N' for Not paid
                )
                
                messages.success(request, f'Tạo mới hóa đơn phòng {phong.DayPhong}{phong.SoPhong} tháng {thang_nam} thành công!')
            
            return redirect('dich_vu')
            
        except Exception as e:
            print(f"Error in cap_nhat_hoa_don: {str(e)}")
            messages.error(request, f'Có lỗi xảy ra: {str(e)}')
            return render(request, 'HTML/capnhathoadon.html', context)
    
    return render(request, 'HTML/capnhathoadon.html', context)

def hoa_don(request):
    # Lấy tên quản lý từ session
    ho_ten_quan_li = request.session.get('ho_ten_quan_li', '')
    
    # Lấy các chỉ số điện nước (hóa đơn) từ database
    chi_so_list = ChiSoDienNuoc.objects.select_related('PhongID').order_by('-ThangNam')
    
    # Lấy thông tin khách hàng cho mỗi phòng
    hoa_don_data = []
    for chi_so in chi_so_list:
        # Lấy hợp đồng hiện tại của phòng (nếu có)
        hop_dong = HopDong.objects.filter(
            PhongID=chi_so.PhongID, 
            TrangThaiHopDong='HoatDong'
        ).select_related('KhachHangID').first()
        
        # Lấy thông tin người thuê
        khach_hang = None
        if hop_dong:
            khach_hang = hop_dong.KhachHangID
        
        # Tạo thông tin hóa đơn
        hoa_don_info = {
            'chi_so_id': chi_so.ChiSoID,
            'phong_id': chi_so.PhongID.PhongID,
            'day_phong': chi_so.DayPhong,
            'so_phong': chi_so.PhongID.SoPhong,
            'thang_nam': chi_so.ThangNam,
            'ten_khach_hang': khach_hang.HoTenKhachHang if khach_hang else 'Chưa có',
            'so_dien_thoai': khach_hang.SoDienThoai if khach_hang else 'Chưa có',
            'tien_dien': chi_so.SoDienDaTieuThu * chi_so.GiaDienMoi,
            'tien_nuoc': chi_so.SoNuocDaTieuThu * chi_so.GiaNuocMoi,
            'tien_phong': chi_so.TienPhong,
            'tong_tien': chi_so.TongTien,
            'tien_no': chi_so.TienNo if hasattr(chi_so, 'TienNo') and chi_so.TienNo is not None else 0,
            'tien_tra': chi_so.Tientra if hasattr(chi_so, 'Tientra') and chi_so.Tientra is not None else 0,
            'da_thanh_toan': chi_so.TrangThaiThanhToan == 'Y'
        }
        hoa_don_data.append(hoa_don_info)
    
    # Lấy danh sách dãy phòng và số phòng để hiển thị trong dropdown
    day_phong_list = Phong.objects.values_list('DayPhong', flat=True).distinct()
    so_phong_list = Phong.objects.values_list('SoPhong', flat=True).distinct()
    
    context = {
        'ho_ten_quan_li': ho_ten_quan_li,
        'hoa_don_data': hoa_don_data,
        'day_phong_list': day_phong_list,
        'so_phong_list': so_phong_list,
    }
    
    return render(request, 'HTML/hoadon.html', context)

def quan_li_hop_dong(request):
    # Fetch all contracts from the database
    hop_dong_list = HopDong.objects.select_related('PhongID', 'KhachHangID').all()
    
    # Prepare contract data for the template
    hop_dong_data = []
    for hop_dong in hop_dong_list:
        hop_dong_info = {
            'hop_dong_id': hop_dong.HopDongID,
            'day_phong': hop_dong.DayPhong,
            'so_phong': hop_dong.PhongID.SoPhong,
            'gia_phong': hop_dong.PhongID.GiaPhong,  # Sử dụng GiaPhong từ bảng Phong
            'ten_khach_hang': hop_dong.KhachHangID.HoTenKhachHang,
            'so_dien_thoai': hop_dong.KhachHangID.SoDienThoai,
            
        }
        hop_dong_data.append(hop_dong_info)
    
    context = {
        'hop_dong_list': hop_dong_data
    }
    return render(request, 'HTML/quanlihopdong.html', context)

def tao_tai_khoan(request, khach_hang_id):
    try:
        khach_hang = KhachHang.objects.get(KhachHangID=khach_hang_id)
        # Lấy thông tin phòng từ hợp đồng đang hoạt động
        hop_dong = HopDong.objects.filter(
            KhachHangID=khach_hang,
            TrangThaiHopDong='HoatDong'
        ).first()
        
        if request.method == 'POST':
            # Lấy thông tin từ form
            email = request.POST.get('email')
            so_dien_thoai = request.POST.get('so_dien_thoai')
            mat_khau = request.POST.get('mat_khau')
            
            # Tạo tài khoản mới
            try:
                tai_khoan = TaiKhoan.objects.create(
                    KhachHangID=khach_hang,
                    TenDangNhap=so_dien_thoai,  # Sử dụng số điện thoại làm tên đăng nhập
                    Email=email,  # Save the email
                    MatKhau=mat_khau
                )
                
                messages.success(request, 'Tạo tài khoản thành công!')
                return redirect('quan_ly_khach_hang')
            except Exception as e:
                messages.error(request, f'Lỗi khi tạo tài khoản: {str(e)}')
                return redirect('tao_tai_khoan', khach_hang_id=khach_hang_id)
        
        context = {
            'khach_hang': khach_hang,
            'hop_dong': hop_dong,
            'ho_ten_quan_li': request.session.get('ho_ten_quan_li', '')
        }
        return render(request, 'HTML/taotaikhoan.html', context)
        
    except KhachHang.DoesNotExist:
        messages.error(request, 'Không tìm thấy khách hàng!')
        return redirect('quan_ly_khach_hang')

def chinh_sua_tai_khoan(request, khach_hang_id):
    try:
        khach_hang = KhachHang.objects.get(KhachHangID=khach_hang_id)
        tai_khoan = TaiKhoan.objects.get(KhachHangID=khach_hang)
        # Fetch room information from the active contract
        hop_dong = HopDong.objects.filter(
            KhachHangID=khach_hang,
            TrangThaiHopDong='HoatDong'
        ).first()
        
        if request.method == 'POST':
            # Get information from the form
            email = request.POST.get('email')
            so_dien_thoai = request.POST.get('so_dien_thoai')
            mat_khau = request.POST.get('mat_khau')
            
            # Update account information
            tai_khoan.TenDangNhap = so_dien_thoai
            tai_khoan.Email = email
            tai_khoan.MatKhau = mat_khau
            tai_khoan.save()
            
            messages.success(request, 'Cập nhật tài khoản thành công!')
            return redirect('quan_ly_khach_hang')
        
        context = {
            'khach_hang': khach_hang,
            'tai_khoan': tai_khoan,
            'hop_dong': hop_dong,
            'ho_ten_quan_li': request.session.get('ho_ten_quan_li', '')
        }
        return render(request, 'HTML/chinhsua_tk.html', context)
        
    except KhachHang.DoesNotExist:
        messages.error(request, 'Không tìm thấy khách hàng!')
        return redirect('quan_ly_khach_hang')
    except TaiKhoan.DoesNotExist:
        messages.error(request, 'Không tìm thấy tài khoản!')
        return redirect('quan_ly_khach_hang')

def cap_nhat_dich_vu(request):
    if request.method == 'POST':
        try:
            # Get service information from the form
            ten_dich_vu = request.POST.get('ten_dich_vu')
            gia_dich_vu = request.POST.get('gia_dich_vu')
            service_id = request.POST.get('service_id', '')
            
            # Debug output
            print(f"Request data: ten_dich_vu={ten_dich_vu}, gia_dich_vu={gia_dich_vu}, service_id={service_id}")
            
            # Convert price to integer
            try:
                # First convert to float to handle any decimal input, then convert to int
                gia_dich_vu = int(float(gia_dich_vu))
                if gia_dich_vu <= 0:
                    messages.error(request, 'Giá dịch vụ phải lớn hơn 0!')
                    return redirect('dich_vu')
            except (ValueError, TypeError):
                messages.error(request, 'Giá dịch vụ không hợp lệ!')
                return redirect('dich_vu')
            
            # Check if we're updating an existing service or creating a new one
            if service_id:
                # Updating existing service
                try:
                    dich_vu = DichVu.objects.get(DichVuID=service_id)
                    print(f"Before update: GiaDichVu={dich_vu.GiaDichVu}, GiaCuDichVu={dich_vu.GiaCuDichVu}")
                    
                    # Save old price before updating
                    dich_vu.GiaCuDichVu = dich_vu.GiaDichVu
                    dich_vu.GiaDichVu = gia_dich_vu
                    dich_vu.TenDichVu = ten_dich_vu
                    dich_vu.save()
                    
                    print(f"After update: GiaDichVu={dich_vu.GiaDichVu}, GiaCuDichVu={dich_vu.GiaCuDichVu}")
                    messages.success(request, f'Cập nhật dịch vụ "{ten_dich_vu}" thành công!')
                except DichVu.DoesNotExist:
                    messages.error(request, f'Không tìm thấy dịch vụ có ID: {service_id}')
            else:
                # Creating new service
                dich_vu = DichVu.objects.create(
                    TenDichVu=ten_dich_vu,
                    GiaDichVu=gia_dich_vu,
                    GiaCuDichVu=0  # Initialize old price as 0 for new services
                )
                print(f"New service created: GiaDichVu={dich_vu.GiaDichVu}, GiaCuDichVu={dich_vu.GiaCuDichVu}")
                messages.success(request, f'Thêm dịch vụ mới "{ten_dich_vu}" thành công!')
            
            return redirect('dich_vu')
        
        except Exception as e:
            print(f"Error in cap_nhat_dich_vu: {str(e)}")
            messages.error(request, f'Có lỗi xảy ra: {str(e)}')
            return redirect('dich_vu')
    
    # If GET request, redirect to the services page
    return redirect('dich_vu')

def xoa_dich_vu(request, dich_vu_id):
    try:
        # Find the service by ID
        dich_vu = DichVu.objects.get(DichVuID=dich_vu_id)
        ten_dich_vu = dich_vu.TenDichVu
        
        # Delete the service
        dich_vu.delete()
        
        messages.success(request, f'Đã xóa dịch vụ "{ten_dich_vu}" thành công!')
    except DichVu.DoesNotExist:
        messages.error(request, f'Không tìm thấy dịch vụ với ID {dich_vu_id}!')
    except Exception as e:
        messages.error(request, f'Có lỗi xảy ra khi xóa dịch vụ: {str(e)}')
    
    return redirect('dich_vu')

def cap_nhat_gia_dien_nuoc(request):
    if request.method == 'POST':
        try:
            # Get service information from the form
            loai_dich_vu = request.POST.get('loai_dich_vu')
            gia_moi = request.POST.get('gia_moi')
            
            # Validate loai_dich_vu
            if not loai_dich_vu or loai_dich_vu not in ['Dien', 'Nuoc']:
                messages.error(request, 'Loại dịch vụ không hợp lệ! Chỉ hỗ trợ Dien hoặc Nuoc.')
                return redirect('dich_vu')
            
            # Convert price to integer
            try:
                gia_moi = int(float(gia_moi))
                if gia_moi <= 0:
                    messages.error(request, 'Giá phải lớn hơn 0!')
                    return redirect('dich_vu')
            except (ValueError, TypeError):
                messages.error(request, 'Giá không hợp lệ!')
                return redirect('dich_vu')
            
            # Get the current price
            gia_cu = GiaDienNuoc.objects.filter(LoaiDichVu=loai_dich_vu).order_by('-NgayCapNhat').first()
            
            # Create a new record with the updated price
            GiaDienNuoc.objects.create(
                LoaiDichVu=loai_dich_vu,
                GiaCu=gia_cu.GiaMoi if gia_cu else 0,
                GiaMoi=gia_moi
            )
            
            # Update in DichVu table for backward compatibility
            if loai_dich_vu == 'Dien':
                dich_vu = DichVu.objects.filter(TenDichVu='Điện').first()
                if dich_vu:
                    dich_vu.GiaCuDichVu = dich_vu.GiaDichVu
                    dich_vu.GiaDichVu = gia_moi
                    dich_vu.save()
            elif loai_dich_vu == 'Nuoc':
                dich_vu = DichVu.objects.filter(TenDichVu='Nước').first()
                if dich_vu:
                    dich_vu.GiaCuDichVu = dich_vu.GiaDichVu
                    dich_vu.GiaDichVu = gia_moi
                    dich_vu.save()
            
            ten_dich_vu = 'Điện' if loai_dich_vu == 'Dien' else 'Nước'
            messages.success(request, f'Cập nhật giá {ten_dich_vu} thành công!')
        except Exception as e:
            messages.error(request, f'Có lỗi xảy ra: {str(e)}')
    
    return redirect('dich_vu')

def cap_nhat_chi_so_dien_nuoc(request):
    # Lấy tên quản lý từ session
    ho_ten_quan_li = request.session.get('ho_ten_quan_li', '')
    
    # Get all rooms
    phong_list = Phong.objects.all().order_by('DayPhong', 'SoPhong')
    
    if request.method == 'POST':
        try:
            phong_id = request.POST.get('phong_id')
            thang_nam = request.POST.get('thang_nam')
            chi_so_dien_cu = request.POST.get('chi_so_dien_cu', '0')
            chi_so_dien_moi = request.POST.get('chi_so_dien_moi', '0')
            chi_so_nuoc_cu = request.POST.get('chi_so_nuoc_cu', '0')
            chi_so_nuoc_moi = request.POST.get('chi_so_nuoc_moi', '0')
            
            # Validate data
            if not phong_id or not thang_nam:
                messages.error(request, 'Vui lòng chọn phòng và tháng năm')
                return redirect('dich_vu')
            
            try:
                phong = Phong.objects.get(PhongID=phong_id)
            except Phong.DoesNotExist:
                messages.error(request, 'Phòng không tồn tại')
                return redirect('dich_vu')
            
            # Convert inputs to integers
            try:
                chi_so_dien_cu = int(chi_so_dien_cu)
                chi_so_dien_moi = int(chi_so_dien_moi)
                chi_so_nuoc_cu = int(chi_so_nuoc_cu)
                chi_so_nuoc_moi = int(chi_so_nuoc_moi)
                
                # Validate new readings are not less than old readings
                if chi_so_dien_moi < chi_so_dien_cu:
                    messages.error(request, 'Chỉ số điện mới không thể nhỏ hơn chỉ số cũ')
                    return redirect('dich_vu')
                
                if chi_so_nuoc_moi < chi_so_nuoc_cu:
                    messages.error(request, 'Chỉ số nước mới không thể nhỏ hơn chỉ số cũ')
                    return redirect('dich_vu')
                
            except (ValueError, TypeError):
                messages.error(request, 'Chỉ số điện nước phải là số nguyên')
                return redirect('dich_vu')
            
            # Calculate consumption
            so_dien_tieu_thu = chi_so_dien_moi - chi_so_dien_cu
            so_nuoc_tieu_thu = chi_so_nuoc_moi - chi_so_nuoc_cu
            
            # Get electricity and water prices from GiaDienNuoc model
            dien_price_record = GiaDienNuoc.objects.filter(LoaiDichVu='Dien').order_by('-NgayCapNhat').first()
            nuoc_price_record = GiaDienNuoc.objects.filter(LoaiDichVu='Nuoc').order_by('-NgayCapNhat').first()
            
            # Get prices from new model or fallback to DichVu
            if dien_price_record:
                gia_dien = dien_price_record.GiaMoi
                gia_dien_cu = dien_price_record.GiaCu
            else:
                # Fallback to DichVu
                dien_service = DichVu.objects.filter(TenDichVu='Điện').first()
                gia_dien = dien_service.GiaDichVu if dien_service else 100000
                gia_dien_cu = dien_service.GiaCuDichVu if dien_service and dien_service.GiaCuDichVu else 0
            
            if nuoc_price_record:
                gia_nuoc = nuoc_price_record.GiaMoi
                gia_nuoc_cu = nuoc_price_record.GiaCu
            else:
                # Fallback to DichVu
                nuoc_service = DichVu.objects.filter(TenDichVu='Nước').first()
                gia_nuoc = nuoc_service.GiaDichVu if nuoc_service else 80000
                gia_nuoc_cu = nuoc_service.GiaCuDichVu if nuoc_service and nuoc_service.GiaCuDichVu else 0
            
            # Calculate total costs
            tong_tien_dien = so_dien_tieu_thu * gia_dien
            tong_tien_nuoc = so_nuoc_tieu_thu * gia_nuoc
            
            # Get room price for this room
            gia_phong = phong.GiaPhong
            
            # Check if record already exists for this room and month
            chi_so, created = ChiSoDienNuoc.objects.get_or_create(
                PhongID=phong,
                DayPhong=phong.DayPhong,
                ThangNam=thang_nam,
                defaults={
                    'ChiSoDienCu': chi_so_dien_cu,
                    'ChiSoDienMoi': chi_so_dien_moi,
                    'ChiSoNuocCu': chi_so_nuoc_cu,
                    'ChiSoNuocMoi': chi_so_nuoc_moi,
                    'SoDienDaTieuThu': so_dien_tieu_thu,
                    'SoNuocDaTieuThu': so_nuoc_tieu_thu,
                    'GiaDienCu': gia_dien_cu,
                    'GiaDienMoi': gia_dien,
                    'GiaNuocCu': gia_nuoc_cu,
                    'GiaNuocMoi': gia_nuoc,
                    'TienPhong': gia_phong,
                    'TongDichVu': tong_tien_dien + tong_tien_nuoc,
                    'TongTien': gia_phong + tong_tien_dien + tong_tien_nuoc,
                    'TrangThaiThanhToan': 'N'  # 'N' for Not paid
                }
            )
            
            if not created:
                # Update existing record
                chi_so.ChiSoDienCu = chi_so_dien_cu
                chi_so.ChiSoDienMoi = chi_so_dien_moi
                chi_so.ChiSoNuocCu = chi_so_nuoc_cu
                chi_so.ChiSoNuocMoi = chi_so_nuoc_moi
                chi_so.SoDienDaTieuThu = so_dien_tieu_thu
                chi_so.SoNuocDaTieuThu = so_nuoc_tieu_thu
                chi_so.GiaDienCu = gia_dien_cu
                chi_so.GiaDienMoi = gia_dien
                chi_so.GiaNuocCu = gia_nuoc_cu
                chi_so.GiaNuocMoi = gia_nuoc
                chi_so.TienPhong = gia_phong
                chi_so.TongDichVu = tong_tien_dien + tong_tien_nuoc
                chi_so.TongTien = gia_phong + tong_tien_dien + tong_tien_nuoc
                chi_so.save()
                messages.success(request, f'Cập nhật chỉ số điện nước cho phòng {phong.DayPhong}{phong.SoPhong} tháng {thang_nam} thành công!')
            else:
                messages.success(request, f'Thêm mới chỉ số điện nước cho phòng {phong.DayPhong}{phong.SoPhong} tháng {thang_nam} thành công!')
            
            return redirect('dich_vu')
            
        except Exception as e:
            print(f"Error in cap_nhat_chi_so_dien_nuoc: {str(e)}")
            messages.error(request, f'Có lỗi xảy ra: {str(e)}')
            return redirect('dich_vu')
    
    # Nếu đây là GET request, chuyển hướng người dùng đến trang dịch vụ
    return redirect('dich_vu')

def xoa_chi_so_dien_nuoc(request, chi_so_id):
    try:
        # Find the record by ID
        chi_so = ChiSoDienNuoc.objects.get(ChiSoID=chi_so_id)
        
        # Save info for success message
        room_info = f"{chi_so.DayPhong}{chi_so.PhongID.SoPhong}" if chi_so.PhongID else "Unknown"
        period = chi_so.ThangNam
        
        # Delete the record
        chi_so.delete()
        
        messages.success(request, f'Đã xóa bản ghi điện nước của phòng {room_info} tháng {period} thành công!')
    except ChiSoDienNuoc.DoesNotExist:
        messages.error(request, f'Không tìm thấy bản ghi với ID {chi_so_id}!')
    except Exception as e:
        messages.error(request, f'Có lỗi xảy ra khi xóa bản ghi: {str(e)}')
    
    return redirect('dich_vu')

def xoa_gia_dien_nuoc(request, gia_id):
    try:
        # Find the record by ID
        gia = GiaDienNuoc.objects.get(GiaID=gia_id)
        
        # Save info for success message
        loai_dich_vu = "Điện" if gia.LoaiDichVu == "Dien" else "Nước"
        
        # Delete the record
        gia.delete()
        
        messages.success(request, f'Đã xóa bản ghi giá {loai_dich_vu} thành công!')
    except GiaDienNuoc.DoesNotExist:
        messages.error(request, f'Không tìm thấy bản ghi giá với ID {gia_id}!')
    except Exception as e:
        messages.error(request, f'Có lỗi xảy ra khi xóa bản ghi giá: {str(e)}')
    
    return redirect('dich_vu')

def process_payment(request, chi_so_id):
    """
    Xử lý thanh toán hóa đơn
    """
    if request.method != 'POST':
        messages.error(request, 'Phương thức không được hỗ trợ!')
        return redirect('hoa_don')
    
    try:
        # Lấy chi số điện nước
        chi_so = ChiSoDienNuoc.objects.get(ChiSoID=chi_so_id)
        
        # Debug: In ra thông tin trước khi cập nhật
        print(f"BEFORE UPDATE - ID: {chi_so.ChiSoID}, TienNo: {chi_so.TienNo}, Tientra: {chi_so.Tientra}")
        
        # Lấy phòng và tháng để hiển thị thông báo
        phong_info = f"{chi_so.DayPhong}{chi_so.PhongID.SoPhong}"
        thang_nam = chi_so.ThangNam
        
        # Lấy trạng thái thanh toán
        payment_status = request.POST.get('payment_status')
        
        if payment_status == 'completed':
            # Thanh toán đầy đủ
            chi_so.TrangThaiThanhToan = 'Y'  # Y = Đã thanh toán
            chi_so.TienNo = Decimal('0')  # Đặt tiền nợ về 0 khi thanh toán đầy đủ
            chi_so.Tientra = chi_so.TongTien  # Ghi nhận đã trả toàn bộ số tiền
            
            # Debug: In ra thông tin trước khi lưu
            print(f"COMPLETED PAYMENT - Setting TienNo: {chi_so.TienNo}, Tientra: {chi_so.Tientra}")
            
            try:
                chi_so.save()
                print(f"SAVE SUCCESS - ID: {chi_so.ChiSoID}")
            except Exception as save_error:
                print(f"SAVE ERROR: {str(save_error)}")
                # Try to save with force_update
                ChiSoDienNuoc.objects.filter(ChiSoID=chi_so_id).update(
                    TrangThaiThanhToan='Y',
                    TienNo=Decimal('0'),
                    Tientra=chi_so.TongTien
                )
                print("ATTEMPTED DIRECT UPDATE")
            
            # Verify data was saved
            chi_so_after = ChiSoDienNuoc.objects.get(ChiSoID=chi_so_id)
            print(f"AFTER SAVE - TienNo: {chi_so_after.TienNo}, Tientra: {chi_so_after.Tientra}")
            
            messages.success(request, f'Hóa đơn phòng {phong_info} tháng {thang_nam} đã được thanh toán đầy đủ!')
        elif payment_status == 'pending':
            # Thanh toán một phần
            paid_amount = request.POST.get('paid_amount')
            due_date = request.POST.get('due_date')
            
            if not paid_amount or not due_date:
                messages.error(request, 'Vui lòng nhập đầy đủ số tiền đã thanh toán và hạn trả!')
                return redirect('hoa_don')
            
            # Tính toán số tiền còn nợ
            paid_amount = Decimal(str(float(paid_amount)))  # Convert to Decimal for accuracy
            
            # Lấy số tiền đã trả trước đó (nếu có)
            current_paid = chi_so.Tientra if chi_so.Tientra is not None else Decimal('0')
            
            # Debug: In ra giá trị
            print(f"PARTIAL PAYMENT - Current paid: {current_paid}, New payment: {paid_amount}")
            
            # Tính tổng số tiền đã trả (trước đó + hiện tại)
            total_paid = current_paid + paid_amount
            
            # Tính số tiền còn nợ
            total_amount = chi_so.TongTien
            remaining_amount = total_amount - total_paid
            
            # Debug: In ra các giá trị tính toán
            print(f"CALCULATION - Total paid: {total_paid}, Total amount: {total_amount}, Remaining: {remaining_amount}")
                
            # Cập nhật trạng thái thanh toán
            if remaining_amount <= 0:
                # Nếu đã thanh toán đủ, cập nhật trạng thái thành đã thanh toán
                chi_so.TrangThaiThanhToan = 'Y'
                chi_so.TienNo = Decimal('0')
                messages.success(request, f'Hóa đơn phòng {phong_info} tháng {thang_nam} đã được thanh toán đầy đủ!')
            else:
                # Vẫn còn nợ
                chi_so.TienNo = remaining_amount
                chi_so.TrangThaiThanhToan = 'N'
                messages.success(request, f'Hóa đơn phòng {phong_info} tháng {thang_nam} đã được thanh toán một phần. Đã trả: {total_paid:,.0f} VNĐ, Còn nợ: {remaining_amount:,.0f} VNĐ')
            
            # Cập nhật tổng số tiền đã trả
            chi_so.Tientra = total_paid
            
            # Debug: In ra thông tin trước khi lưu
            print(f"BEFORE SAVE - Setting TienNo: {chi_so.TienNo}, Tientra: {chi_so.Tientra}")
            
            try:
                chi_so.save()
                print(f"SAVE SUCCESS - ID: {chi_so.ChiSoID}")
            except Exception as save_error:
                print(f"SAVE ERROR: {str(save_error)}")
                # Try direct update via QuerySet
                ChiSoDienNuoc.objects.filter(ChiSoID=chi_so_id).update(
                    TrangThaiThanhToan=chi_so.TrangThaiThanhToan,
                    TienNo=chi_so.TienNo,
                    Tientra=chi_so.Tientra,
                )
                print("ATTEMPTED DIRECT UPDATE")
            
            # Verify data was saved
            chi_so_after = ChiSoDienNuoc.objects.get(ChiSoID=chi_so_id)
            print(f"AFTER SAVE - TienNo: {chi_so_after.TienNo}, Tientra: {chi_so_after.Tientra}")
        else:
            messages.error(request, 'Trạng thái thanh toán không hợp lệ!')
    
    except ChiSoDienNuoc.DoesNotExist:
        messages.error(request, f'Không tìm thấy hóa đơn với ID {chi_so_id}!')
    except Exception as e:
        print(f"ERROR IN PROCESS_PAYMENT: {str(e)}")
        messages.error(request, f'Có lỗi xảy ra khi xử lý thanh toán: {str(e)}')
    
    return redirect('hoa_don')

def xem_hoa_don(request, chi_so_id):
    # Lấy chi số điện nước
    chi_so = get_object_or_404(ChiSoDienNuoc, ChiSoID=chi_so_id)
    
    # Lấy thông tin hợp đồng từ phòng
    hop_dong = HopDong.objects.filter(PhongID=chi_so.PhongID, TrangThaiHopDong='HoatDong').first()
    
    # Lấy thông tin hóa đơn
    hoa_don_info = {
        'chi_so_id': chi_so.ChiSoID,
        'day_phong': chi_so.DayPhong,
        'so_phong': chi_so.PhongID.SoPhong,
        'ten_khach_hang': hop_dong.KhachHangID.HoTenKhachHang if hop_dong else 'Chưa có',
        'so_dien_thoai': hop_dong.KhachHangID.SoDienThoai if hop_dong else 'Chưa có',
        'tong_tien': chi_so.TongTien,
        'tien_no': chi_so.TienNo,
        'tien_tra': chi_so.Tientra,
        'da_thanh_toan': chi_so.TrangThaiThanhToan == 'Y',
        'ngay_thu': timezone.now().strftime('%d/%m/%Y'),  # Ngày thu
        'ngay_vao': hop_dong.NgayBatDau.strftime('%d/%m/%Y') if hop_dong else 'Chưa có',  # Ngày vào
        'tien_dien': chi_so.GiaDienMoi * chi_so.SoDienDaTieuThu if chi_so.GiaDienMoi and chi_so.SoDienDaTieuThu else 0,
        'tien_nuoc': chi_so.GiaNuocMoi * chi_so.SoNuocDaTieuThu if chi_so.GiaNuocMoi and chi_so.SoNuocDaTieuThu else 0,
        'sua_chua': chi_so.TongDichVu - (chi_so.GiaDienMoi * chi_so.SoDienDaTieuThu + chi_so.GiaNuocMoi * chi_so.SoNuocDaTieuThu) if chi_so.TongDichVu else 0,
        'khac': 0  # Assuming 'khac' is a placeholder for any other charges, set to 0
    }
    
    return render(request, 'HTML/xuathoadon.html', {'hoa_don': hoa_don_info})