from utils import factorial
from utils import nsd_finder
if __name__ == "__main__":
    n = input("Введіть число: ")
    print(f"Факторіал {n} = {factorial(n)}\n")
if __name__ == "__main__":
    a, b = [int(el) for el in input().split()]
    print(f"НСД({a},{b}) = {nsd_finder(a, b)}")


from utils import is_power_of_5
if __name__ == "__main__":
	n = int(input("Введіть число для перевірки:"))
	print(f"{n} {"не "*(not(is_power_of_5(n)))}є степенем п'ятірки")
