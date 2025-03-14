from django.db import models
from django.utils import timezone

# Model Quản lí (không thay đổi)
class QuanLi(models.Model):
    QuanLiID = models.AutoField(primary_key=True)
    SoDienThoaiDN = models.CharField(max_length=15, unique=True)
    MatKhauDN = models.CharField(max_length=100)  # Lưu mật khẩu đã hash
    HoTenQuanLi = models.CharField(max_length=100)
    failed_attempts = models.IntegerField(default=0)  # Số lần đăng nhập thất bại
    lockout_time = models.DateTimeField(null=True, blank=True)  # Thời gian tài khoản bị khóa

# Model Khách Hàng (không thay đổi)
class KhachHang(models.Model):
    KhachHangID = models.AutoField(primary_key=True)
    HoTenKhachHang = models.CharField(max_length=100)
    SoDienThoai = models.CharField(max_length=15, null=True, blank=True)  # Thêm trường này
    NgaySinh = models.DateField()
    GioiTinh = models.CharField(max_length=5)
    CongViec = models.CharField(max_length=100)
    TinhThanh = models.CharField(max_length=100)
    QuanHuyen = models.CharField(max_length=100)
    PhuongXa = models.CharField(max_length=100)
    DiaChiCuThe = models.CharField(max_length=255)
    SoCCCD = models.CharField(max_length=12)
    NgayCapCCCD = models.DateField()
    NoiCapCCCD = models.CharField(max_length=100)
    CCCDMT = models.ImageField(upload_to='images/')
    CCCDMS = models.ImageField(upload_to='images/')

# Model Phòng
class Phong(models.Model):
    PhongID = models.AutoField(primary_key=True)
    SoPhong = models.CharField(max_length=100)
    DayPhong = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B')])
    GiaPhong = models.DecimalField(max_digits=10, decimal_places=2)
    TrangThaiPhong = models.CharField(max_length=50, choices=[('ConTrong', 'Còn trống'), ('DaThue', 'Đã thuê')])
    MoTaPhong = models.TextField()
    DienTich = models.CharField(max_length=10)  # Cho phép lưu cả số và đơn vị (ví dụ: "15m2")
    TienIch = models.JSONField(default=list)  # Lưu danh sách tiện ích


# Model Hợp Đồng
class HopDong(models.Model):
    HopDongID = models.AutoField(primary_key=True)
    PhongID = models.ForeignKey('Phong', on_delete=models.CASCADE)
    KhachHangID = models.ForeignKey('KhachHang', on_delete=models.CASCADE)
    DayPhong = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B')])
    NgayBatDau = models.DateField()
    NgayKetThuc = models.DateField()
    ChuKy = models.CharField(max_length=100, default='1 tháng')
    TienDatCoc = models.DecimalField(max_digits=10, decimal_places=2)
    TrangThaiHopDong = models.CharField(max_length=50, choices=[('HoatDong', 'Hoạt động'), ('HetHan', 'Hết hạn')])
    NgayTaoHopDong = models.DateField(auto_now_add=True)
class ChiSoDienNuoc(models.Model):
    ChiSoID = models.AutoField(primary_key=True)
    PhongID = models.ForeignKey('Phong', on_delete=models.CASCADE, related_name='chi_so_dien_nuoc')
    DayPhong = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B')])
    ThangNam = models.CharField(max_length=7, null=True, blank=True)
    ChiSoDienCu = models.IntegerField(null=True, blank=True)
    ChiSoNuocCu = models.IntegerField(null=True, blank=True)
    ChiSoDienMoi = models.IntegerField(null=True, blank=True)
    ChiSoNuocMoi = models.IntegerField(null=True, blank=True)
    SoDienDaTieuThu = models.IntegerField(null=True, blank=True)
    SoNuocDaTieuThu = models.IntegerField(null=True, blank=True)
    TongTienDien = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    TongTienNuoc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    TienPhong = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    TongPhiPhatSinh = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    TongTien = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    TrangThaiThanhToan = models.CharField(max_length=1, null=True, blank=True)
    Tientra = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    TienNo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

# Model Phí phát sinh
class PhiPhatSinh(models.Model):
    PhatSinhID = models.AutoField(primary_key=True)
    PhongID = models.ForeignKey('Phong', on_delete=models.CASCADE)
    DayPhong = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B')])
    TenPhatSinh = models.CharField(max_length=100)
    GiaPhatSinh = models.DecimalField(max_digits=10, decimal_places=2)
    MoTaPhatSinh = models.TextField()
    ThangNam = models.CharField(max_length=7)

# Model Thanh Toán (không thay đổi)
class ThanhToan(models.Model):
    ThanhToanID = models.AutoField(primary_key=True)
    KhachHangID = models.ForeignKey('KhachHang', on_delete=models.CASCADE)
    PhongID = models.ForeignKey('Phong', on_delete=models.CASCADE)
    HopDongID = models.ForeignKey('HopDong', on_delete=models.CASCADE)
    ChiSoDienNuocID = models.ForeignKey('ChiSoDienNuoc', on_delete=models.CASCADE, null=True, blank=True)
    SoTienThanhToan = models.DecimalField(max_digits=10, decimal_places=2)
    PhuongThucThanhToan = models.CharField(max_length=50, choices=[('TienMat', 'Tiền mặt'), ('ChuyenKhoan', 'Chuyển khoản'), ('VNPay', 'VNPay'), ('MOMO', 'MOMO')])
    MaGiaoDich = models.CharField(max_length=100, null=True, blank=True)
    TrangThaiGiaoDich = models.CharField(max_length=20, choices=[('ThanhCong', 'Thành công'), ('ThatBai', 'Thất bại'), ('ChoXuLy', 'Chờ xử lý')], default='ChoXuLy')
    NoiDungThanhToan = models.CharField(max_length=255, null=True, blank=True)
    NgayThanhToan = models.DateTimeField(auto_now_add=True)
    ResponseData = models.JSONField(null=True, blank=True)

# Model Lịch Sử Giao Dịch (không thay đổi)
class LichSuGiaoDich(models.Model):
    LichSuID = models.AutoField(primary_key=True)
    ThanhToanID = models.ForeignKey('ThanhToan', on_delete=models.CASCADE)
    NgayThanhToan = models.DateTimeField(auto_now_add=True)
    SoTienDaThanhToan = models.DecimalField(max_digits=10, decimal_places=2)
    PhuongThucThanhToan = models.CharField(max_length=50, choices=[('TienMat', 'Tiền mặt'), ('ChuyenKhoan', 'Chuyển khoản'), ('VNPay', 'VNPay'), ('MOMO', 'MOMO')])
    MaGiaoDich = models.CharField(max_length=100, null=True, blank=True)
    TrangThaiGiaoDich = models.CharField(max_length=20, choices=[('ThanhCong', 'Thành công'), ('ThatBai', 'Thất bại'), ('ChoXuLy', 'Chờ xử lý')], default='ChoXuLy')