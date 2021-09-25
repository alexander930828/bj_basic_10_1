#1

def factorial(n):
    result = 1
    if n > 0:
        result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))


#2

def pibo(n):                      # 재귀 함수
    if n < 2: return n            # 2보다 작을 때 그대로 반환
    return pibo(n-1) + pibo(n-2)  # n-1번째 수와 n-2번째 수를 더해 반환
print(pibo(int(input())))