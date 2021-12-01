with open ('vocabulary.txt', 'w') as v:

    while True:
        e = input('영어 단어를 입력하세요: ')
        if e == 'q':
            break
    
        k = input('한국어 뜻을 입력하세요: ')
        if k == 'q':
            break

        v.write('{}: {}\n'.format(e, k))