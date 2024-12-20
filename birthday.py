import turtle
import math

def carazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2*n) - 2 * math.cos(3*n) - math.cos(4*n)
    return x, y

def tulis_teks(teks, y):
    t.goto(0, y)
    t.write(teks, align="center", font=("Arial", 4, "bold"))

t = turtle.Turtle()
t.speed(0)
t.color("white")
turtle.bgcolor("black")

# Gambar hati
t.penup()
for i in range(15):
    t.goto(0, 0)
    t.pendown()
    for n in range(0, 100, 2):
        x, y = carazon(n/10)
        t.goto(x*i, y*i)
    t.penup()

# Tulis teks
t.penup()
t.goto(0, -450)
tulis_teks("happy birthdayy daviinn, wytb yaa!", -450)
tulis_teks("tiriizz maangg uda ga 14 lagii, mantaapp. jangaan boseen-bosen yaa sama lalaa", -470)
tulis_teks("tapi kalo emang bosen, yauda la mau gimana lagi..", -490)
tulis_teks("MAAFF YAA GABISAA NGASII APAA APAA, nantii kapaan kapaan lala kasii daa", -510)
tulis_teks("tapi ngasi apa ya, bingung demi da, nantii pas sma kitaa gimana yaa", -530)
tulis_teks("apakah masi berkomunikasii?:(", -550)
tulis_teks("tapi bunga mawar bunga melati, hanya kamu yang adaa dihatiii ♡", -570)
tulis_teks("i love youu daviin sayaangg", -590)

turtle.done()

