def find_common_participants(first_group, second_group, sep=','):
    first_group = set(first_group.split(sep))
    second_group = set(second_group.split(sep))
    return sorted(first_group.intersection(second_group))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
