users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dictionary = {"Общее количество": 0,"Уникальные посещения":0}
count = len(users)
unique_count = len(set(users))
dictionary["Общее количество"] = count
dictionary["Уникальные посещения"] = unique_count
print(dictionary)
