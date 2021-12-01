sum = 0
with open ('chicken.txt', 'r', encoding='UTF-8') as s:
    for line in s:
        str_s = line
        list_s = line.split("일: ")
        sum += int(list_s[1])
        day = int(list_s[0])
average = sum / day
print(average)