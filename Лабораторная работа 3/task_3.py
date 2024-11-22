# TODO Напишите функцию для поиска индекса товара
def f_index(list,find_item):
    index=0
    for i in items_list:
        if(i==find_item):
            return index
        else:
            index+=1
            continue
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = f_index(items_list,find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
