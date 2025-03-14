
function showStatus(side) {
    var input = document.getElementById(side + '-id-image');
    var status = document.getElementById('status-' + side);

    // Kiểm tra nếu có tệp được chọn
    if (input.files && input.files.length > 0) {
        status.style.display = 'block';
    } else {
        status.style.display = 'none';
    }
}
// địa chỉ
  const data = {
    "Can Tho": {
        "Ninh Kiều": ["An Cư", "An Hòa", "An Khánh", "An Nghiệp", "An Phú", "Cái Khế", "Hưng Lợi", "Tân An", "Thới Bình", "Xuân Khánh"],
        "Bình Thủy": ["An Thới", "Bình Thủy", "Long Hòa", "Long Tuyền", "Thới An Đông", "Trà An", "Trà Nóc"],
        "Cái Răng": ["Ba Láng", "Hưng Phú", "Hưng Thạnh", "Lê Bình", "Phú Thứ", "Tân Phú", "Thường Thạnh"],
        "Ô Môn": ["Châu Văn Liêm", "Long Hưng", "Phước Thới", "Thới An", "Thới Hòa", "Trường Lạc"],
        "Thốt Nốt": ["Thốt Nốt", "Thới Thuận", "Tân Lộc", "Tân Hưng", "Thuận An", "Trung Nhứt", "Trung Kiên", "Trung Thạnh"],
        "Phong Điền": ["Nhơn Ái", "Nhơn Nghĩa", "Tân Thới", "Trường Long", "Mỹ Khánh", "Giai Xuân"],
        "Cờ Đỏ": ["Thới Hưng", "Thới Đông", "Thạnh Phú", "Đông Hiệp", "Đông Thắng", "Trung Hưng", "Trung An"],
         "Vĩnh Thạnh": ["Vĩnh Thạnh", "Thạnh Mỹ", "Thạnh An", "Thạnh Quới", "Thạnh Thắng", "Thạnh Tiến", "Thạnh Lộc", "Thạnh Lợi"],
        "Thới Lai": ["Thới Lai", "Tân Thạnh", "Đông Bình", "Đông Thuận", "Thới Tân", "Thới Thạnh", "Trường Thành", "Trường Thắng", "Xuân Thắng"],
    },
    "Ho Chi Minh": {
        "Quận 1": ["Bến Nghé", "Bến Thành", "Cầu Kho", "Cầu Ông Lãnh", "Cô Giang", "Đa Kao", "Nguyễn Cư Trinh", "Nguyễn Thái Bình", "Phạm Ngũ Lão", "Tân Định"],
"Quận 2": ["An Khánh", "An Lợi Đông", "An Phú", "Bình An", "Bình Khánh", "Bình Trưng Đông", "Bình Trưng Tây", "Cát Lái", "Thạnh Mỹ Lợi", "Thảo Điền"],
"Quận 3": ["Phường 1", "Phường 2", "Phường 3", "Phường 4", "Phường 5", "Phường 6", "Phường 7", "Phường 8", "Phường 9", "Phường 10", "Phường 11", "Phường 12", "Phường 13", "Phường 14"],
"Quận 4": ["Phường 1", "Phường 2", "Phường 3", "Phường 4", "Phường 5", "Phường 6", "Phường 8", "Phường 9", "Phường 10", "Phường 12", "Phường 13", "Phường 14", "Phường 15", "Phường 16", "Phường 18"],
"Quận 5": ["Phường 1", "Phường 2", "Phường 3", "Phường 4", "Phường 5", "Phường 6", "Phường 7", "Phường 8", "Phường 9", "Phường 10", "Phường 11", "Phường 12", "Phường 13", "Phường 14", "Phường 15"],
"Quận 6": ["Phường 1", "Phường 2", "Phường 3", "Phường 4", "Phường 5", "Phường 6", "Phường 7", "Phường 8", "Phường 9", "Phường 10", "Phường 11", "Phường 12", "Phường 13", "Phường 14"],
"Quận 7": ["Bình Thuận", "Phú Mỹ", "Phú Thuận", "Tân Hưng", "Tân Kiểng", "Tân Phong", "Tân Phú", "Tân Quy", "Tân Thuận Đông", "Tân Thuận Tây"],
"Quận 8": ["Phường 1", "Phường 2", "Phường 3", "Phường 4", "Phường 5", "Phường 6", "Phường 7", "Phường 8", "Phường 9", "Phường 10", "Phường 11", "Phường 12", "Phường 13", "Phường 14", "Phường 15", "Phường 16"],
"Quận 9": ["Hiệp Phú", "Long Bình", "Long Phước", "Long Thạnh Mỹ", "Long Trường", "Phú Hữu", "Phước Bình", "Phước Long A", "Phước Long B", "Tăng Nhơn Phú A", "Tăng Nhơn Phú B", "Trường Thạnh"],
"Quận 10": ["Phường 1", "Phường 2", "Phường 3", "Phường 4", "Phường 5", "Phường 6", "Phường 7", "Phường 8", "Phường 9", "Phường 10", "Phường 11", "Phường 12", "Phường 13", "Phường 14", "Phường 15"],
"Quận 11": ["Phường 1", "Phường 2", "Phường 3", "Phường 4", "Phường 5", "Phường 6", "Phường 7", "Phường 8", "Phường 9", "Phường 10", "Phường 11", "Phường 12", "Phường 13", "Phường 14", "Phường 15"],
"Quận 12": ["An Phú Đông", "Đông Hưng Thuận", "Hiệp Thành", "Tân Chánh Hiệp", "Tân Thới Hiệp", "Tân Thới Nhất", "Thạnh Lộc", "Thạnh Xuân", "Thới An", "Trung Mỹ Tây"],
"Quận Bình Tân": ["An Lạc", "An Lạc A", "Bình Hưng Hòa", "Bình Hưng Hòa A", "Bình Hưng Hòa B", "Bình Trị Đông", "Bình Trị Đông A", "Bình Trị Đông B", "Tân Tạo", "Tân Tạo A"],
"Quận Bình Thạnh": ["Phường 1", "Phường 2", "Phường 3", "Phường 5", "Phường 6", "Phường 7", "Phường 11", "Phường 12", "Phường 13", "Phường 14", "Phường 15", "Phường 17", "Phường 19", "Phường 21", "Phường 22", "Phường 24", "Phường 25", "Phường 26", "Phường 27", "Phường 28"],
"Quận Gò Vấp": ["Phường 1", "Phường 3", "Phường 4", "Phường 5", "Phường 6", "Phường 7", "Phường 8", "Phường 9", "Phường 10", "Phường 11", "Phường 12", "Phường 13", "Phường 14", "Phường 15", "Phường 16", "Phường 17"],
"Quận Phú Nhuận": ["Phường 1", "Phường 2", "Phường 3", "Phường 5",  "Phường 7", "Phường 8", "Phường 9", "Phường 10", "Phường 11", "Phường 13","Phường 15", "Phường 17"],
"Quận Tân Bình": ["Phường 1", "Phường 3", "Phường 4", "Phường 5", "Phường 6", "Phường 7", "Phường 8", "Phường 9", "Phường 10", "Phường 11", "Phường 12", "Phường 13", "Phường 14", "Phường 15"],
"Quận Tân Phú": ["Hiệp Tân", "Hòa Thạnh", "Phú Thạnh", "Phú Thọ Hòa", "Phú Trung", "Sơn Kỳ", "Tân Quý", "Tân Sơn Nhì", "Tân Thành", "Tây Thạnh"],
"Quận Thủ Đức": ["Bình Chiểu", "Bình Thọ", "Hiệp Bình Chánh", "Hiệp Bình Phước", "Linh Chiểu", "Linh Đông", "Linh Tây", "Linh Trung", "Linh Xuân", "Tam Bình", "Tam Phú", "Trường Thọ"],
"Huyện Bình Chánh": ["An Phú Tây", "Bình Chánh", "Bình Hưng", "Bình Lợi", "Đa Phước", "Hưng Long", "Lê Minh Xuân", "Phong Phú", "Qui Đức", "Tân Kiên", "Tân Nhựt", "Tân Quý Tây", "Vĩnh Lộc A", "Vĩnh Lộc B"],
"Huyện Cần Giờ": ["An Thới Đông", "Bình Khánh", "Cần Thạnh", "Lý Nhơn", "Long Hòa", "Tam Thôn Hiệp", "Thạnh An"],
"Huyện Củ Chi": ["An Nhơn Tây", "An Phú", "Bình Mỹ", "Hòa Phú", "Nhuận Đức", "Phạm Văn Cội", "Phú Hòa Đông", "Phú Mỹ Hưng", "Phước Hiệp", "Phước Thạnh", "Phước Vĩnh An", "Tân An Hội", "Tân Phú Trung", "Tân Thạnh Đông", "Tân Thạnh Tây", "Tân Thông Hội", "Thái Mỹ", "Trung An", "Trung Lập Hạ", "Trung Lập Thượng"],
"Huyện Hóc Môn": ["Bà Điểm", "Đông Thạnh", "Nhị Bình", "Tân Hiệp", "Tân Thới Nhì", "Thới Tam Thôn", "Trung Chánh", "Xuân Thới Đông", "Xuân Thới Sơn", "Xuân Thới Thượng"],
"Huyện Nhà Bè": ["Hiệp Phước", "Long Thới", "Nhơn Đức", "Phú Xuân", "Phước Kiển", "Phước Lộc"]
    },
    "Ha Noi": {
        "Ba Đình": ["Cống Vị", "Điện Biên", "Đội Cấn", "Giảng Võ", "Kim Mã", "Liễu Giai", "Ngọc Hà", "Ngọc Khánh", "Nguyễn Trung Trực", "Phúc Xá", "Quán Thánh", "Thành Công", "Trúc Bạch", "Vĩnh Phúc"],
"Hoàn Kiếm": ["Chương Dương", "Cửa Đông", "Cửa Nam", "Đồng Xuân", "Hàng Bạc", "Hàng Bài", "Hàng Bồ", "Hàng Bông", "Hàng Buồm", "Hàng Đào", "Hàng Gai", "Hàng Mã", "Hàng Trống", "Lý Thái Tổ", "Phan Chu Trinh", "Phúc Tân", "Tràng Tiền", "Trần Hưng Đạo"],
"Bắc Từ Liêm": ["Cổ Nhuế 1", "Cổ Nhuế 2", "Đông Ngạc", "Đức Thắng", "Liên Mạc", "Minh Khai", "Phú Diễn", "Phúc Diễn", "Tây Tựu", "Thượng Cát", "Thụy Phương", "Xuân Đỉnh", "Xuân Tảo"],
"Cầu Giấy": ["Dịch Vọng", "Dịch Vọng Hậu", "Mai Dịch", "Nghĩa Đô", "Nghĩa Tân", "Quan Hoa", "Trung Hòa", "Yên Hòa"],
"Đống Đa": ["Cát Linh", "Hàng Bột", "Khâm Thiên", "Khương Thượng", "Kim Liên", "Láng Hạ", "Láng Thượng", "Nam Đồng", "Ngã Tư Sở", "Phương Liên", "Phương Mai", "Quang Trung", "Quốc Tử Giám", "Thịnh Quang", "Thổ Quan", "Trung Liệt", "Trung Phụng", "Trung Tự", "Văn Chương", "Văn Miếu"],
"Hà Đông": ["Biên Giang", "Đồng Mai", "Dương Nội", "Hà Cầu", "Kiến Hưng", "La Khê", "Mộ Lao", "Nguyễn Trãi", "Phú La", "Phú Lãm", "Phú Lương", "Phúc La", "Quang Trung", "Vạn Phúc", "Văn Quán", "Yên Nghĩa", "Yết Kiêu"],
"Hai Bà Trưng": ["Bạch Đằng", "Bạch Mai", "Bách Khoa", "Cầu Dền", "Đồng Nhân", "Đồng Tâm", "Lê Đại Hành", "Minh Khai", "Ngô Thì Nhậm", "Nguyễn Du", "Phạm Đình Hổ", "Phố Huế", "Quỳnh Lôi", "Quỳnh Mai", "Thanh Lương", "Thanh Nhàn", "Trương Định", "Vĩnh Tuy"],
"Hoàng Mai": ["Đại Kim", "Định Công", "Giáp Bát", "Hoàng Liệt", "Hoàng Văn Thụ", "Lĩnh Nam", "Mai Động", "Tân Mai", "Thịnh Liệt", "Trần Phú", "Trương Định", "Vĩnh Hưng", "Yên Sở"],
"Long Biên": ["Bồ Đề", "Cự Khối", "Đức Giang", "Gia Thụy", "Giang Biên", "Long Biên", "Ngọc Lâm", "Ngọc Thụy", "Phúc Đồng", "Phúc Lợi", "Sài Đồng", "Thạch Bàn", "Thượng Thanh", "Việt Hưng"],
"Nam Từ Liêm": ["Cầu Diễn", "Đại Mỗ", "Mễ Trì", "Mỹ Đình 1", "Mỹ Đình 2", "Phú Đô", "Phương Canh", "Tây Mỗ", "Trung Văn", "Xuân Phương"],
"Tây Hồ": ["Bưởi", "Nhật Tân", "Phú Thượng", "Quảng An", "Thụy Khuê", "Tứ Liên", "Xuân La", "Yên Phụ"],
"Thanh Xuân": ["Hạ Đình", "Khương Đình", "Khương Mai", "Khương Trung", "Nhân Chính", "Phương Liệt", "Thanh Xuân Bắc", "Thanh Xuân Nam", "Thanh Xuân Trung", "Thượng Đình"],
    },
    "Da Nang": {
"Hải Châu": ["Bình Hiên", "Bình Thuận", "Hải Châu I", "Hải Châu II", "Hòa Cường Bắc", "Hòa Cường Nam", "Hòa Thuận Đông", "Hòa Thuận Tây", "Nam Dương", "Phước Ninh", "Thạch Thang", "Thanh Bình", "Thuận Phước"],
"Thanh Khê": ["An Khê", "Chính Gián", "Hòa Khê", "Tam Thuận", "Tân Chính", "Thạc Gián", "Thanh Khê Đông", "Thanh Khê Tây", "Vĩnh Trung", "Xuân Hà"],
"Sơn Trà": ["An Hải Bắc", "An Hải Đông", "An Hải Tây", "Mân Thái", "Nại Hiên Đông", "Phước Mỹ", "Thọ Quang"],
"Ngũ Hành Sơn": ["Hòa Hải", "Hòa Quý", "Khuê Mỹ", "Mỹ An"],
"Liên Chiểu": ["Hòa Hiệp Bắc", "Hòa Hiệp Nam", "Hòa Khánh Bắc", "Hòa Khánh Nam", "Hòa Minh"],
"Cẩm Lệ": ["Hòa An", "Hòa Phát", "Hòa Thọ Đông", "Hòa Thọ Tây", "Hòa Xuân", "Khuê Trung"],
"Hòa Vang": ["Hòa Bắc", "Hòa Châu", "Hòa Khương", "Hòa Liên", "Hòa Nhơn", "Hòa Ninh", "Hòa Phong", "Hòa Phú", "Hòa Phước", "Hòa Sơn", "Hòa Tiến"],
"Hoàng Sa": ["Đảo Hoàng Sa"]
},
"Da Nang": {
"Hải Châu": ["Bình Hiên", "Bình Thuận", "Hải Châu I", "Hải Châu II", "Hòa Cường Bắc", "Hòa Cường Nam", "Hòa Thuận Đông", "Hòa Thuận Tây", "Nam Dương", "Phước Ninh", "Thạch Thang", "Thanh Bình", "Thuận Phước"],
"Thanh Khê": ["An Khê", "Chính Gián", "Hòa Khê", "Tam Thuận", "Tân Chính", "Thạc Gián", "Thanh Khê Đông", "Thanh Khê Tây", "Vĩnh Trung", "Xuân Hà"],
"Sơn Trà": ["An Hải Bắc", "An Hải Đông", "An Hải Tây", "Mân Thái", "Nại Hiên Đông", "Phước Mỹ", "Thọ Quang"],
"Ngũ Hành Sơn": ["Hòa Hải", "Hòa Quý", "Khuê Mỹ", "Mỹ An"],
"Liên Chiểu": ["Hòa Hiệp Bắc", "Hòa Hiệp Nam", "Hòa Khánh Bắc", "Hòa Khánh Nam", "Hòa Minh"],
"Cẩm Lệ": ["Hòa An", "Hòa Phát", "Hòa Thọ Đông", "Hòa Thọ Tây", "Hòa Xuân", "Khuê Trung"],
"Hòa Vang": ["Hòa Bắc", "Hòa Châu", "Hòa Khương", "Hòa Liên", "Hòa Nhơn", "Hòa Ninh", "Hòa Phong", "Hòa Phú", "Hòa Phước", "Hòa Sơn", "Hòa Tiến"],
"Hoàng Sa": ["Đảo Hoàng Sa"]
},
"Hai Phong": {
"Hồng Bàng": ["Hạ Lý", "Hoàng Văn Thụ", "Hùng Vương", "Minh Khai", "Phan Bội Châu", "Quán Toan", "Sở Dầu", "Thượng Lý", "Trại Chuối"],
"Ngô Quyền": ["Cầu Đất", "Đằng Giang", "Đông Khê", "Gia Viên", "Lạc Viên", "Lê Lợi", "Máy Chai", "Máy Tơ", "Vạn Mỹ"],
"Lê Chân": ["An Biên", "An Dương", "Cát Dài", "Dư Hàng", "Dư Hàng Kênh", "Hàng Kênh", "Hồ Nam", "Kênh Dương", "Lam Sơn", "Nghĩa Xá", "Niệm Nghĩa", "Trại Cau", "Vĩnh Niệm"],
"Hải An": ["Cát Bi", "Đằng Hải", "Đằng Lâm", "Đông Hải 1", "Đông Hải 2", "Nam Hải", "Tràng Cát"],
"Kiến An": ["Bắc Sơn", "Đồng Hòa", "Lãm Hà", "Nam Sơn", "Ngọc Sơn", "Phù Liễn", "Quán Trữ", "Trần Thành Ngọ"],
"Dương Kinh": ["Anh Dũng", "Đa Phúc", "Hưng Đạo", "Hải Thành", "Tân Thành", "Hoà Nghĩa"],
"An Dương": ["An Đồng", "An Hòa", "An Hưng", "An Hồng", "An Tiến", "Bắc Sơn", "Đặng Cương", "Đại Bản", "Đồng Thái", "Hồng Phong", "Hồng Thái", "Lê Lợi", "Nam Sơn", "Tân Tiến"],
"An Lão": ["An Lão", "An Thắng", "An Tiến", "Bát Trang", "Chiến Thắng", "Mỹ Đức", "Quang Trung", "Quốc Tuấn", "Tân Dân", "Tân Viên", "Thái Sơn", "Trường Sơn"],
"Bạch Long Vĩ": ["Thị Trấn Bạch Long Vĩ"],
"Cát Hải": ["Cát Bà", "Cát Hải", "Hiền Hào", "Nghĩa Lộ", "Phù Long", "Trân Châu", "Văn Phong", "Xuân Đám"],
"Kiến Thụy": ["Đại Đồng", "Đoàn Xá", "Đông Phương", "Hưng Nhân", "Hữu Bằng", "Kiến Quốc", "Minh Tân", "Ngũ Đoan", "Tân Phong", "Tân Trào", "Thanh Sơn", "Thuận Thiên", "Thuỵ Hương"],
"Thủy Nguyên": ["Cao Nhân", "Chính Mỹ", "Đông Sơn", "Dương Quan", "Gia Đức", "Gia Minh", "Hoà Bình", "Hoa Động", "Hoà Ninh", "Hợp Thành", "Kênh Giang", "Kiền Bái", "Kỳ Sơn", "Lại Xuân", "Lập Lễ", "Liên Khê", "Lưu Kiếm", "Lưu Kỳ", "Minh Tân", "Mỹ Đồng", "Ngũ Lão", "Núi Đèo", "Phục Lễ", "Phù Ninh", "Quảng Thanh", "Tân Dương", "Tam Hưng", "Thiên Hương", "Thuỷ Đường", "Thuỷ Sơn", "Thuỷ Triều"],
"Tiên Lãng": ["Bạch Đằng", "Cấp Tiến", "Đại Thắng", "Đoàn Lập", "Đông Hưng", "Khởi Nghĩa", "Kiến Thiết", "Nam Hưng", "Nam Hải", "Quyết Tiến", "Tây Hưng", "Tiên Cường", "Tiên Minh", "Tiên Thanh", "Tiên Thắng", "Tiên Tiến", "Tự Cường", "Toàn Thắng", "Vinh Quang"],
"Vĩnh Bảo": ["An Hòa", "Cao Minh", "Cổ Am", "Dũng Tiến", "Giang Biên", "Hiệp Hòa", "Hòa Bình", "Hùng Tiến", "Liên Am", "Lý Học", "Nhân Hoà", "Tam Cường", "Tam Đa", "Tam Lương", "Tân Hưng", "Tân Liên", "Tân Tiến", "Thanh Lương", "Thắng Thủy", "Trung Lập", "Vĩnh An", "Vĩnh Bảo", "Vĩnh Long", "Vĩnh Phong", "Vĩnh Tiến"]
},
"An Giang": {
"Long Xuyên": ["Bến Ghé", "Bình Khánh", "Khánh Hòa", "Mỹ Phước", "Nhà Bàng", "Tân Lộc", "Tân An", "Vĩnh Ninh"],
"Châu Đốc": ["Châu Phú", "Cô Tô", "Đông Hồ", "Hưng Điền A", "Hưng Điền B", "Vĩnh Tế"],
"An Phú": ["Khánh An", "Khánh Bình", "Phú Hữu", "Phú Mỹ", "Quốc Thái", "Tân An", "Tân Châu"],
"Châu Phú": ["Bình Long", "Châu Phú A", "Châu Phú B", "Đông Xuyên", "Tân Phú"],
"Châu Thành": ["Bình Mỹ", "Châu Thành A", "Châu Thành B", "Đông Thạnh", "Hòa Bình", "Phú Hòa"],
"Chợ Mới": ["An Thạnh Trung", "Hòa An", "Long Điền A", "Long Điền B", "Tân Thạnh", "Tịnh Biên"],
"Phú Tân": ["Phú Tân", "Tân Trung"],
"Thoại Sơn": ["Định Mỹ", "Thoại Giang", "Thoại Sơn", "Vĩnh Trạch"],
"Tịnh Biên": ["Tân Lợi", "Tịnh Biên", "Vĩnh Trung"],
"Tri Tôn": ["Tri Tôn", "Lạc Quới", "Vĩnh Gia"]
},
"Ba Ria - Vung Tau": {
"Vũng Tàu": ["Bãi Sau", "Bãi Trước", "Phước Hải", "Long Hải"],
"Bà Rịa": ["Long Tân", "Phước Bình", "Tân Hòa"],
"Châu Đức": ["Bàu Chinh", "Bình Trung", "Nghĩa Thành", "Quảng Thành"],
"Côn Đảo": ["Côn Sơn", "Đất Đỏ"],
"Đất Đỏ": ["Đất Đỏ", "Lộc An", "Phước Hải"],
"Long Điền": ["Long Điền", "Phước Hải", "Tam Phước"],
"Phú Mỹ": ["Châu Pha", "Hòa Hội", "Hòa Long", "Phú Mỹ", "Tân Thành"],
"Xuyên Mộc": ["Bắc Sơn", "Bàu Lâm", "Phước Bình", "Phước Hòa", "Phước Tân", "Tam Phước"]
},
"Bac Giang": {
"Bắc Giang": ["Dĩnh Kế", "Đại Lâm", "Đồng Sơn", "Hòa Long", "Nội Hoàng", "Ngọc Châu", "Tân Mỹ"],
"Hiệp Hòa": ["Bắc Lương", "Đan Hội", "Đông Lương", "Hợp Thịnh", "Lương Phong"],
"Lạng Giang": ["Bắc Lạng", "Cẩm Lạng", "Đan Hội", "Đông Phú", "Lạng Giang"],
"Lục Nam": ["Bình Sơn", "Cẩm Lý", "Đan Mỹ", "Khám Lạng", "Lục Nam", "Tân Dĩnh"],
"Lục Ngạn": ["Chũ", "Đèo Gia", "Đồng Hỷ", "Hồng Giang", "Lục Ngạn", "Phú Nhuận"],
"Sơn Động": ["An Lạc", "Cẩm Sơn", "Đông Sơn", "Lục Sơn", "Sơn Động"],
"Tân Yên": ["Bắc Lý", "Đại Hợp", "Đồng Hòa", "Quế Nhai", "Tân Yên"],
"Việt Yên": ["Bắc Tiến", "Bắc Giang", "Bắc Tân", "Đại Hợp", "Đồng Lý", "Phú Lương", "Tân Liễu"],
"Yên Dũng": ["Đại Lợi", "Đức Giang", "Hương Gián", "Hương Sơn", "Yên Dũng"],
"Yên Thế": ["Bố Hạ", "Canh Nậu", "Đại Lâm", "Đồng Hưu", "Hà Ninh"]
},
"Bac Kan": {
"Bắc Kạn": ["Bắc Kạn", "Nông Thượng", "Sông Cầu", "Xuân Lạc"],
"Ba Bể": ["Ba Bể", "Địa Linh", "Khang Ninh", "Nam Mẫu", "Quảng Khê"],
"Bạch Thông": ["Bạch Thông", "Cẩm Giàng", "Đồng Thẩm", "Nguyên Phúc", "Tân Tú"],
"Chợ Đồn": ["Chợ Đồn", "Bằng Lãng", "Định Hóa", "Nam Cường", "Ngọc Phái"],
"Chợ Mới": ["Chợ Mới", "Đức Xuân", "Nà Tu", "Quảng Bạch", "Tân Sơn"],
"Na Rì": ["Na Rì", "Đồng Liên", "Đức Chính", "Khánh Xuân", "Lương Thượng"],
"Ngân Sơn": ["Ngân Sơn", "Bằng Vân", "Cốc Đán", "Đức Sinh", "Ngọc Lạc"],
"Pác Nặm": ["Pác Nặm", "Cổ Linh", "Khánh Khê", "Nà Thẩu", "Thị trấn Pác Nặm"]
},
"Bac Lieu": {
"Bạc Liêu": ["Bạc Liêu", "Nhà Mát", "Phường 1", "Phường 2", "Phường 3", "Phường 4"],
"Đông Hải": ["Đông Hải", "Đồng Tâm", "Long Điền Đông", "Long Điền Tây"],
"Giá Rai": ["Giá Rai", "Phường 1", "Phường 2", "Phường 3", "Phường 4"],
"Hòa Bình": ["Hòa Bình", "Hòa Bình", "Hòa Lợi"],
"Hồng Dân": ["Hồng Dân", "Lộc Ninh", "Ninh Quới", "Ninh Thạnh Lợi"],
"Phước Long": ["Phước Long", "Phước Khánh", "Phước Mỹ", "Phước Thạnh"],
"Vĩnh Lợi": ["Vĩnh Lợi", "Vĩnh Lộc", "Vĩnh Thạnh", "Vĩnh Phú"]
},
"Bac Ninh": {
"Bắc Ninh": ["Đại Phúc", "Đào Viên", "Khắc Niệm", "Kinh Bắc", "Vệ An"],
"Gia Bình": ["Gia Bình", "Giang Sơn", "Nhân Thắng", "Quỳnh Phú", "Song Giang"],
"Lương Tài": ["Lương Tài", "Bình Định", "Lương Tài", "Phú Hòa"],
"Quế Võ": ["Phương Liễu", "Tam Đa", "Văn Môn", "Vạn An"],
"Thuận Thành": ["Bình Định", "Đại Đồng", "Đình Bảng", "Gia Đông"],
"Tiên Du": ["Đông Côi", "Hoàn Sơn", "Nam Sơn", "Tiên Sơn"],
"Từ Sơn": ["Đình Bảng", "Đông Ngàn", "Phù Khê", "Tân Hồng"],
"Yên Phong": ["Yên Phong", "Vân Hà", "Vân Trung", "Yên Trung"]
},
"Ben Tre": {
"Bến Tre": ["Phường 1", "Phường 2", "Phường 3", "Phường 4", "Phường 5", "Phường 6"],
"Ba Tri": ["Ba Tri", "Bình Thạnh", "Đức Thạnh", "Hưng Nhượng"],
"Bình Đại": ["Bình Đại", "Bình Thới", "Đại Hòa", "Đại Điền"],
"Châu Thành": ["Châu Thành", "An Khánh", "An Phú", "Tân Thạch"],
"Chợ Lách": ["Chợ Lách", "Bình Hòa", "Bình Đại", "Phú Sơn"],
"Giồng Trôm": ["Giồng Trôm", "Châu Bình", "Lương Phú", "Phước Mỹ"],
"Mỏ Cày Bắc": ["Mỏ Cày Bắc", "Mỏ Cày Nam", "Thành An"],
"Mỏ Cày Nam": ["Mỏ Cày Nam", "Thành An", "Thạnh Ngãi"],
"Thạnh Phú": ["Thạnh Phú", "Hòa Lợi", "Hòa Nghĩa", "Thạnh Hải"]
},
"Binh Dinh": {
"Quy Nhơn": ["Đống Đa", "Ghềnh Ráng", "Hoài Hải", "Nhơn Bình", "Trần Hưng Đạo"],
"An Lão": ["An Lão", "Bắc Sơn", "Bình Tân", "Lý Lễ", "Pha Lê"],
"An Nhơn": ["An Nhơn", "Đông Bình", "Đông Cát", "Tây An", "Tân An"],
"Hoài Ân": ["Hoài Ân", "Bình Tân", "Đức Thạnh", "Hoài Hảo"],
"Hoài Nhơn": ["Hoài Nhơn", "Bình Dương", "Hoài Hảo", "Hoài Thanh", "Hoài Xuân"],
"Phù Cát": ["Phù Cát", "Cát Chánh", "Cát Hiệp", "Cát Khánh"],
"Phù Mỹ": ["Phù Mỹ", "Bắc Mỹ", "Hòa Mỹ", "Thành Mỹ"],
"Tây Sơn": ["Tây Sơn", "Định Bình", "Định Quán", "Bình Tân"],
"Tuy Phước": ["Tuy Phước", "Phước Hòa", "Phước Sơn", "Tuy Hòa"],
"Vân Canh": ["Vân Canh", "Canh Liên", "Canh Vinh"],
"Vĩnh Thạnh": ["Vĩnh Thạnh", "Vĩnh Hòa", "Vĩnh Thịnh"]
},
"Binh Duong": {
"Thủ Dầu Một": ["Chánh Nghĩa", "Hòa Phú", "Phú Hòa", "Tương Bình Hiệp"],
"Bàu Bàng": ["Bàu Bàng", "Hòa Phú", "Lạc An", "Phú Hội"],
"Bến Cát": ["Bến Cát", "Chánh Mỹ", "Định Thành", "Nguyên Khai"],
"Dầu Tiếng": ["Dầu Tiếng", "Định An", "Định Thành", "Định Hòa"],
"Dĩ An": ["Dĩ An", "An Bình", "Dĩ An", "Tân Bình"],
"Phú Giáo": ["Phú Giáo", "Phước Hòa", "Tân Hiệp"],
"Tân Uyên": ["Tân Uyên", "Khánh Bình", "Khánh Hòa", "Thái Hòa"],
"Thuận An": ["Thuận An", "An Phú", "Bình Nhâm", "Lái Thiêu"],
"Bắc Tân Uyên": ["Bắc Tân Uyên", "Tân Định", "Tân Hòa"]
},
"Binh Phuoc": {
"Đồng Xoài": ["Đồng Xoài", "Tiến Thành", "Tân Thành", "Tân Phú"],
"Bù Đăng": ["Bù Đăng", "Bù Gia Mập", "Đak Nhau"],
"Bù Đốp": ["Bù Đốp", "Đak Nhau"],
"Bù Gia Mập": ["Bù Gia Mập", "Phú Riềng"],
"Chơn Thành": ["Chơn Thành", "Thạnh Bình"],
"Đồng Phú": ["Đồng Phú", "Tam Hiệp", "Phú Riềng"],
"Hớn Quản": ["Hớn Quản", "Tân Lợi"],
"Lộc Ninh": ["Lộc Ninh", "Lộc Thịnh", "Lộc Hòa"],
"Phú Riềng": ["Phú Riềng", "Phú Nghĩa", "Phú Mỹ"]
},
"Binh Thuan": {
"Phan Thiết": ["Phú Thủy", "Phú Hài", "Mũi Né", "Hàm Tiến"],
"La Gi": ["La Gi", "Tân Thiện", "Tân Phú"],
"Bắc Bình": ["Bắc Bình", "Phan Rí Cửa", "Hàm Thắng"],
"Đức Linh": ["Đức Linh", "Đức Tín", "Nghị Đức"],
"Hàm Tân": ["Hàm Tân", "Hàm Mỹ"],
"Hàm Thuận Bắc": ["Hàm Thuận Bắc", "La Gi"],
"Hàm Thuận Nam": ["Hàm Thuận Nam", "Tân Phước"],
"Phú Quý": ["Phú Quý", "Tam Thanh"],
"Tánh Linh": ["Tánh Linh", "Vĩnh Hảo", "Vĩnh Hòa"],
"Tuy Phong": ["Tuy Phong", "Phú Lạc"]
},
"Ca Mau": {
"Cà Mau": ["An Xuyên", "Đường 19/5", "Tân Xuyên", "Khánh Hòa"],
"Cái Nước": ["Cái Nước", "Lương Thế Trân", "Thới Bình"],
"Đầm Dơi": ["Đầm Dơi", "Trần Phán", "Tân Duyệt", "Tân Thới"],
"Năm Căn": ["Năm Căn", "Hòa Thành", "Rạch Gốc"],
"Ngọc Hiển": ["Ngọc Hiển", "Viên An", "Tân Hưng"],
"Phú Tân": ["Phú Tân", "Phú Thịnh", "Phú Xuân"],
"Thới Bình": ["Thới Bình", "Thới Giang"],
"Trần Văn Thời": ["Trần Văn Thời", "Khánh Bình"],
"U Minh": ["U Minh", "Khánh An"]
},
"Cao Bang": {
"Cao Bằng": ["Cao Bằng", "Đề Thám", "Hợp Giang"],
"Bảo Lạc": ["Bảo Lạc", "Hồng Trị"],
"Bảo Lâm": ["Bảo Lâm", "Hưng Đạo"],
"Hạ Lang": ["Hạ Lang", "Đàm Thủy"],
"Hà Quảng": ["Hà Quảng", "Hà Thượng"],
"Hòa An": ["Hòa An", "Hòa Thuận"],
"Nguyên Bình": ["Nguyên Bình", "Tam Kim"],
"Phục Hòa": ["Phục Hòa", "Tân Việt"],
"Quảng Hòa": ["Quảng Hòa", "Chí Thảo"],
"Thạch An": ["Thạch An", "Kim Đồng"],
"Trùng Khánh": ["Trùng Khánh", "Đức Hạnh"]
},
"Dak Lak": {
"Buôn Ma Thuột": ["Tân Lợi", "Tân An", "Thành Nhất", "Thành Công"],
"Buôn Đôn": ["Buôn Đôn", "Tân Hòa", "Krông Na"],
"Cư Kuin": ["Cư Kuin", "Ea Ktur"],
"Cư M'gar": ["Cư M'gar", "Quảng Tiến"],
"Ea H'leo": ["Ea H'leo", "Ea Khal"],
"Ea Kar": ["Ea Kar", "Cư Ni"],
"Ea Súp": ["Ea Súp", "Hòa Đông"],
"Krông Ana": ["Krông Ana", "Lê Hồng Phong"],
"Krông Bông": ["Krông Bông", "Cư Kty"],
"Krông Buk": ["Krông Buk", "Buôn Hồ"],
"Krông Năng": ["Krông Năng", "Phú Xuân"],
"Krông Pắc": ["Krông Pắc", "Phước An"],
"Lắk": ["Lắk", "Bông Krang"],
"M'Đrắk": ["M'Đrắk", "Thắng Lợi"]
},
"Dak Nong": {
"Gia Nghĩa": ["Gia Nghĩa", "Đắk Nia", "Quảng Thành"],
"Cư Jút": ["Cư Jút", "Đắk Wil"],
"Đắk Glong": ["Đắk Glong", "Đắk Som"],
"Đắk Mil": ["Đắk Mil", "Đắk Phơi"],
"Đắk R'Lấp": ["Đắk R'Lấp", "Đắk Sin"],
"Đắk Song": ["Đắk Song", "Quảng Hòa"],
"Krông Nô": ["Krông Nô", "Nâm Nung"],
"Tuy Đức": ["Tuy Đức", "Đắk Buk So"]
},
"Dien Bien": {
"Điện Biên Phủ": ["Mường Thanh", "Thanh Bình", "Tân Thanh"],
"Mường Lay": ["Mường Lay", "Nậm Lay"],
"Điện Biên": ["Điện Biên", "Tây Thành"],
"Điện Biên Đông": ["Điện Biên Đông", "Mường Mìn"],
"Mường Ảng": ["Mường Ảng", "Nà Tấu"],
"Mường Chà": ["Mường Chà", "Nậm Nhừ"],
"Mường Nhé": ["Mường Nhé", "Nậm Vì"],
"Nậm Pồ": ["Nậm Pồ", "Nậm Khăn"],
"Tủa Chùa": ["Tủa Chùa", "Sín Thầu"],
"Tuần Giáo": ["Tuần Giáo", "Tỏa Tình"]
},
"Dong Nai": {
"Biên Hòa": ["An Bình", "Bửu Hòa", "Bửu Long", "Hóa An", "Hiệp Hòa"],
"Long Khánh": ["Bàu Trâm", "Bình Lộc", "Bình Sơn", "Xuân Bình", "Xuân Tân"],
"Cẩm Mỹ": ["Cẩm Đường", "Lâm San", "Nhân Nghĩa", "Sông Nhạn", "Thừa Đức"],
"Định Quán": ["Định Quán", "La Ngà", "Ngọc Định", "Phú Cường", "Suối Nho"],
"Long Thành": ["Long Thành", "An Phước", "Bình An", "Bình Sơn", "Phước Bình"],
"Nhơn Trạch": ["Nhơn Trạch", "Đại Phước", "Hiệp Phước", "Long Thọ", "Phú Đông"],
"Tân Phú": ["Tân Phú", "Phú Bình", "Phú Điền", "Phú Lộc", "Thanh Sơn"],
"Thống Nhất": ["Thống Nhất", "Gia Tân", "Gia Kiệm", "Bàu Hàm", "Lộ 25"],
"Trảng Bom": ["Trảng Bom", "An Viễn", "Bàu Hàm", "Bình Minh", "Hưng Thịnh"],
"Vĩnh Cửu": ["Vĩnh Cửu", "Bình Lợi", "Bình Minh", "Hố Nai", "Thạnh Phú"],
"Xuân Lộc": ["Xuân Lộc", "Gia Ray", "Suối Cao", "Suối Cát", "Xuân Bắc"]
},
"Dong Thap": {
"Cao Lãnh": ["An Bình", "Bình Thạnh", "Hòa An", "Hòa Thành", "Phương Thịnh"],
"Sa Đéc": ["Tân Quy Tây", "Tân Phú Đông", "An Hòa", "Tân Khánh Đông"],
"Hồng Ngự": ["An Bình A", "An Bình B", "Long Khánh A", "Long Khánh B"],
"Châu Thành": ["An Hiệp", "An Nhơn", "Tân Bình", "Tân Nhuận Đông"],
"Hồng Ngự": ["Thường Thới Tiền", "Thường Phước 1", "Thường Phước 2"],
"Lai Vung": ["Lai Vung", "Hòa Long", "Long Hậu", "Tân Dương"],
"Lấp Vò": ["Định Yên", "Bình Thạnh Trung", "Tân Mỹ", "Tân Thành"],
"Tam Nông": ["An Long", "Hòa Bình", "Phú Thọ", "Tân Công Sính"],
"Tân Hồng": ["An Phước", "Phú Cường", "Tân Thành", "Thường Lạc"],
"Thanh Bình": ["Bình Tấn", "Tân Bình", "Phú Lợi", "Tân Long"],
"Tháp Mười": ["Mỹ An", "Mỹ Hòa", "Phú Điền", "Trường Xuân"]
},
"Gia Lai": {
"Pleiku": ["Hoa Lư", "Hoa Sen", "Hoa Thành", "Hoa Thủy"],
"An Khê": ["Cửu An", "Song An", "Thanh An", "Tây Sơn"],
"Ayun Pa": ["Cheo Reo", "Đức Cơ", "Đak Pơ"],
"Chư Păh": ["Hòa Phú", "Ia Nhin", "Ia Nhin", "Ia Khươl"],
"Chư Prông": ["Ia Drăng", "Ia Lâu", "Ia Me"],
"Chư Pưh": ["Pờ Tó", "Chư Don", "Ia Le"],
"Chư Sê": ["Ia Glai", "Ia Blang", "Ia Ko"],
"Đắk Đoa": ["Hà Bầu", "Hà Đông", "Đắk Sơmei"],
"Đắk Pơ": ["An Thành", "Hà Tam", "Tân Thành"],
"Đức Cơ": ["Ia Dêr", "Ia Pnôn", "Ia Nan"],
"Ia Grai": ["Ia Kha", "Ia Chía", "Ia Pếch"],
"Ia Pa": ["Chư Răng", "Ia Kriêng", "Ia Trok"],
"KBang": ["Sơ Ró", "Kon Pne", "Lơ Ku"],
"Kông Chro": ["An Trung", "Chơ Long", "Đak Pơ Pho"],
"Krông Pa": ["Chư Gu", "Phú Cần", "Uar"],
"Mang Yang": ["Kon Chiêng", "Ayun", "Đắk Trôi"],
"Phú Thiện": ["Ia Sol", "Chư A Thai", "Ia Peng"]
},
"Ha Giang": {
"Hà Giang": ["Ngọc Đường", "Minh Khai", "Quang Trung", "Kim Linh"],
"Bắc Mê": ["Đồng Yên", "Yên Phú", "Thượng Bình", "Lạc Nông"],
"Bắc Quang": ["Bằng Hành", "Đồng Tâm", "Đồng Yên"],
"Đồng Văn": ["Lũng Cú", "Sà Phìn", "Sính Lủng"],
"Hoàng Su Phì": ["Bản Luốc", "Bản Nhùng", "Túng Sán"],
"Mèo Vạc": ["Nậm Ban", "Pả Vi", "Tả Lủng"],
"Quản Bạ": ["Cao Mã Pờ", "Nậm Lý", "Tùng Vài"],
"Quang Bình": ["Bản Rịa", "Nậm Ban", "Nậm Ty"],
"Vị Xuyên": ["Bạch Ngọc", "Cao Bồ", "Phú Linh"],
"Xín Mần": ["Bản Díu", "Chí Cà", "Nấm Dẩn"],
"Yên Minh": ["Bạch Đích", "Du Già", "Mậu Duệ"]
},
"Ha Nam": {
"Phủ Lý": ["Liêm Chính", "Liêm Cần", "Thanh Tuyền"],
"Bình Lục": ["An Đổ", "Bồ Đề", "Tràng An"],
"Duy Tiên": ["Châu Giang", "Đồng Văn", "Hòa Mạc"],
"Kim Bảng": ["Ba Sao", "Hoàng Đông", "Lạc Tràng"],
"Lý Nhân": ["Bắc Lý", "Nhân Nghĩa", "Nhân Thịnh"],
"Thanh Liêm": ["Thanh Hà", "Thanh Nghị", "Liêm Phong"]
},
"Ha Tinh": {
"Hà Tĩnh": ["Nam Hà", "Tân Giang", "Thạch Linh"],
"Hồng Lĩnh": ["Đức Thuận", "Đậu Liêu", "Thuận Lộc"],
"Kỳ Anh": ["Kỳ Thịnh", "Kỳ Ninh", "Kỳ Phú"],
"Cẩm Xuyên": ["Cẩm Dương", "Cẩm Hà", "Cẩm Hòa"],
"Can Lộc": ["Đồng Lộc", "Khánh Lộc", "Sơn Lộc"],
"Đức Thọ": ["Bùi La Nhân", "Đức Thanh", "Trung Lễ"],
"Hương Khê": ["Gia Phố", "Hương Bình", "Phú Gia"],
"Hương Sơn": ["Sơn An", "Sơn Bằng", "Sơn Châu"],
"Kỳ Anh": ["Kỳ Sơn", "Kỳ Tây", "Kỳ Văn"],
"Lộc Hà": ["Bùi Xá", "Hồng Lộc", "Ích Hậu"],
"Nghi Xuân": ["Cương Gián", "Xuân Thành", "Xuân Trường"],
"Thạch Hà": ["Thạch Đài", "Thạch Hải", "Thạch Hạ"],
"Vũ Quang": ["Hương Minh", "Hương Thọ", "Vũ Quang"]
},
"Hai Duong": {
"Hải Dương": ["Bình Hàn", "Cẩm Thượng", "Đại Nãi", "Lê Thanh Nghị", "Quang Trung"],
"Chí Linh": ["An Lạc", "Cao Thắng", "Chí Linh", "Phả Lại", "Thái Học"],
"Bình Giang": ["Bình Minh", "Cổ Bì", "Hồng Khê", "Tân Hồng"],
"Cẩm Giàng": ["Cẩm Giàng", "Lai Cách", "Lương Điền", "Ngọc Liên"],
"Gia Lộc": ["Đồng Tâm", "Gia Khánh", "Gia Tân", "Phương Hưng"],
"Kim Thành": ["Cộng Hòa", "Kim Xuyên", "Liên Hòa", "Ngũ Phúc"],
"Kinh Môn": ["An Sinh", "Bạch Đằng", "Hiệp An", "Kinh Môn"],
"Nam Sách": ["An Bình", "Hiệp Cát", "Nam Chính", "Thanh Quang"],
"Ninh Giang": ["An Đức", "Đông Xuyên", "Hiệp Lực", "Ninh Giang"],
"Thanh Hà": ["Cẩm Chế", "Thanh Bính", "Thanh Giang", "Thanh Hồng"],
"Thanh Miện": ["Chi Lăng Bắc", "Đoàn Tùng", "Hồng Quang", "Thanh Miện"],
"Tứ Kỳ": ["An Thanh", "Cộng Lạc", "Đại Hợp", "Quảng Nghiệp"]
},
"Hau Giang": {
"Vị Thanh": ["I", "IV", "V", "VII"],
"Ngã Bảy": ["Hiệp Lợi", "Hiệp Thành", "Lái Hiếu", "Ngã Bảy"],
"Châu Thành": ["Đông Phước", "Phú Hữu", "Phú Tân", "Tân Phú Thạnh"],
"Châu Thành A": ["Bảy Ngàn", "Cái Tắc", "Tân Hòa", "Thạnh Xuân"],
"Long Mỹ": ["Long Bình", "Long Trị", "Long Phú", "Vĩnh Viễn"],
"Phụng Hiệp": ["Búng Tàu", "Cây Dương", "Hòa Mỹ", "Phụng Hiệp"],
"Vị Thủy": ["Vĩnh Thuận", "Vị Đông", "Vị Thanh", "Vị Trung"]
},
"Hoa Binh": {
"Hòa Bình": ["Đồng Tâm", "Hòa Bình", "Thịnh Lang", "Tân Hòa"],
"Cao Phong": ["Bắc Sơn", "Bình Thanh", "Nam Phong", "Tân Phong"],
"Đà Bắc": ["Đoàn Kết", "Hiền Lương", "Hòa Bình", "Toàn Sơn"],
"Kim Bôi": ["Kim Bôi", "Sào Báy", "Vĩnh Tiến"],
"Lạc Sơn": ["Hương Nhượng", "Thạch Yên", "Yên Phú"],
"Lạc Thủy": ["Cao Thượng", "Thượng Bình", "Yên Bồng"],
"Lương Sơn": ["Cao Răm", "Nhuận Trạch", "Thanh Lương"],
"Mai Châu": ["Chiềng Châu", "Đồng Tân", "Tòng Đậu"],
"Tân Lạc": ["Nam Sơn", "Phú Cường", "Tử Nê"],
"Yên Thủy": ["Hưng Thi", "Ngọc Lương", "Lạc Lương"]
},
"Hung Yen": {
"Hưng Yên": ["An Tảo", "Hiến Nam", "Hồng Châu"],
"Ân Thi": ["Bắc Sơn", "Hoàng Hanh", "Quảng Lãng"],
"Khoái Châu": ["An Vĩ", "Đồng Tiến", "Thành Công"],
"Kim Động": ["Lệ Xá", "Vũ Xá", "Song Mai"],
"Mỹ Hào": ["Bạch Sam", "Bần Yên Nhân", "Phùng Chí Kiên"],
"Phù Cừ": ["Đoàn Đào", "Đông Tảo", "Phan Sào Nam"],
"Tiên Lữ": ["Dị Chế", "Đức Thắng", "Nhân Hoà"],
"Văn Giang": ["Cửu Cao", "Mễ Sở", "Xuân Quan"],
"Văn Lâm": ["Đình Dù", "Lạc Hồng", "Minh Hải"],
"Yên Mỹ": ["Đồng Than", "Liêu Xá", "Yên Phú"]
},
"Khanh Hoa": {
"Nha Trang": ["Phước Long", "Phước Hòa", "Vạn Thắng"],
"Cam Ranh": ["Cam Lộc", "Cam Phúc Bắc", "Cam Thịnh Đông"],
"Ninh Hòa": ["Ninh Bình", "Ninh Hải", "Ninh Hòa"],
"Diên Khánh": ["Diên An", "Diên Bình", "Diên Toàn"],
"Khánh Sơn": ["Ba Cụm Bắc", "Ba Cụm Nam"],
"Khánh Vĩnh": ["Cầu Bà", "Khánh Bình"],
"Trường Sa": ["Song Tử Tây", "Sinh Tồn"],
"Vạn Ninh": ["Đại Lãnh", "Vạn Hưng"]
},
"Kien Giang": {
"Rạch Giá": ["An Hòa", "Rạch Sỏi", "Vĩnh Hiệp"],
"Hà Tiên": ["Bình San", "Mỹ Đức", "Thuận Yên"],
"Giang Thành": ["Phú Lợi", "Phú Mỹ", "Vĩnh Phú"],
"An Biên": ["Nam Thái", "Tây Yên", "Thạnh Yên"],
"An Minh": ["Đông Hưng", "Tân Thuận", "Thuận Hoà"],
"Châu Thành": ["Giục Tượng", "Minh Hoà", "Vĩnh Hoà"],
"Giồng Riềng": ["Bàn Thạch", "Hoà Thuận", "Ngọc Chúc"],
"Gò Quao": ["Thủy Liễu", "Vĩnh Hòa", "Vĩnh Phước A"],
"Hòn Đất": ["Bình Giang", "Sóc Sơn", "Thổ Sơn"],
"Kiên Hải": ["An Sơn", "Hòn Tre", "Lại Sơn"],
"Kiên Lương": ["Bình An", "Bình Trị", "Hòn Nghệ"],
"Phú Quốc": ["An Thới", "Dương Đông", "Gành Dầu"],
"Tân Hiệp": ["Tân An", "Tân Hòa", "Thạnh Trị"],
"U Minh Thượng": ["An Minh Bắc", "Minh Thuận", "Thạnh Yên A"],
"Vĩnh Thuận": ["Vĩnh Bình Nam", "Vĩnh Phong", "Vĩnh Thuận"]
},
"Kon Tum": {
"Kon Tum": ["Duy Tân", "Ngọc Bay", "Quyết Thắng", "Thắng Lợi"],
"Đắk Glei": ["Đắk Choong", "Đắk Man", "Đắk Pék"],
"Đắk Hà": ["Đắk Long", "Đắk Mar", "Đắk PXi"],
"Đắk Tô": ["Diên Bình", "Đắk Rơ Nga", "Ngọc Tụ"],
"Ia H'Drai": ["Ia Dal", "Ia Dom", "Ia Tơi"],
"Kon Plông": ["Đắk Rinh", "Măng Bút", "Măng Cành"],
"Kon Rẫy": ["Đắk Ruồng", "Đắk Tờ Re", "Tân Lập"],
"Ngọc Hồi": ["Đắk Ang", "Đắk Dục", "Pờ Y"],
"Sa Thầy": ["Hơ Moong", "Mô Rai", "Sa Sơn"],
"Tu Mơ Rông": ["Đắk Hà", "Ngọc Lây", "Tê Xăng"]
},
"Lai Chau": {
"Lai Châu": ["Đoàn Kết", "Nậm Loỏng", "Quyết Thắng"],
"Mường Tè": ["Mường Tè", "Pa Ủ", "Pa Vệ Sử"],
"Nậm Nhùn": ["Nậm Hàng", "Nậm Manh", "Nậm Pì"],
"Phong Thổ": ["Bản Lang", "Hoang Thèn", "Mường So"],
"Sìn Hồ": ["Căn Co", "Làng Mô", "Phăng Sô Lin"],
"Tam Đường": ["Bình Lư", "Nà Tăm", "Sơn Bình"],
"Tân Uyên": ["Mường Khoa", "Phúc Khoa", "Thân Thuộc"],
"Than Uyên": ["Hua Nà", "Mường Cang", "Phúc Than"]
},
"Lam Dong": {
"Đà Lạt": ["Đa Lộc", "Liên Khương", "Phường 1", "Phường 2"],
"Bảo Lộc": ["B'Lao", "Đạm Bri", "Lộc Phát"],
"Bảo Lâm": ["Lộc Bảo", "Lộc Bắc", "Lộc Đức"],
"Cát Tiên": ["Cát Lâm", "Cát Tiên", "Phước Cát"],
"Di Linh": ["Đinh Trang Hòa", "Gia Hiệp", "Hòa Nam"],
"Đạ Huoai": ["Đạ M’ri", "Đạ Tồn", "Ma Đa Guôi"],
"Đạ Tẻh": ["An Nhơn", "Mỹ Đức", "Quốc Oai"],
"Đam Rông": ["Đạ K’Nàng", "Đạ Rsal", "Đạ Tông"],
"Đơn Dương": ["Ka Đô", "Lạc Lâm", "Quảng Lập"],
"Đức Trọng": ["Bình Thạnh", "Đa Quyn", "Hiệp An"],
"Lạc Dương": ["Đạ Chais", "Đạ Nhim", "Lát"],
"Lâm Hà": ["Đạ Đờn", "Đan Phượng", "Phi Tô"]
},
"Lang Son": {
"Lạng Sơn": ["Chi Lăng", "Hoàng Đồng", "Vĩnh Trại"],
"Bắc Sơn": ["Bắc Sơn", "Chiến Thắng", "Hưng Vũ"],
"Bình Gia": ["Bình La", "Hoa Thám", "Quý Hòa"],
"Cao Lộc": ["Bảo Lâm", "Cao Lâu", "Xuân Long"],
"Chi Lăng": ["Bằng Hữu", "Bắc Thủy", "Thái Học"],
"Đình Lập": ["Bắc Lãng", "Cường Lợi", "Thái Bình"],
"Hữu Lũng": ["Cai Kinh", "Đồng Tiến", "Hữu Liên"],
"Lộc Bình": ["Hữu Khánh", "Lợi Bác", "Tú Đoạn"],
"Tràng Định": ["Bình Yên", "Đề Thám", "Tân Minh"],
"Văn Lãng": ["Bắc La", "Hoàng Văn Thụ", "Trùng Khánh"],
"Văn Quan": ["An Sơn", "Bình Phúc", "Trấn Ninh"]
},
"Lao Cai": {
"Lào Cai": ["Bắc Cường", "Bắc Lệnh", "Kim Tân"],
"Bát Xát": ["A Mú Sung", "A Lù", "Nậm Pung"],
"Bảo Thắng": ["Bản Cầm", "Bản Phiệt", "Xuân Quang"],
"Bảo Yên": ["Cam Cọn", "Điện Quan", "Yên Sơn"],
"Bắc Hà": ["Bảo Nhai", "Cốc Ly", "Tả Van Chư"],
"Mường Khương": ["Bản Lầu", "La Pan Tẩn", "Nậm Chảy"],
"Sa Pa": ["Lao Chải", "Tả Phìn", "Trung Chải"],
"Si Ma Cai": ["Cán Cấu", "Quan Hồ Thẩn", "Sán Chải"],
"Văn Bàn": ["Chiềng Ken", "Dương Quỳ", "Nậm Xây"]
},
"Long An": {
"Tân An": ["Khánh Hậu", "Nhơn Thạnh Trung", "Phường 1"],
"Bến Lức": ["An Thạnh", "Lương Bình", "Thạnh Lợi"],
"Cần Đước": ["Long Hựu Đông", "Phước Đông", "Tân Lân"],
"Cần Giuộc": ["Long Hậu", "Phước Lại", "Trường Bình"],
"Châu Thành": ["An Lục Long", "Phú Ngãi Trị", "Vĩnh Công"],
"Đức Hòa": ["An Ninh Đông", "Hòa Khánh Tây", "Hiệp Hòa"],
"Đức Huệ": ["Mỹ Bình", "Mỹ Thạnh Tây", "Thạnh Lợi"],
"Mộc Hóa": ["Bình Hòa Đông", "Bình Phong Thạnh", "Nhơn Hòa"],
"Tân Hưng": ["Hưng Điền", "Thạnh Hưng", "Vĩnh Thạnh"],
"Tân Thạnh": ["Bắc Hòa", "Tân Bình", "Tân Lập"],
"Tân Trụ": ["An Nhựt Tân", "Tân Phước Tây", "Tân Trụ"],
"Thạnh Hóa": ["Thạnh An", "Thạnh Phước", "Thủy Đông"],
"Thủ Thừa": ["Bình An", "Long Thạnh", "Nhị Thành"],
"Vĩnh Hưng": ["Hưng Điền A", "Khánh Hưng", "Thái Trị"]
},
"Nam Dinh": {
"Nam Định": ["Cửa Bắc", "Cửa Nam", "Hạ Long", "Lộc Vượng"],
"Giao Thủy": ["Giao An", "Giao Châu", "Giao Hải"],
"Hải Hậu": ["Hải Anh", "Hải Châu", "Hải Đường"],
"Mỹ Lộc": ["Mỹ Hà", "Mỹ Hưng", "Mỹ Phúc"],
"Nam Trực": ["Nam Dương", "Nam Hùng", "Nam Lợi"],
"Nghĩa Hưng": ["Nghĩa Bình", "Nghĩa Hồng", "Nghĩa Minh"],
"Trực Ninh": ["Trực Cát", "Trực Đại", "Trực Hưng"],
"Vụ Bản": ["Hiển Khánh", "Liên Bảo", "Quang Trung"],
"Xuân Trường": ["Xuân Bắc", "Xuân Hồng", "Xuân Thượng"],
"Ý Yên": ["Yên Bình", "Yên Chính", "Yên Cường"]
},
"Nghe An": {
"Vinh": ["Cửa Nam", "Đội Cung", "Hồng Sơn"],
"Cửa Lò": ["Nghi Hải", "Nghi Hòa", "Nghi Tân"],
"Hoàng Mai": ["Mai Hùng", "Quỳnh Dị", "Quỳnh Lộc"],
"Thái Hòa": ["Long Sơn", "Nghĩa Mỹ", "Nghĩa Thuận"],
"Anh Sơn": ["Cẩm Sơn", "Đỉnh Sơn", "Tường Sơn"],
"Con Cuông": ["Bồng Khê", "Cam Lâm", "Chi Khê"],
"Diễn Châu": ["Diễn An", "Diễn Bích", "Diễn Hạnh"],
"Đô Lương": ["Đà Sơn", "Giang Sơn Đông", "Lạc Sơn"],
"Hưng Nguyên": ["Hưng Châu", "Hưng Đạo", "Hưng Lam"],
"Kỳ Sơn": ["Bắc Lý", "Bảo Nam", "Đoọc Mạy"],
"Nam Đàn": ["Kim Liên", "Nam Cường", "Nam Giang"],
"Nghi Lộc": ["Nghi Công Bắc", "Nghi Diên", "Nghi Hợp"],
"Nghĩa Đàn": ["Nghĩa An", "Nghĩa Bình", "Nghĩa Hưng"],
"Quế Phong": ["Cắm Muộn", "Châu Kim", "Hạnh Dịch"],
"Quỳ Châu": ["Châu Bính", "Châu Hạnh", "Châu Nga"],
"Quỳ Hợp": ["Châu Cường", "Châu Đình", "Châu Lý"],
"Quỳnh Lưu": ["Quỳnh Bá", "Quỳnh Châu", "Quỳnh Đôi"],
"Tân Kỳ": ["Tân An", "Tân Hương", "Tân Phú"],
"Tương Dương": ["Lượng Minh", "Mai Sơn", "Nga My"],
"Yên Thành": ["Bắc Thành", "Công Thành", "Đồng Thành"]
},
"Ninh Binh": {
"Ninh Bình": ["Bích Đào", "Đông Thành", "Nam Bình"],
"Tam Điệp": ["Bắc Sơn", "Nam Sơn", "Tân Bình"],
"Gia Viễn": ["Gia Hòa", "Gia Hưng", "Gia Lạc"],
"Hoa Lư": ["Ninh An", "Ninh Hải", "Ninh Thắng"],
"Kim Sơn": ["Kim Chính", "Kim Đông", "Kim Hải"],
"Nho Quan": ["Gia Lâm", "Lạc Vân", "Phú Lộc"],
"Yên Khánh": ["Khánh An", "Khánh Cư", "Khánh Hải"],
"Yên Mô": ["Mai Sơn", "Yên Hòa", "Yên Lâm"]
},
"Ninh Thuan": {
"Phan Rang - Tháp Chàm": ["Đô Vinh", "Kinh Dinh", "Tấn Tài"],
"Bác Ái": ["Phước Bình", "Phước Đại", "Phước Hòa"],
"Ninh Hải": ["Hộ Hải", "Nhơn Hải", "Tân Hải"],
"Ninh Phước": ["An Hải", "Phước Dân", "Phước Hậu"],
"Ninh Sơn": ["Hòa Sơn", "Hòa Thành", "Lâm Sơn"],
"Thuận Bắc": ["Bắc Phong", "Bắc Sơn", "Lợi Hải"],
"Thuận Nam": ["Cà Ná", "Phước Hà", "Phước Nam"]
},
"Phu Tho": {
"Việt Trì": ["Bạch Hạc", "Gia Cẩm", "Vân Cơ"],
"Phú Thọ": ["Hùng Vương", "Phong Châu", "Thanh Đình"],
"Cẩm Khê": ["Cẩm Đàn", "Cấp Dẫn", "Phú Khê"],
"Đoan Hùng": ["Chân Mộng", "Hùng Xuyên", "Phương Trung"],
"Hạ Hòa": ["Gia Điền", "Hà Lương", "Linh Giang"],
"Lâm Thao": ["Cao Xá", "Hợp Hải", "Sơn Vi"],
"Phù Ninh": ["An Đạo", "Lệ Mỹ", "Phú Lộc"],
"Tam Nông": ["Hiền Quan", "Quang Húc", "Thanh Uyên"],
"Tân Sơn": ["Kiệt Sơn", "Minh Đài", "Tân Phú"],
"Thanh Ba": ["Đông Lĩnh", "Hoàng Cương", "Quảng Yên"],
"Thanh Sơn": ["Cự Đồng", "Địch Quả", "Lê Lợi"],
"Thanh Thủy": ["Bảo Yên", "Đoan Hạ", "Yến Mao"],
"Yên Lập": ["Đồng Thịnh", "Hưng Long", "Lương Sơn"]
},
"Quang Binh": {
"Đồng Hới": ["Bắc Lý", "Đức Ninh Đông", "Nam Lý"],
"Ba Đồn": ["Quảng Long", "Quảng Phong", "Quảng Thuận"],
"Bố Trạch": ["Hải Phú", "Hòa Trạch", "Nhân Trạch"],
"Lệ Thủy": ["An Thủy", "Hoa Thủy", "Mai Thủy"],
"Minh Hóa": ["Dân Hóa", "Hóa Hợp", "Hồng Hóa"],
"Quảng Ninh": ["An Ninh", "Duy Ninh", "Hiền Ninh"],
"Quảng Trạch": ["Cảnh Dương", "Quảng Đông", "Quảng Hòa"],
"Tuyên Hóa": ["Cao Quảng", "Châu Hóa", "Lâm Hóa"]
},
"Quang Nam": {
"Tam Kỳ": ["An Sơn", "An Xuân", "Hòa Hương"],
"Hội An": ["Cẩm An", "Cẩm Châu", "Cẩm Hà"],
"Đại Lộc": ["Ái Nghĩa", "Đại An", "Đại Cường"],
"Điện Bàn": ["Điện An", "Điện Dương", "Điện Minh"],
"Đông Giang": ["A Rooi", "Jơ Ngây", "Sông Kôn"],
"Duy Xuyên": ["Duy An", "Duy Châu", "Duy Hải"],
"Hiệp Đức": ["Bình Lâm", "Hiệp Hòa", "Phước Gia"],
"Nam Giang": ["Cà Dy", "Đắc Pre", "Tà Bhing"],
"Nam Trà My": ["Trà Cang", "Trà Don", "Trà Mai"],
"Nông Sơn": ["Quế Lộc", "Quế Ninh", "Sơn Viên"],
"Núi Thành": ["Tam Anh", "Tam Giang", "Tam Hải"],
"Phú Ninh": ["Tam Dân", "Tam Lãnh", "Tam Phước"],
"Phước Sơn": ["Phước Chánh", "Phước Công", "Phước Lộc"],
"Quế Sơn": ["Đông Phú", "Hương An", "Phú Thọ"],
"Tây Giang": ["A Xan", "A Nông", "Lăng"],
"Thăng Bình": ["Bình An", "Bình Chánh", "Bình Hải"],
"Tiên Phước": ["Tiên Cảnh", "Tiên Hiệp", "Tiên Kỳ"]
},
"Quang Ngai": {
"Quảng Ngãi": ["Nghĩa Chánh", "Quảng Phú", "Trần Phú"],
"Ba Tơ": ["Ba Bích", "Ba Chùa", "Ba Điền"],
"Bình Sơn": ["Bình An", "Bình Châu", "Bình Đông"],
"Đức Phổ": ["Phổ An", "Phổ Cường", "Phổ Minh"],
"Lý Sơn": ["An Bình", "An Hải", "An Vĩnh"],
"Minh Long": ["Long Hiệp", "Long Mai", "Thanh An"],
"Mộ Đức": ["Đức Chánh", "Đức Hiệp", "Đức Phong"],
"Nghĩa Hành": ["Hành Đức", "Hành Dũng", "Hành Minh"],
"Sơn Hà": ["Sơn Bao", "Sơn Cao", "Sơn Hạ"],
"Sơn Tây": ["Sơn Dung", "Sơn Liên", "Sơn Mùa"],
"Sơn Tịnh": ["Tịnh An", "Tịnh Bắc", "Tịnh Châu"],
"Tây Trà": ["Trà Khê", "Trà Lãnh", "Trà Thanh"],
"Trà Bồng": ["Trà Bùi", "Trà Giang", "Trà Hiệp"],
"Tư Nghĩa": ["Nghĩa An", "Nghĩa Điền", "Nghĩa Hiệp"]
},
"Quang Ninh": {
"Hạ Long": ["Bạch Đằng", "Cao Thắng", "Hồng Hà"],
"Cẩm Phả": ["Cẩm Bình", "Cẩm Phú", "Cẩm Sơn"],
"Móng Cái": ["Bình Ngọc", "Hải Đông", "Ka Long"],
"Uông Bí": ["Bắc Sơn", "Nam Khê", "Quang Trung"],
"Bình Liêu": ["Đồng Tâm", "Húc Động", "Vô Ngại"],
"Ba Chẽ": ["Đạp Thanh", "Lương Mông", "Nam Sơn"],
"Cô Tô": ["Cô Tô", "Thanh Lân"],
"Đầm Hà": ["Đầm Hà", "Quảng Lợi", "Tân Bình"],
"Đông Triều": ["An Sinh", "Bình Khê", "Thủy An"],
"Hải Hà": ["Quảng An", "Quảng Chính", "Quảng Đức"],
"Hoành Bồ": ["Bằng Cả", "Đồng Lâm", "Quảng La"],
"Quảng Yên": ["Cẩm La", "Đông Mai", "Hà An"],
"Tiên Yên": ["Đại Dực", "Đại Thành", "Tiên Lãng"],
"Vân Đồn": ["Bản Sen", "Bình Dân", "Đoàn Kết"]
},
"Quang Tri": {
"Đông Hà": ["Đông Lễ", "Đông Lương", "Phường 1"],
"Quảng Trị": ["An Đôn", "Phường 1", "Phường 2"],
"Cam Lộ": ["Cam An", "Cam Hiếu", "Cam Thành"],
"Cồn Cỏ": ["Cồn Cỏ"],
"Đa Krông": ["A Bung", "A Ngo", "Hướng Hiệp"],
"Gio Linh": ["Gio An", "Gio Châu", "Gio Hải"],
"Hải Lăng": ["Hải An", "Hải Ba", "Hải Chánh"],
"Hướng Hóa": ["Húc", "Hướng Lộc", "Lìa"],
"Triệu Phong": ["Triệu Ái", "Triệu An", "Triệu Độ"],
"Vĩnh Linh": ["Hiền Thành", "Kim Thạch", "Vĩnh Chấp"]
},
"Soc Trang": {
"Sóc Trăng": ["Khánh Hòa", "Phường 1", "Phường 2"],
"Châu Thành": ["An Hiệp", "An Ninh", "An Thạnh"],
"Cù Lao Dung": ["An Thạnh 1", "An Thạnh 2", "An Thạnh Đông"],
"Kế Sách": ["An Lạc Tây", "An Mỹ", "Ba Trinh"],
"Long Phú": ["Châu Khánh", "Đại Ân", "Hậu Thạnh"],
"Mỹ Tú": ["Hưng Phú", "Long Hưng", "Mỹ Hương"],
"Mỹ Xuyên": ["Đại Tâm", "Gia Hòa 1", "Gia Hòa 2"],
"Ngã Năm": ["Phường 1", "Phường 2", "Vĩnh Quới"],
"Thạnh Trị": ["Châu Hưng", "Hưng Lợi", "Thạnh Lợi"],
"Trần Đề": ["Đại Ân 2", "Lịch Hội Thượng", "Thạnh Thới An"],
"Vĩnh Châu": ["Hòa Đông", "Lạc Hòa", "Vĩnh Hiệp"]
},
"Son La": {
"Sơn La": ["Chiềng An", "Chiềng Cơi", "Chiềng Đen"],
"Bắc Yên": ["Chim Vàn", "Hang Chú", "Hồng Ngài"],
"Mai Sơn": ["Chiềng Ban", "Chiềng Chăn", "Chiềng Chung"],
"Mộc Châu": ["Chiềng Hắc", "Chiềng Khừa", "Đông Sang"],
"Mường La": ["Chiềng Ân", "Chiềng Công", "Chiềng Hoa"],
"Phù Yên": ["Gia Phù", "Huy Bắc", "Huy Hạ"],
"Quỳnh Nhai": ["Chiềng Bằng", "Chiềng Khay", "Pá Ma Pha Khinh"],
"Sông Mã": ["Chiềng Cang", "Chiềng En", "Chiềng Khoong"],
"Sốp Cộp": ["Dồm Cang", "Mường Lèo", "Púng Bánh"],
"Thuận Châu": ["Bon Phặng", "Bó Mười", "Chiềng Bôm"],
"Vân Hồ": ["Chiềng Khoa", "Chiềng Xuân", "Liên Hòa"],
"Yên Châu": ["Chiềng Đông", "Chiềng Hặc", "Lóng Phiêng"]
},
"Tay Ninh": {
"Tây Ninh": ["Hiệp Ninh", "Ninh Sơn", "Ninh Thạnh"],
"Bến Cầu": ["An Thạnh", "Lợi Thuận", "Long Chữ"],
"Châu Thành": ["An Cơ", "Biên Giới", "Hảo Đước"],
"Dương Minh Châu": ["Bàu Năng", "Cầu Khởi", "Chà Là"],
"Gò Dầu": ["Bàu Đồn", "Hiệp Thạnh", "Phước Đông"],
"Hòa Thành": ["Long Thành Bắc", "Long Thành Nam", "Long Thành Trung"],
"Tân Biên": ["Hòa Hiệp", "Mỏ Công", "Tân Bình"],
"Tân Châu": ["Suối Dây", "Suối Ngô", "Tân Đông"],
"Trảng Bàng": ["An Hòa", "Gia Bình", "Gia Lộc"]
},
"Thai Binh": {
"Thái Bình": ["Đề Thám", "Hoàng Diệu", "Kỳ Bá"],
"Đông Hưng": ["An Châu", "Đông Á", "Đông Các"],
"Hưng Hà": ["Bắc Sơn", "Canh Tân", "Chi Lăng"],
"Kiến Xương": ["An Bình", "Bình Định", "Hồng Tiến"],
"Quỳnh Phụ": ["An Bài", "An Ấp", "An Dục"],
"Thái Thụy": ["Thụy Bình", "Thụy Chính", "Thụy Dân"],
"Tiền Hải": ["Đông Cơ", "Đông Hoàng", "Đông Lâm"],
"Vũ Thư": ["Bách Thuận", "Dũng Nghĩa", "Hiệp Hòa"]
},
"Thai Nguyen": {
"Thái Nguyên": ["Cam Giá", "Gia Sàng", "Hoàng Văn Thụ"],
"Sông Công": ["Bình Sơn", "Cải Đan", "Lương Châu"],
"Phổ Yên": ["Bãi Bông", "Ba Hàng", "Đắc Sơn"],
"Đại Từ": ["Bản Ngoại", "Bình Thuận", "Cù Vân"],
"Định Hóa": ["Bảo Cường", "Bảo Linh", "Bộc Nhiêu"],
"Đồng Hỷ": ["Cây Thị", "Hóa Thượng", "Khe Mo"],
"Phú Bình": ["Bàn Đạt", "Bảo Lý", "Đào Xá"],
"Phú Lương": ["Cổ Lũng", "Động Đạt", "Hợp Thành"],
"Võ Nhai": ["Cúc Đường", "Dân Tiến", "La Hiên"]
},
"Thanh Hoa": {
"Thanh Hóa": ["An Hưng", "Đông Hải", "Đông Hương"],
"Bỉm Sơn": ["Ba Đình", "Bắc Sơn", "Đông Sơn"],
"Sầm Sơn": ["Bắc Sơn", "Quảng Châu", "Trường Sơn"],
"Ba Thước": ["Ái Thượng", "Ban Công", "Cổ Lũng"],
"Cẩm Thủy": ["Cẩm Bình", "Cẩm Giang", "Cẩm Liên"],
"Đông Sơn": ["Đông Hoàng", "Đông Minh", "Đông Nam"],
"Hà Trung": ["Hà Bình", "Hà Đông", "Hà Giang"],
"Hậu Lộc": ["Đa Lộc", "Đồng Lộc", "Hòa Lộc"],
"Hoằng Hóa": ["Hoằng Đại", "Hoằng Đạo", "Hoằng Đạt"],
"Lang Chánh": ["Giao An", "Giao Thiện", "Tam Văn"],
"Mường Lát": ["Mường Chanh", "Pù Nhi", "Quang Chiểu"],
"Nga Sơn": ["Nga An", "Nga Bạch", "Nga Điền"],
"Ngọc Lặc": ["Cao Ngọc", "Kiên Thọ", "Lam Sơn"],
"Như Thanh": ["Cán Khê", "Hải Long", "Mậu Lâm"],
"Như Xuân": ["Bãi Trành", "Cát Tân", "Hóa Quỳ"],
"Nông Cống": ["Cầu Quan", "Công Chính", "Hoàng Sơn"],
"Quan Hóa": ["Hiền Chung", "Hiền Kiệt", "Nam Động"],
"Quan Sơn": ["Mường Mìn", "Na Mèo", "Sơn Điện"],
"Quảng Xương": ["Quảng Bình", "Quảng Chính", "Quảng Định"],
"Thạch Thành": ["Thạch Bình", "Thạch Cẩm", "Thạch Định"],
"Thiệu Hóa": ["Thiệu Châu", "Thiệu Chính", "Thiệu Công"],
"Thọ Xuân": ["Bắc Lương", "Nam Giang", "Phúc Thịnh"],
"Thường Xuân": ["Bát Mọt", "Luận Khê", "Ngọc Phụng"],
"Triệu Sơn": ["An Nông", "Dân Lực", "Dân Quyền"],
"Vĩnh Lộc": ["Vĩnh An", "Vĩnh Hòa", "Vĩnh Hùng"],
"Yên Định": ["Định Bình", "Định Hải", "Định Hòa"]
},
"Thua Thien Hue": {
"Huế": ["An Cựu", "An Đông", "An Hòa"],
"A Lưới": ["A Đớt", "Bắc Sơn", "Hồng Bắc"],
"Hương Trà": ["Bình Thành", "Bình Tiến", "Bình Thanh"],
"Hương Thủy": ["Phú Bài", "Phú Sơn", "Thủy An"],
"Nam Đông": ["Hương Giang", "Hương Hòa", "Thượng Lộ"],
"Phong Điền": ["Điền An", "Điền Hòa", "Điền Hải"],
"Phú Lộc": ["Lộc An", "Lộc Bình", "Lộc Bổn"],
"Phú Vang": ["Phú An", "Phú Diên", "Phú Dương"],
"Quảng Điền": ["Quảng An", "Quảng Công", "Quảng Lợi"]
},
"Tien Giang": {
"Mỹ Tho": ["Mỹ Phước", "Tân Long", "Thới Sơn"],
"Cai Lậy": ["Bình Phú", "Cẩm Sơn", "Hậu Mỹ Bắc A"],
"Gò Công": ["Bình Đông", "Bình Xuân", "Long Hưng"],
"Cái Bè": ["An Cư", "An Hữu", "An Thái Đông"],
"Châu Thành": ["Bàn Long", "Hữu Đạo", "Kim Sơn"],
"Chợ Gạo": ["An Thạnh Thủy", "Bình Ninh", "Bình Phan"],
"Gò Công Đông": ["Bình Ân", "Gia Thuận", "Kiểng Phước"],
"Gò Công Tây": ["Bình Nhì", "Đồng Thạnh", "Thạnh Nhựt"],
"Tân Phú Đông": ["Phú Đông", "Phú Tân", "Tân Phú"],
"Tân Phước": ["Mỹ Phước", "Phú Mỹ", "Thạnh Hòa"]
},

"Tra Vinh": {
"Trà Vinh": ["Phường 1", "Phường 2", "Phường 3", "Phường 4"],
"Càng Long": ["An Trường", "An Trường A", "Đại Phúc"],
"Cầu Kè": ["An Phú Tân", "Châu Điền", "Hòa Ân"],
"Cầu Ngang": ["Hiệp Mỹ Đông", "Hiệp Mỹ Tây", "Long Sơn"],
"Châu Thành": ["Đa Lộc", "Hòa Lợi", "Hòa Minh"],
"Duyên Hải": ["Dân Thành", "Hiệp Thạnh", "Long Khánh"],
"Tiểu Cần": ["Hiếu Tử", "Hiếu Trung", "Hùng Hòa"],
"Trà Cú": ["An Quảng Hữu", "Đại An", "Định An"]
},
"Tuyen Quang": {
"Tuyên Quang": ["An Tường", "Đội Cấn", "Lưỡng Vượng"],
"Chiêm Hóa": ["Bình Nhân", "Bình Phú", "Hùng Mỹ"],
"Hàm Yên": ["Bạch Xa", "Bằng Cốc", "Nhân Mục"],
"Lâm Bình": ["Bình An", "Hồng Quang", "Phúc Sơn"],
"Na Hang": ["Côn Lôn", "Đà Vị", "Năng Khả"],
"Sơn Dương": ["Bình Yên", "Cấp Tiến", "Chi Thiết"],
"Yên Sơn": ["Hoàng Khai", "Lang Quán", "Mỹ Bằng"]
},
"Tuyen Quang": {
"Tuyên Quang": ["An Tường", "Đội Cấn", "Lưỡng Vượng"],
"Chiêm Hóa": ["Bình Nhân", "Bình Phú", "Hùng Mỹ"],
"Hàm Yên": ["Bạch Xa", "Bằng Cốc", "Nhân Mục"],
"Lâm Bình": ["Bình An", "Hồng Quang", "Phúc Sơn"],
"Na Hang": ["Côn Lôn", "Đà Vị", "Năng Khả"],
"Sơn Dương": ["Bình Yên", "Cấp Tiến", "Chi Thiết"],
"Yên Sơn": ["Hoàng Khai", "Lang Quán", "Mỹ Bằng"]
},
"Vinh Long": {
"Vĩnh Long": ["Phường 1", "Phường 2", "Phường 3", "Phường 4"],
"Bình Minh": ["Cái Vồn", "Đông Bình", "Đông Thành"],
"Bình Tân": ["Mỹ Thuận", "Ngãi Tứ", "Tân An Thạnh"],
"Long Hồ": ["An Bình", "Bình Hòa Phước", "Đồng Phú"],
"Mang Thít": ["Chánh An", "Hòa Tịnh", "Mỹ An"],
"Tam Bình": ["Hòa Hiệp", "Hòa Lộc", "Loan Mỹ"],
"Trà Ôn": ["Hòa Bình", "Hòa Hiệp", "Thới Hòa"],
"Vũng Liêm": ["Hiếu Nghĩa", "Hiếu Nhơn", "Trung Hiệp"]
},
"Vinh Phuc": {
"Vĩnh Yên": ["Đống Đa", "Đồng Tâm", "Hội Hợp"],
"Phúc Yên": ["Cao Minh", "Đồng Xuân", "Phúc Thắng"],
"Bình Xuyên": ["Bá Hiến", "Đạo Đức", "Hương Canh"],
"Lập Thạch": ["Bàn Giản", "Đình Chu", "Triệu Đề"],
"Sông Lô": ["Bạch Lưu", "Đồng Quế", "Lãng Công"],
"Tam Đảo": ["Đạo Trù", "Hợp Châu", "Tam Quan"],
"Tam Dương": ["An Hòa", "Duy Phiên", "Hoàng Đan"],
"Vĩnh Tường": ["Bình Dương", "Chấn Hưng", "Kim Xá"],
"Yên Lạc": ["Đại Tự", "Đồng Văn", "Hồng Phương"]
},
"Yen Bai": {
"Yên Bái": ["Phường Đồng Tâm", "Phường Minh Tân", "Phường Nguyễn Thái Học", "Xã Giới Phiên"],
"Nghĩa Lộ": ["Phường Trung Tâm", "Xã Nghĩa Lợi", "Xã Nghĩa Phúc", "Xã Nghĩa An"],
"Lục Yên": ["Xã An Phú", "Xã Động Quan", "Xã Khánh Hòa", "Xã Liễu Đô"],
"Mù Cang Chải": ["Xã Chế Cu Nha", "Xã Dế Xu Phình", "Xã La Pán Tẩn", "Xã Mồ Dề"],
"Trạm Tấu": ["Xã Bản Công", "Xã Hát Lừu", "Xã Làng Nhì", "Xã Trạm Tấu"],
"Trấn Yên": ["Xã Báo Đáp", "Xã Cường Thịnh", "Xã Hòa Cuông", "Xã Việt Cường"],
"Văn Chấn": ["Xã Bình Thuận", "Xã Cát Thịnh", "Xã Đại Lịch", "Xã Nậm Lành"],
"Văn Yên": ["Xã An Bình", "Xã Châu Quế Hạ", "Xã Đại Phác", "Xã Mỏ Vàng"]
},
"Phu Yen": {
"Tuy Hòa": ["Phường 1", "Phường 2", "Phường Phú Đông", "Xã Bình Kiến"],
"Sông Cầu": ["Phường Xuân Đài", "Xã Xuân Lộc", "Xã Xuân Hải", "Xã Xuân Phương"],
"Đông Hòa": ["Xã Hòa Hiệp Bắc", "Xã Hòa Hiệp Trung", "Xã Hòa Xuân Nam", "Xã Hòa Tâm"],
"Đồng Xuân": ["Xã Đa Lộc", "Xã Phú Mỡ", "Xã Xuân Lãnh", "Xã Xuân Quang 1"],
"Phú Hòa": ["Xã Hòa An", "Xã Hòa Định Đông", "Xã Hòa Định Tây", "Xã Hòa Trị"],
"Sơn Hòa": ["Xã Sơn Định", "Xã Sơn Long", "Xã Sơn Nguyên", "Xã Sơn Xuân"],
"Sông Hinh": ["Xã Ea Bá", "Xã Ea Lâm", "Xã Ea Ly", "Xã Ea Trol"],
"Tây Hòa": ["Xã Hòa Bình 1", "Xã Hòa Đồng", "Xã Hòa Phong", "Xã Hòa Tân Tây"]
}

    // Thêm các tỉnh/thành khác với các quận/huyện và phường/xã tương ứng
};

function updateDistricts() {
    const citySelect = document.getElementById("city");
    const districtSelect = document.getElementById("district");
    const wardSelect = document.getElementById("ward");
    const selectedCity = citySelect.value;

    // Xóa các tùy chọn cũ của quận/huyện và phường/xã
    districtSelect.innerHTML = '<option value="">Chọn Quận/Huyện</option>';
    wardSelect.innerHTML = '<option value="">Chọn Phường/Xã</option>';

    // Kiểm tra và thêm các tùy chọn quận/huyện tương ứng
    if (selectedCity && data[selectedCity]) {
        Object.keys(data[selectedCity]).forEach(district => {
            const option = document.createElement("option");
            option.value = district;
            option.textContent = district;
            districtSelect.appendChild(option);
        });
    }
}

function updateWards() {
    const citySelect = document.getElementById("city");
    const districtSelect = document.getElementById("district");
    const wardSelect = document.getElementById("ward");
    const selectedCity = citySelect.value;
    const selectedDistrict = districtSelect.value;

    // Xóa các tùy chọn phường/xã cũ
    wardSelect.innerHTML = '<option value="">Chọn Phường/Xã</option>';

    // Kiểm tra và thêm các tùy chọn phường/xã tương ứng
    if (selectedCity && selectedDistrict && data[selectedCity][selectedDistrict]) {
        data[selectedCity][selectedDistrict].forEach(ward => {
            const option = document.createElement("option");
            option.value = ward;
            option.textContent = ward;
            wardSelect.appendChild(option);
        });
    }
}