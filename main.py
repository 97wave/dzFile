from pprint import pprint

def read(file_):
    cook_book = {}
    with open(file_) as f:
        line = ' '
        while line != '':
            dish_name = f.readline().strip()
            cnt = ord(f.readline()[0])
            cnt -= 48
            list_of_ingridient = []
            for i in range(cnt):
                temp_dict = {}
                ingridient = f.readline().strip().split('|')
                temp_dict = {'ingredient_name': ingridient[0], 'quantity': ingridient[1], 'measure': ingridient[2]}
                list_of_ingridient += [temp_dict]
            cook_book[dish_name] = list_of_ingridient         
            line = f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish_name, ingridients in cook_book.items():
        if dish_name in dishes:
            for ingridient in ingridients:
                if ingridient.get('ingredient_name') not in shop_list:
                    shop_list[ingridient.get('ingredient_name')] = {'measure': ingridient.get('measure'), 'quantity': person_count * int(ingridient.get('quantity'))}
                else:
                    shop_list[ingridient.get('ingredient_name')]['quantity'] += int(ingridient.get('quantity'))
    return shop_list       


def unite_files(files, unite_file):
    with open(unite_file, 'w') as ff:
        files_dict = {}
        sort_list = []
        for file in files:
            with open(file) as f:
                str_cnt = len(f.readlines())
            files_dict[str_cnt] = file
            sort_list.append(str_cnt)
        sort_list.sort()
        for file in sort_list:
            ff.write(files_dict.get(file) + '\n')
            ff.write(str(file) + '\n')
            with open(files_dict.get(file)) as f:
                ff.write(f.read() + '\n')
            
        




cook_book = read('book.txt')
pprint(cook_book)
print()

shop_list = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
pprint(shop_list)

unite_files(['1.txt', '2.txt', '3.txt'], 'final_file.txt')