#prints a diamond first by printing spaces and then * accordingly
i=5
for j in range(i):
    print(" "*(i-j), "*"*(2*j+1))
print()


for k in range(i, 0,-1):
    print(" "*(i-k+1), "*"*(2*k-1))
print()
