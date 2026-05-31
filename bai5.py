# ================== DATA ==================
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]


# ================== HELPER ==================

def normalize_product_id(product_id):
    return product_id.strip().upper()


def find_product(product_id):
    for product in product_list:
        if product["product_id"] == product_id:
            return product
    return None


def get_valid_int(prompt):
    value = input(prompt)
    if not value.isdigit():
        return None
    return int(value)


def get_stock_status(quantity):
    if quantity == 0:
        return "Hết hàng"
    elif quantity <= 5:
        return "Sắp hết hàng"
    return "Còn hàng"


# ================== FUNCTIONS ==================

def display_products():
    if not product_list:
        print("Danh sách sản phẩm hiện đang trống.")
        return

    print("\nDanh sách sản phẩm hiện tại:")
    for i, p in enumerate(product_list, 1):
        status = get_stock_status(p["quantity"])
        print(f"{i}. Mã SP: {p['product_id']} | Tên: {p['product_name']} | "
              f"Giá: {p['price']} | Tồn kho: {p['quantity']} | "
              f"Đã bán: {p['sold']} | Đổi trả: {p['returned']} | "
              f"Giảm giá: {p['discount']}% | Trạng thái: {status}")


def sell_product():
    product_id = normalize_product_id(input("Nhập mã sản phẩm khách muốn mua: "))
    product = find_product(product_id)

    if not product:
        print("Không tìm thấy sản phẩm cần bán")
        return

    quantity = get_valid_int("Nhập số lượng khách mua: ")
    if quantity is None or quantity <= 0:
        print("Số lượng mua không hợp lệ")
        return

    if quantity > product["quantity"]:
        print("Số lượng trong kho không đủ để bán")
        return

    # tính giá sau giảm
    final_price = product["price"] * (100 - product["discount"]) / 100
    total = final_price * quantity

    # cập nhật
    product["quantity"] -= quantity
    product["sold"] += quantity

    print(f"Tổng tiền khách cần thanh toán: {int(total)}")


def return_product():
    product_id = normalize_product_id(input("Nhập mã sản phẩm khách muốn đổi/trả: "))
    product = find_product(product_id)

    if not product:
        print("Không tìm thấy sản phẩm cần đổi trả")
        return

    quantity = get_valid_int("Nhập số lượng đổi/trả: ")
    if quantity is None or quantity <= 0:
        print("Số lượng đổi/trả không hợp lệ")
        return

    if quantity > product["sold"]:
        print("Số lượng đổi/trả không được vượt quá số lượng đã bán")
        return

    # tính tiền hoàn
    final_price = product["price"] * (100 - product["discount"]) / 100
    refund = final_price * quantity

    # cập nhật
    product["sold"] -= quantity
    product["quantity"] += quantity
    product["returned"] += quantity

    print(f"Số tiền hoàn lại cho khách: {int(refund)}")


def apply_discount():
    product_id = normalize_product_id(input("Nhập mã sản phẩm cần giảm giá: "))
    product = find_product(product_id)

    if not product:
        print("Không tìm thấy sản phẩm")
        return

    discount = get_valid_int("Nhập phần trăm giảm giá: ")
    if discount is None or discount < 0 or discount > 70:
        print("Phần trăm giảm giá không hợp lệ")
        return

    product["discount"] = discount
    print("Cập nhật giảm giá thành công")


def restock_product():
    product_id = normalize_product_id(input("Nhập mã sản phẩm cần nhập thêm: "))
    product = find_product(product_id)

    if not product:
        print("Không tìm thấy sản phẩm cần nhập kho")
        return

    quantity = get_valid_int("Nhập số lượng nhập thêm: ")
    if quantity is None or quantity <= 0:
        print("Số lượng nhập kho không hợp lệ")
        return

    product["quantity"] += quantity
    print("Nhập kho thành công")


# ================== MAIN ==================

def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Bán sản phẩm cho khách hàng")
        print("3. Xử lý đổi trả sản phẩm")
        print("4. Áp dụng giảm giá cho sản phẩm")
        print("5. Nhập thêm hàng vào kho cửa hàng")
        print("6. Thoát chương trình")

        choice = input("Chọn chức năng (1-6): ")

        if not choice.isdigit() or int(choice) not in range(1, 7):
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
            continue

        choice = int(choice)

        if choice == 1:
            display_products()
        elif choice == 2:
            sell_product()
        elif choice == 3:
            return_product()
        elif choice == 4:
            apply_discount()
        elif choice == 5:
            restock_product()
        elif choice == 6:
            print("Thoát chương trình.")
            break


# chạy chương trình
if __name__ == "__main__":
    main()