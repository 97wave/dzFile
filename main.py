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
                temp_dict['ingredient_name'] = ingridient[0]
                temp_dict['quantity'] = ingridient[1]
                temp_dict['measure'] = ingridient[2]
                list_of_ingridient += [temp_dict]
            cook_book[dish_name] = list_of_ingridient         
            line = f.readline()
    return cook_book

pprint(read('book.txt'))