import os
import json

def normalize_industries(industries):
    industry_list = industries.split(', ')

    industry_mapping = {
        "Tư vấn": "Consulting",
        "Dịch vụ khách hàng": "Customer services",
        "Bán hàng / Kinh doanh": "Retail and wholesale",
        "Dược / Sinh học": "Pharmaceutical",
        "Kế toán / Kiểm toán": "Finance and economic",
        "Quảng cáo / Khuyến mãi / Đối ngoại": "Advertising and marketing",
        "Ngân hàng / Chứng khoán": "Finance and economic",
        "Thư ký / Hành chánh": "Administrative",
        "Kỹ thuật ứng dụng / Cơ khí": "Manufacturing",
        "Chăm sóc sức khỏe / Y tế": "Health care",
        "Nhà hàng / Dịch vụ ăn uống": "Food and beverage",
        "Giáo dục / Đào tạo / Thư viện": "Education",
        "CNTT - Phần mềm": "Computer and technology",
        "Xây dựng": "Construction",
        "Sản xuất / Vận hành sản xuất": "Manufacturing",
        "Nghệ thuật / Thiết kế / Giải trí": "Art",
        "Nông nghiệp / Lâm nghiệp": "Agriculture",
        "Điện / Điện tử": "Manufacturing",
        "Biên phiên dịch / Thông dịch viên": "Customer services",
        "Xuất nhập khẩu / Ngoại thương": "Foreign trade",
        "Quản lý điều hành": "Administrative",
        "Lao động phổ thông": "Customer services",
        "Vận chuyển / Giao thông / Kho bãi": "Transportation",
        "Nhân sự": "Human resources",
        "Hóa chất / Sinh hóa / Thực phẩm": "Pharmaceutical",
        "Dệt may / Da giày": "Fashion",
        "Khách sạn": "Hospitality",
        "Pháp lý / Luật": "Customer services",
        "Du lịch": "Travel and tourism",
        "Bảo trì / Sửa chữa": "Customer services",
        "Viễn Thông": "Telecommunication",
        "CNTT - Phần cứng / Mạng": "Computer and technology",
        "Bất động sản": "Real estate",
        "An Ninh / Bảo Vệ": "Customer services",
        "Bán lẻ / Bán sỉ": "Retail and wholesale",
        "Bảo hiểm": "Insurance",
        "Tài chính / Đầu tư": "Finance and economic",
        "Tiếp thị": "Consulting",
        "Kiến trúc": "Construction",
        "Nội thất / Ngoại thất": "Manufacturing",
        "Đồ Gỗ": "Manufacturing",
        "Thuỷ Hải Sản": "Agriculture",
        "Ô tô": "Manufacturing",
        "Dầu khí / Khoáng sản": "Energy",
        "Thời trang": "Fashion",
        "Điện lạnh / Nhiệt lạnh": "Manufacturing",
        "Hàng gia dụng": "Manufacturing"
    }

    return industry_mapping.get(industry_list[0], "Other")

