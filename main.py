from random import randint
ran= randint(1, 1000)
print("Отгадайте число от 1 до 1000")
while (True):
    inp = int(input("Введите число от 1 до 1000__"))
    if inp <ran :
      print("Ваше число меньше загаданного")
    elif inp>ran:
        print("Ваше число больше загаданного")
    else:
        print("Вы угадали число", ran)
        break
    
