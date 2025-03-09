from random import randint

a = [12, 20, 11, 10, 14, 16, 15, 10]
N = len(a)  # количество элементов в списке
print(a)  # вывод исходного неотсортированного списка

# Сама сортировка методом "пузырька"
for i in range(2):
    for j in range(N-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)