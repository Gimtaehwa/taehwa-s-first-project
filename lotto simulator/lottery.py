from random import randint

def generate_numbers(n):
    random_num = []

    while len(random_num) < n:
        num = randint(1, 45)

        if num not in random_num:
            random_num.append(num)

    return random_num 
    

def draw_winning_numbers():
    winning_num = generate_numbers(7)

    return sorted(winning_num[:6]) + winning_num[6:]


def count_matching_numbers(numbers, winning_numbers):
    overlap_num = 0

    for n in numbers:
            if n in winning_numbers:
                overlap_num += 1
    
    return overlap_num


def check(numbers, winning_numbers):
    
    if count_matching_numbers(numbers, winning_numbers[:6]) == 6:
        return 1,000,000,000
    elif count_matching_numbers(numbers, winning_numbers) == 6:
        return 50000000
    elif count_matching_numbers(numbers, winning_numbers[:6]) == 5:
        return 1000000
    elif count_matching_numbers(numbers, winning_numbers[:6]) == 4:
        return 50000
    elif count_matching_numbers(numbers, winning_numbers[:6]) == 3:
        return 5000
    else:
        return 0
    
numbers = input ('번호 6개 입력 :')
print('당첨번호는 {}입니다.\n 당신의 상금은 {}원 입니다.'.format(draw_winning_numbers(), check(numbers, draw_winning_numbers())))