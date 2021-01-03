import time

ruas = {
    "timur":["STOP", 0, 0],
    "selatan":["STOP", 0, 0],
    "barat":["STOP", 0, 0],
    "utara":["STOP", 0, 0],
}

def decrement_number(num):
    for i in range(0, num):
        num -= 1
        print(num)
lst_ruas = list(ruas.items())

num_green_timur = 5
num_green_selatan = 10
yellow_num = 1
yellow_num_next = 1
yellow_num_next_next = 1
yellow_num_next_next_next = 1
while(True):
    
    # if ruas["timur"][2] >= 0:
    ruas["timur"][0] = 0
    ruas["timur"][2] = num_green_timur
    ruas["selatan"][0] = ruas["timur"][2] + 1
    
    if ruas["timur"][2] < 0:
        ruas["timur"][2] = 0
        ruas["timur"][1] = yellow_num

        yellow_num -= 1

        if ruas["selatan"][0] < 0:
            ruas["selatan"][0] = 0
            ruas["selatan"][1] = yellow_num_next

            yellow_num_next -= 1

        if ruas["selatan"][1] < 0:
            ruas["selatan"][1] = 0
            ruas["selatan"][2] = num_green_selatan
            ruas["barat"][0] = num_green_selatan + 1


            num_green_selatan -= 1
        
        if ruas["selatan"][2] < 0:
            ruas["selatan"][2] = 0
            ruas["selatan"][1] = yellow_num_next_next
            ruas["barat"][0] = 0

            yellow_num_next_next -= 1

        if ruas["timur"][1] < 0:
            ruas["timur"][1] = 0
            ruas["timur"][0] = "STOP"
    print(ruas)

    # while(num_green_timur >= 0):
    num_green_timur -= 1

    # while(num_green_selatan >=0):
    #     num_green_selatan -= 1
    time.sleep(1)




