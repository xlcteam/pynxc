STATE = 0
FINAL = 0
THRESH = 40
THRESH2 = 40

def task_ruky():
    while (1):
        OnFwd(OUT_C, 65)
        Wait(500)
        Off(OUT_C)

        OnRev(OUT_C,65)
        Wait(500 * 2)
        Off(OUT_C)

        OnFwd(OUT_C,65)
        Wait(500)
        Off(OUT_C)
        if STATE == 5:
            break

def task_pohyb():
    while(1):
        if Sensor(IN_1) < THRESH and Sensor(IN_4) < THRESH2:
            STATE += 1

            Off(OUT_AB)
            Wait(2000)
            OnFwd(OUT_AB,90)
            Wait(200)
            if STATE == 6:
                RotateMotor(OUT_A,60,290)
                x = 0
                for x in range(0, 5):
                    OnFwd(OUT_C, 45)
                    Wait(500)
                    Off(OUT_C)
                    Wait(500)

                    OnRev(OUT_C,45)
                    Wait(500 * 2)
                    Off(OUT_C)
                    Wait(500)

                    OnFwd(OUT_C,45)
                    Wait(500)
                    Off(OUT_C)
                    Wait(500)

                OnFwd(OUT_A,50)
                OnFwd(OUT_B,-50)
                Wait(3000)
                OnFwd(OUT_A,70)
                OnFwd(OUT_B,-50)
                Wait(10000)
                StopAllTasks()

        elif(Sensor(IN_1) < THRESH):
            OnFwd(OUT_A, -50)
            OnFwd(OUT_B, 50)
        elif(Sensor(IN_4) < THRESH2):
            OnFwd(OUT_B, -50)
            OnFwd(OUT_A, 50)
        else:
            OnFwd(OUT_AB,50)

def main():
    SetSensorTouch(IN_2)
    while Sensor(IN_2) != 1:
        pass

    SetSensorLight(IN_4)
    SetSensorLight(IN_1)
    Wait(2000)

    StartTask(task_ruky)
    StartTask(task_pohyb)
