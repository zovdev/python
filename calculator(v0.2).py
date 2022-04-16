#calculator v0.2
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.CYAN)
what = input("Выберите вариант(+,-):")
print(Fore.GREEN)
a = float(input("Введи первое число: "))
print(Style.DIM)
b = float(input("Введи второе число: "))
if what =="+":
	c = a+b
	print(Fore.BLUE)
	print("Ответ:"+str(c))

elif what =="-":
	c = a-b
	print(Fore.BLUE)
	print("Ответ:"+str(c))
else:
	print(Back.RED+Fore.BLUE+ "Такой функции нет!")