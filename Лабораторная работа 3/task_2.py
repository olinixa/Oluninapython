
def proverka(group):
    for char in group:
        if not char.isalpha():
            camma=char
            return camma
def find_common_participants(first_group, second_group, comma=","):
    comma=proverka(first_group)
    result = set(first_group.split(comma)).intersection(second_group.split(comma))

    result = list(result)
    result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result=find_common_participants(participants_first_group,participants_second_group)

for imy in (result):
    print(result)
