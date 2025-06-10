set1={1,22,33,44,55,55,66,77,88}

frozenSet=frozenset(set1)

print("Originalset",set1)

set1.add(221)

print("Modified Set",set1)

print("Frozen Set",frozenSet)

try:
    frozenSet.add(21)

except AttributeError as e:
    print("Error:", e)


