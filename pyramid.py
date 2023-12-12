#prints a pyramid first by printing spaces and then * accordingly
i=5
for j in range(i):
    print(" "*(i-j), "*"*(2*j+1))
print()
