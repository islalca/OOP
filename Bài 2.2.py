# 1
import math

r = 5
volume = (4/3) * math.pi * r**3

print("Volume of sphere:", volume)

# 2
price = 24.95
discount = 0.40
shipping_first = 3
shipping_extra = 0.75
copies = 60

book_price = price * (1 - discount)

shipping_cost = shipping_first + (copies - 1) * shipping_extra

total_cost = copies * book_price + shipping_cost

print("Total wholesale cost:", total_cost)

# 3
start_hour = 6
start_min = 52

easy_pace = 8 * 60 + 15
tempo_pace = 7 * 60 + 12

total_seconds = easy_pace + 3 * tempo_pace + easy_pace

total_minutes = total_seconds // 60
extra_seconds = total_seconds % 60

end_min = start_min + total_minutes
end_hour = start_hour + end_min // 60
end_min = end_min % 60

print("Breakfast time:", end_hour, ":", end_min, ":", extra_seconds)