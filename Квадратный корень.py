print("Корень квадратный-реализация!")
print("Введите число из которого слдует извлечь квадратный корень:")


a=float(input())
if a<1:
 b=a+1
 c=b*b
 while c<a:
  b=b-1
  c=b*b
 else:
  print("Крень равен:", b)
if a>=0:
 if a==1:
  print("Крень равен:", 1)
 elif a==0:
  print("Крень равен:", 0)   
 else: 
  b=a-1
  c=b*b
  while c>a:
   b=b-1
   c=b*b
  else:
   print("Крень равен:", b)
else:
 print("Ваше значение меньше 0, расчет не возможен!")
