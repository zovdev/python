#calculator v0.1
what = input("Выберите вариант(+,-):")
a = float(input("Введи первое число: "))
b = float(input("Введи второе число: "))
if what =="+":
	c = a+b
	print("Ответ:"+str(c))

elif what =="-":
	c = a-b	
	print("Ответ:"+str(c))
else: print("Такой функции нет!")