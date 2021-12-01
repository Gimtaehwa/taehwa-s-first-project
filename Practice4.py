with open ('vocabulary.txt', 'r') as v:

    for line in v:

        list_v = line.strip().split(': ')
        
        e = input("{}: ".format(list_v[1]))

        if e == list_v[0]:
            print('맞았습니다!\n')

        else:
            print('아쉽습니다. 정답은 {}입니다.\n'.format(list_v[0]))

   # with open ("vocabulary.txt", "r") as f:    
        #     for line in f:
        #         i += 1
        #         f_list = line.strip().split(': ')

        #         if i == r:
        #             break