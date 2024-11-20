# https://progolymp.se/2024/skolkval/uppgifter24.pdf
n = int(input("N ? "))
ans = 0
a = 1
while a*(a+1)*(a+2) < n:
    ans += 1
    a += 1
print(ans)