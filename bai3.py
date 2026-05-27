order_list = ["GE001", "GE002", "GE003"]

while True : 
    choice = input('''
===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Thêm đơn hàng mới
3. Xóa đơn hàng theo mã
4. Thoát chương trình
Nhập lựa chọn của bạn : ''')
    
    if not choice.isdigit() :
        print('[Lỗi] Lựa chọn không hợp lệ ! Vui lòng nhập số từ 1 - 4 !')
        continue

    choice = int(choice)

    if choice == 4 :
        print('Hệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!')
        break

    elif choice == 1 :
        print('--- DANH SÁCH ĐƠN HÀNG HIỆN TẠI ---')

        if len(order_list) == 0 :
            print('Danh sách đơn hàng hiện đang trống.')
        else :
            for i in range(len(order_list)):
                print(f'{i + 1} . {order_list[i]}')
    
    elif choice == 2 : 
        new_order = input('Nhập mã đơn hàng mới : ').strip().upper()

        order_list.append(new_order)

        print(f'Danh sách đơn hàng hiện tại : {order_list}')

    elif choice == 3 :
        delete_order = input('Nhập tên đơn hàng cần xóa : ').strip().upper()

        if not delete_order in order_list:
            print('Không tìm thấy mã đơn hàng cần xóa!')
        else :
            order_deleted = order_list.remove(delete_order)
            print(f'Danh sách hiện tại : {order_list}')
    
    