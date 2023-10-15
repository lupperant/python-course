numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
count = len(numbers)
average_of_numbers = sum(i for i in numbers if i is not None)/count
index_of_None = numbers.index(None)
numbers[index_of_None] = average_of_numbers
print("Измененный список:", numbers)
