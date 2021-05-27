from math import pi
from datetime import time, timedelta

# 1
r = 5
print(4 / 3 * pi * pow(r, 3))  # 523.5987755982989

# 2
book_cover = 24.95
discount = 0.4
shipping_first_copy = 3
shipping_additional_copy = 0.75
number_of_copies = 60

discounted_book_price = book_cover * discount
total_price = discounted_book_price * (shipping_first_copy + (number_of_copies - 1))
print(total_price)  # 618.76

# 3
# if we consider that we will run in circle and will return to starting position when we finish
breakfast_time = timedelta(hours=6, minutes=52) + timedelta(minutes=2 * 8, seconds=2 * 15) + timedelta(minutes=3 * 7, seconds=3 * 12)
print(breakfast_time)  # 7:30:06
