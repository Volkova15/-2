result = []
def divider(a, b):
try:
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
      raise TypeError("Ключ або значення не є числом")
    if a < b:
     raise ValueError("а меньше за b")
    if b > 100:
     raise IndexError("b дільше за 100")
 return a/b
except Exception as e:
print(f"Помилка:{e}")
return None
data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 15, 8 : 4}
for key,value in data.items():
 try:
    res = divider(key, value)
 if res is not None:
   results.append(res)
except Exception as e:
print(f"Помилка при обробці {key}: {e}")

print(result)