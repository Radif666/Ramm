n = int(input())
lenght = 0
while n > 0:
    n //= 10
    lenght += 1
    print(lenght)