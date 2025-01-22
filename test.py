labels = ["Яблоко", "Яблоко", "Персик", "Апельсин", "Кокос"]

print(list(sorted(set(filter(bool, map(str.strip, labels))))))