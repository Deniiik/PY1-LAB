def find_common_participants(first_group, second_group, comma=','):
    group_one = first_group.split(comma)
    group_two = second_group.split(comma)
    common_participants = list(set(group_one).intersection(group_two))
    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("Общие участники:", find_common_participants(participants_first_group, participants_second_group, "|"))
