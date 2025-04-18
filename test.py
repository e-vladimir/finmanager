labels: set[str] = {"Макси", "Продукты питания"}

processing_include = ["Макси"]
processing_exclude = []

print(f"{bool(processing_include) and not bool(labels.intersection(processing_include))} = {bool(processing_include)} and {not bool(labels.intersection(processing_include))}")
print(f"{bool(processing_exclude) and     bool(labels.intersection(processing_exclude))} = {bool(processing_exclude)} and {bool(labels.intersection(processing_exclude))}")
print(f"")

flag_skip: bool = True
flag_skip &= bool(processing_include) and not bool(labels.intersection(processing_include))
flag_skip |= bool(processing_exclude) and     bool(labels.intersection(processing_exclude))

print(flag_skip)
