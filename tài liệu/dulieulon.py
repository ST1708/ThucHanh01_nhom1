# script_tao_file_lon.py

# Kích thước mong muốn: Ví dụ 400MB
# 1 ký tự (char) = 1 byte (xấp xỉ). Cần 400 triệu ký tự.
KICH_THUOC_MONG_MUON = 400 * 1024 * 1024 
CHUOI_DATA = 'x' * KICH_THUOC_MONG_MUON # Chuỗi 400 triệu ký tự 'x'

noi_dung_file = f"""
# Đây là một file Python chứa dữ liệu lớn
DATA = \"\"\"{CHUOI_DATA}\"\"\"

# Thêm một lệnh đơn giản để kiểm tra
print("Dữ liệu đã được nạp (nếu thành công)")
print(f"Kích thước DATA: {{len(DATA) / 1024 / 1024:.2f}} MB")
"""

with open('large_python_data.py', 'w', encoding='utf-8') as f:
    f.write(noi_dung_file)

print("Đã tạo file large_python_data.py thành công.")
