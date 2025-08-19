# Control-Mouse-by-Camera-with-Finger
Khiển chuột bằng camera


# Điều Khiển Chuột Bằng Cử Chỉ Tay
#### Vì lí do project này nhỏ và trên python tải từ python.org thì thư viện python không hoạt động với nhau nếu không cài đúng bản nên mình chọn IDE Thonny 
## Cài Đặt
### Vào thonny , vào Tools, vào Open System Shell, cd "Address", rồi nhập :
```bash
pip install opencv-python mediapipe pyautogui
```

## Chạy Chương Trình

```bash
main.py
```

## Cử Chỉ

### Tay Phải
- **Ngón trỏ duỗi**: Di chuyển chuột
- **Dơ cả bàn tay**: Click chuột phải (1 lần)

### Tay Trái  
- **Ngón trỏ duỗi**: Giữ chuột trái (drag)
- **Dơ cả bàn tay**: Click chuột trái (1 lần)


Nhấn **ESC** để thoát.

## Tính Năng

- **Click thông minh**: Mỗi cử chỉ chỉ click 1 lần, không spam
- **Reset độc lập**: Mỗi tay có trạng thái riêng, không ảnh hưởng lẫn nhau
- **Di chuột mượt**: Theo dõi chính xác vị trí ngón trỏ

- Đảm bảo ánh sáng đủ cho camera
- Giữ tay trong khung hình camera
- Nắm tay để reset trạng thái click
