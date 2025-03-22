class LichSuGiaoDich(models.Model):
    LichSuID = models.AutoField(primary_key=True)
    ThanhToanID = models.ForeignKey('ThanhToan', on_delete=models.CASCADE)
    NgayThanhToan = models.DateTimeField(auto_now_add=True)
    SoTienDaThanhToan = models.DecimalField(max_digits=10, decimal_places=2)
    PhuongThucThanhToan = models.CharField(max_length=50, choices=[('TienMat', 'Tiền mặt'), ('ChuyenKhoan', 'Chuyển khoản'), ('VNPay', 'VNPay'), ('MOMO', 'MOMO')])
    MaGiaoDich = models.CharField(max_length=100, null=True, blank=True)
    TrangThaiGiaoDich = models.CharField(max_length=20, choices=[('ThanhCong', 'Thành công'), ('ThatBai', 'Thất bại'), ('ChoXuLy', 'Chờ xử lý')], default='ChoXuLy')

class TaiKhoan(models.Model):
    TaiKhoanID = models.AutoField(primary_key=True)
    KhachHangID = models.OneToOneField(KhachHang, on_delete=models.CASCADE, related_name='tai_khoan')
    TenDangNhap = models.CharField(max_length=50, unique=True)
    MatKhau = models.CharField(max_length=50)
    NgayTao = models.DateTimeField(auto_now_add=True)
    TrangThai = models.CharField(max_length=20, choices=[
        ('HoatDong', 'Hoạt động'),
        ('Khoa', 'Khóa'),
        ('Xoa', 'Xóa')
    ], default='HoatDong')

    def __str__(self):
        return f"Tài khoản {self.TenDangNhap} - {self.KhachHangID.HoTenKhachHang}"

    class Meta:
        db_table = 'TaiKhoan'
        verbose_name = 'Tài khoản'
        verbose_name_plural = 'Tài khoản' 