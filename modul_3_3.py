def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()              #вызываем функцию без аргументов
print_params(b=25)          #вызываем функцию b=25
print_params(c=[1, 2, 3])   #вызываем функцию c=[1,2,3]

values_list = [675,True,"marik"]              #создаем список
values_dict = {"a":397, "b":3.14, "c":"farm"} #создаем словарь
print_params(*values_list)                    #вызываем функцию распакованый список
print_params(**values_dict)                   #вызываем функцию распакованый словарь

values_list_2 = [54.32, "string"]             #создаем список с двумя элементами разных типов
print_params(*values_list_2, 42)           #вызываем список