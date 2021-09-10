def count():
    dict_1 = {}
    with open('3.txt', encoding='utf-8') as file_3:
        count_3 = len(file_3.readlines())
    dict_1["3.txt"] = count_3
    with open('2.txt', encoding='utf-8') as file_2:
        count_2 = len(file_2.readlines())
    dict_1["2.txt"] = count_2
    with open('1.txt', encoding='utf-8') as file_1:
        count_1 = len(file_1.readlines())
    dict_1['1.txt'] = count_1

    sorted_dict = sorted(dict_1.items(), key=lambda x: x[1])
    new_dict = dict(sorted_dict)

    dict_2 = {}
    with open('2.txt', 'r', encoding='utf-8') as first_file:
        a = first_file.read()
        dict_2[a] = list(new_dict.items())[0]
    with open('1.txt', 'r', encoding='utf-8') as second_file:
        b = second_file.read()
        dict_2[b] = list(new_dict.items())[1]
    with open('3.txt', 'r', encoding='utf-8') as third_file:
        c = third_file.read()
        dict_2[c] = list(new_dict.items())[2]

    with open('itog', 'w', encoding='utf-8') as itog_file:
        for keys,values in dict_2.items():
            for values_2 in values:

                itog_file.write(f'{values_2}\n{keys} \n')

print(count())



