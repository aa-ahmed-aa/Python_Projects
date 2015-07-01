stack = {
    'Google' : 501.152,
    'Yahoo' : 250.12,
    'FaceBook' : 750.21,
    'Amazone' : 285.12,
    'Apple' : 14.15
}

print(min(zip(stack.values(),stack.keys())))
print(max(zip(stack.values(),stack.keys())))
print(sorted(zip(stack.values(),stack.keys())))