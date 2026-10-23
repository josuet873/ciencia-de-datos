notas = [85, 90, 60, 70]

print(len(notas))
print(sum(notas))
print(min(notas),max(notas))
print(sum(notas)/(len(notas)))

print(70 in notas)
print(100 in notas)

notas.remove(60)
print(notas)

notas.sort()
print(notas)
