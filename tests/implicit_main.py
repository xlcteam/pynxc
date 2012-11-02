
x = 42
NumOut(0, LCD_LINE1, x)

for x in range(10):
    NumOut(0, LCD_LINE1, x)

while True:
    Wait(10)

if True == False:
    TextOut(0, LCD_LINE1, "there is something wrong")

OnFwd(OUT_AB, 100)
Wait(1000)

