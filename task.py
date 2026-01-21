# Masalalar: clck.ru/3RP2fm
# 1-masala
# Supermarket savatchasi uchun asosiy sinf
class CartItem:
    def __init__(self, name, price, quantity, discount):
        # Mahsulot nomi
        self.name = name
        # Mahsulot narxi
        self.price = price
        # Mahsulot miqdori
        self.quantity = quantity
        # Chegirma foizi
        self.discount = discount

    def total_cost(self):
        # Chegirma qo'llangan umumiy narxni hisoblash
        return self.price * self.quantity * (1 - self.discount / 100)


# Oziq-ovqat mahsulotlari uchun sinf
class FoodItem(CartItem):
    def total_cost(self):
        # Asosiy sinfdagi hisoblash metodidan foydalanish
        cost = super().total_cost()
        # Formatlangan natijani qaytarish
        return f"Oziq-ovqat mahsuloti: {self.name} -> {cost:.2f}$"


# Oziq-ovqat bo'lmagan mahsulotlar uchun sinf
class NonFoodItem(CartItem):
    def total_cost(self):
        # Asosiy sinfdagi hisoblash metodidan foydalanish
        cost = super().total_cost()
        # Formatlangan natijani qaytarish
        return f"Nooziq-ovqat mahsuloti: {self.name} -> {cost:.2f}$"


# Savatchadagi mahsulotlar ro'yxati
items = [
    FoodItem("Olma", 1.5, 3, 10),
    FoodItem("Non", 2.0, 2, 5)
]

# Barcha mahsulotlar bo'yicha umumiy summani hisoblash
total_sum = 0

# Har bir mahsulotning narxini chiqarish
for item in items:
    print(item.total_cost())
    total_sum += item.price * item.quantity * (1 - item.discount / 100)

# Umumiy savatcha narxini chiqarish
print("Umumiy summa:", round(total_sum, 2), "$")