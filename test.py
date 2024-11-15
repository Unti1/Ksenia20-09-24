grade_book = {
    "Bob": [3,4,5,4,3],
    "Alice": [5,4],
    "Jack": [3,2,4,4,3],
    "Dean": [5,5,5,4],
    }

# print(max(grade_book, key=grade_book.get)) # продвинутый способ

# Стандартный путь решения
best_student = '' # Ученик с лучшим результатом
best_mark = 0 # средняя оценка ученика с лучшим результатом

for student in grade_book:
    total_sum = sum(grade_book[student])
    total_len = len(grade_book[student])
    mean_mark = total_sum/total_len
    print(f"Сейчас проверяется {student} с средней оценкой {mean_mark}",)

    if mean_mark > best_mark:
        best_mark = mean_mark
        best_student = student
        print(f'На текущем этапе у {student} максимальный балл.')


print(f"Лучший средний балл у {best_student}")
