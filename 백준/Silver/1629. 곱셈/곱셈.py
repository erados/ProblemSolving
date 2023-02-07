A, B, C = map(int, input().split())
bin_B = bin(B)[2:]
memory = [A]
for _ in range(len(bin_B) - 1):
    A = (A * A) % C
    memory.append(A)

for index, value in enumerate(bin_B[1:][::-1]):
    if value == "1":
        A = (A * memory[index]) % C

print(A % C)
