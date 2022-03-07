import random

def random_num(x,y):
  num = random.randint(x,y)
  return num



k = random_num(0,20)

def random_num_prime(m):
  if m > 1:
    for i in range(2, m):
        if (m % i) == 0:
            return f"{m} is not prime"
            break
    else:
      return m

print(random_num_prime(k))
