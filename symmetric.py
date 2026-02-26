# Find symmetric difference between two sets without built-in methods
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set()

for i in set1:
    if i not in set2:
        result.add(i)

for i in set2:
    if i not in set1:
        result.add(i)

print(result)
