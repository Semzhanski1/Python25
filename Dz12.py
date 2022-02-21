imya = "Антон"
print(imya)

vozrst = 18
print("Мой возраст -", vozrst)

x = "Антон"
# y = x + x + x + x + x
y = x * 5
print(y)

print("Сколько вам лет?")
age_str = input()
print("Как вас зовут?")
name_str = input()
print("Здравствуйте",name_str,age_str, "лет" )




print("Сколько вам лет?")
age_str = input()
if age_str in range(60,100):
    print("Старость не радость")
else:
    print("Молодость не веселье")


imyapolz = imya
print(imyapolz[2:6])


imyapolz2 = imya[::-1]
print(imyapolz2)

imyapolz3 = imya
print(imyapolz3[-7:5])

imyapolz4 = imya
print(imyapolz4[-3:])


imyapolz5 = imya
print(imyapolz5[0:5])




print("Введите имя")
imya = input()
x = len(imya)
print("Длинна вашего имени",x)
num = int(input("Введите возраст: "))
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("Сумма цифр возраста равна: ", sum)
num = int(input("Введите возраст повторно "))
mult = 1
while (num != 0):
    mult = mult * (num % 10)
    num = num // 10
print("Произведение цифр возраста равно: ", mult)




print("Введите имя")
imyastr = input()
if not int(imyastr.rfind(" ")) == -1:
    print("ЕГГОГ! Не используйте пробелы!")
print("Введите возраст")
vozrststr = int(input())
if vozrststr < 0 or vozrststr > 150:
    print("ЕГГОГ! Такого не бывает!")


anser = input("Сколько будет 2+2*2?")
if anser == "6":
    otvet = "Вы ответили верно!"
else:
    otvet = "Вы ответили неверно!"
print(otvet)
