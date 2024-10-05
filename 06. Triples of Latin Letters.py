num_triples = int(input())

for i in range(0, num_triples):
    for j in range(0, num_triples):
        for l in range(0, num_triples):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + l)}")
