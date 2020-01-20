in_file = "logs.txt"
success_counter = 0

success_mas = []
success_mas_ips = []
cart_mas = []

time_of_the_day = [0, 0, 0, 0]

counter_cart = 0
counter_cart_sorted = 0

with open(in_file, 'r') as read_file:
  for line in read_file:
    line_mas = line.split(' ')
    if "success_pay" in line_mas[12]:
      success_mas.append(line_mas)
      success_mas_ips.append(line_mas[11])
      success_counter += 1
    if "cart_id" in line_mas[12]:
      cart_mas.append(line_mas[12][:-1])
      counter_cart += 1
    if int(line_mas[8][:2]) in range(6):
      time_of_the_day[0] += 1
    if int(line_mas[8][:2]) in range(6, 12):
      time_of_the_day[1] += 1
    if int(line_mas[8][:2]) in range(12, 18):
      time_of_the_day[2] += 1
    if int(line_mas[8][:2]) in range(18, 25):
      time_of_the_day[3] += 1
    
unique_mas_id = []
unique_cart_counter = 0

for string_with_id in cart_mas:
  just_id = string_with_id[-4:]
  if unique_mas_id.count(just_id) == 0:
    unique_mas_id.append(just_id)
    unique_cart_counter += 1

number_of_rebuys = 0
for string_with_ip in success_mas_ips:
  ip = string_with_ip
  number_of_rebuys += (success_mas_ips.count(string_with_ip) - 1)

print("Number of rebuys? ", number_of_rebuys)
print("How many carts left? ", unique_cart_counter - success_counter)

decide_var = 3
for i in range(3):
  if time_of_the_day[i] > time_of_the_day[decide_var]:
    decide_var = i

if decide_var == 0:
  print('Time of day - Night')
if decide_var == 1:
    print('Time of day - Morning')
if decide_var == 2:
    print('Time of day - Day')
if decide_var == 3:
  print('Time of day - Evening')
