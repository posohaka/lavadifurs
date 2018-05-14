import numpy as nm
import math
import matplotlib.pyplot as plt

def fotx(x):
    return pow(x * math.log(x - 1), 2) * math.exp(x)

def fh2(x):
    l = (math.exp(x) * pow(x,2) + 4 * math.exp(x) * x + 2 * math.exp(x)) *pow(math.log(x - 1), 2) + \
        math.exp(x) * pow(x, 2) * pow(x - 1, -2) * (2 - 2 * math.log(x - 1)) + \
        (4 * (math.exp(x) * pow(x, 2) + 2 * math.exp(x) * x) * math.log(x)) / (x - 1)
    return l

def plotfh2():
    fig = plt.figure()
    x = nm.arange(3, 4 + 0.0001, 0.0001)
    y = [fh2(i) for i in x]
    plt.plot(x, y)
    plt.title("График 2 производной")
    plt.grid(True)


def integralltrap(a, b):
    #h = 0.001
    #eps = fh2(b) * (b - a) / 12
    #while (eps * pow(h, 2) > pow(10.0, -5)):
    #    h /= 10
    h = math.sqrt(12 * pow(10, -5) / (fh2(b) * (b - a)))
    s = (fotx(a) + fotx(b)) / 2
    n = nm.round((b - a) / h)
    for i in nm.arange(a + h, b, h):
        s += fotx(i)

    s *= h
    print("Метод трапеции")
    print("Отрекзок [{0}, {1}]".format(a, b), "С шагом h = {0}".format(h))
    print("Колличество узлов n = {0}".format(n))
    print("Значение интегралла = ", s)
    #print("Оценка погрешности = ", eps*pow(h, 2), "\n")

def integrallsimp(a, b):
    h = (b - a) / 10
    s = fotx(a) + fotx(b)
    s1 = 0
    s2 = 0
    y = [fotx(i) for i in nm.arange(a + h, b + h, h)]
    for i in range(5):
        s1 += y[2 * i]
    for i in range(4):
        s2 += y[2 * i + 1]
    s += 4 * s1 + 2 * s2
    s *= h / 3
    print("Метод Симпсона")
    print("Отрекзок [{0}, {1}]".format(a, b), "С шагом h = {0}".format(h))
    print("Колличество узлов n = {0}".format(10))
    print("Значение интегралла = ", s, "\n")
    #print("Оценка погрешности = ", eps * pow(h, 2))

def plotfunct():
    x = nm.arange(3,4, 0.0001)
    y = [fotx(i) for i in x]
    fig = plt.figure()
    plt.plot(x, y, 'b')
    plt.fill_between(x, y)
    plt.title("Интеграл функции")
    plt.grid(True)
    #plt.show()

def funcxy(x, y):
    return pow(x * y - 0.5, 2)

#y(1)= 0 h = 0.1

def rongekute_3(x0, y0):
    h = 0.1
    y = []
    x = []
    y.append(y0)
    x.append(x0)
    yn = y0
    xn = x0
    for i in range(3):
        f0 = h * funcxy(xn, yn)
        f1 = h * funcxy(xn + h / 2, yn + f0 / 2)
        f2 = h * funcxy(xn + h, yn - f0 + 2 * f1)
        ynext = (f0 + 4 * f1 + f2) / 6 + yn
        y.append(ynext)
        yn = ynext
        xn += h
        x.append(xn)
    #plotdifur(x, y, "Метод Рунге-Кута - 3 порядка")
    return x, y

def rongekute_4(x0, y0):
    h = 0.1
    y = []
    x = []
    y.append(y0)
    x.append(x0)
    yn = y0
    xn = x0
    for i in range(3):
        f0 = h * funcxy(xn, yn)
        f1 = h * funcxy(xn + h / 2, yn + f0 / 2)
        f2 = h * funcxy(xn + h / 2, yn + f1 / 2)
        f3 = h * funcxy(xn + h, yn + f2)
        ynext = (f0 + 2 * f1 + 2 * f2 + f3) / 6 + yn
        y.append(ynext)
        yn = ynext
        xn += h
        x.append(xn)
    #plotdifur(x, y, "Метод Рунге-Кута - 4 порядка")
    return x, y

def plotdifur(x, y, x1, y1, x2, y2):
    fig = plt.figure()
    legend1, legend2, legend3 = plt.plot(x, y, x1, y1, x2, y2)
    plt.legend((legend1, legend2, legend3), ("Метод Рунге-Кута - 3 порядка","Метод Рунге-Кута - 4 порядка", "Метод прогноза и коррекции" ))
    plt.grid(True)
    #plt.show()

def prognozkorr():
    h = 0.1
    xn = 1
    yn = 0
    x = []
    y = []
    y.append(yn)
    x.append(xn)
    for i in range(3):
        """"
        ykp1 = yn + funcxy(xn, yn) * h
        while (True):
            fk = funcxy(xn + h, ykp1)
            ykp1ip = yn + (funcxy(xn, yn) + fk) * h / 2
            if (abs(ykp1 - ykp1ip) <= pow(10, -6)):
                y.append(ykp1ip)
                yn = ykp1ip
                xn += h
                x.append(xn)
                break
            ykp1 = ykp1ip
            """
        yh2 = yn + h ** 2 * funcxy(xn, yn)
        yn = yn + h * funcxy(xn, yn) + 1 / 2 * (funcxy(xn + h ** 2, yh2) - funcxy(xn, yn))
        xn = xn + h
        x.append(xn)
        y.append(yn)
    #plotdifur(x, y, "Метод прогноза и коррекции")
    return x, y


plotfh2()
plotfunct()
integralltrap(3, 4)
integrallsimp(3, 4)



r3 = rongekute_3(1, 0)
print("Метод Рунге-Кута - 3 порядка   n = 3")
print("Количесвто узлов n = 3")
print("Шаг h = 0.1")
for i in range(len(r3[1])):
    print("x{0} = {1}, y{0} = {2}".format(i, nm.round(r3[0][i], 5), nm.round(r3[1][i], 5)))
r4 = rongekute_4(1, 0)
print()
print("Метод Рунге-Кута - 4 порядка   n = 3")
print("Количесвто узлов n = 3")
print("Шаг h = 0.1")
for i in range(len(r4[1])):
    print("x{0} = {1}, y{0} = {2}".format(i, nm.round(r4[0][i], 5), nm.round(r4[1][i], 5)))
print()
p = prognozkorr()
print("Метод прогноза и коррекции   n = 3")
print("Количесвто узлов n = 3")
print("Шаг h = 0.1")
for i in range(len(p[1])):
    print("x{0} = {1}, y{0} = {2}".format(i, nm.round(p[0][i], 5), nm.round(p[1][i], 5)))
plotdifur(r3[0], r3[1], r4[0], r4[1], p[0], p[1])


plt.show()
