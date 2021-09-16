# https://contest.yandex.ru/contest/28166/problems/

# A. Вычислите сумму всех целых чисел от 16 до 24 включительно.
print(sum([16, 17, 18, 19, 20, 21, 22, 23, 24]))

# B. На вход подаются два целых числа. Найдите и напечатайте их сумму.
a=int(input())
b=int(input())
print(sum([a,b]))

# C. Если у нас есть черно-белое изображение, то каждый пиксель (точка) в нем кодируется градацией яркости:
# числом от 0 (черный цвет) до 255 (самый яркий белый).
# Например, 50 ближе к 0, чем к 255, поэтому это темно-серый цвет; а 250 - чуть потускневший белый.
# Если мы ходим получить негатив изображения, то чем ярче был пиксель, тем темнее он станет на негативе.
# Мы как бы развернем всю шкалу наоборот. Для получения цвета негатива для пикселя из 255 вычитают исходный цвет:
# 255 - 0 = 255: Черный становится белым
# 255 - 255 = 0: Белый становится черным
# 255 - 240 = 15: Почти белый цвет становится очень темным.
# Получается, что мы находим дополнение числа до 255.
# Напишите функцию, которая для цвета позитива выводит цвет негатива.
a=int(input())
print(255-a)

# D. На вход подается 3 целых числа, вычислить их сумму, максимальное и минимальное значения.
# Вывести их именно в таком порядке: sum, max, min.
a=int(input())
b=int(input())
c=int(input())
print(sum([a, b, c]))
print(max([a, b, c]))
print(min([a, b, c]))

# E. На вход подается два целых числа, вычислить расстояние между ними на числовой оси.
a=int(input())
b=int(input())
print(max([a, b]) - min([a,b]))

# F. Известен курс рубля к доллару, например. 1 рубль = 0,014 доллара.
# Известен курс доллара к евро, например, 1 доллар = 0,84 евро.
# Вычислите курс евро к рублю, округлив до 2 знаков после запятой. То есть надо ответить на вопрос: сколько рублей стоит один евро?
r=float(input())
d=float(input())
print(round(1/r/d, 2))

# G. У нас есть бюджет: 1572 рубля. На вход нам подается стоимость некоторого товара.
# Нужно вычислить, сколько единиц этого товара мы можем купить, используя полностью наш бюджет.
# Покупать дробные единицы товара мы не можем.
# Вполне возможно, что мы не сможем купить ни одной единицы товара. То есть ответом будет 0.
a=int(input())
print(1572//a)

# H. Дано трехзначное число. Пользуясь только операциями с числами, вычислите сумму его цифр.
# Например: 145 -> 1 + 4 + 5 = 10
# Задача довольно легко гуглится, но давайте попробуем решить ее без циклов. )
a=int(input())
print(sum([a//100, (a%100)//10, a%10]))

# I. Пользуясь решением предыдущей задачи, «переверните» целое трехзначное число.
# Напомним, что желательно не использовать циклы, строковые операции и т.д: только операции с числами.
a=int(input())
print(sum([a//100, a%100-a%10, a%10*100]))

# J. Очень часто время в информационных системах хранится как количество секунд, которые прошли с 1 января 1970 года
# (посмотрите статью в Википедии про Unix-время). Например, 1624198275.
# В таком виде времена удобно сравнивать, вычислять разницу между любыми значениями в секундах.
# Напишите программу, которая по заданному времени печатает год, когда был сделан соответствующий замер.
# Считать разницу в длинах разных годов несущественной: можно предположить, что во всех годах 365 дней
a=int(input())
print(1970 + int(a/365/24/60/60))

# K. Индекс массы тела (англ. body mass index (BMI), ИМТ)
# — величина, позволяющая оценить степень соответствия массы человека и его роста и тем самым косвенно судить о том,
# является ли масса недостаточной, нормальной или избыточной. Важен при определении показаний для необходимости лечения.
# I = m/h**2
# m — масса тела в килограммах. h — рост в метрах.
# Напишите программу, которая по заданным значениям m и h печатает ИМТ.
m=int(input())
h=int(input())
print(round(m/(h/100)**2, 2))

# L. Давайте повторим функциональность калькулятора краски на сайте OBI, только без количества слоев.
# Округляйте значения, если нужно, только при их печати. Все вычисления производите с полной точностью.
w=float(input())
h=float(input())
r=float(input())
v=int(input())
pz=int(input())
s=w*h
l=s/r*(1+pz/100)
kb=l//v+1
ost=kb*v-l
print(round(s, 2), round(l, 2), int(kb), round(ost, 2), sep='\n')