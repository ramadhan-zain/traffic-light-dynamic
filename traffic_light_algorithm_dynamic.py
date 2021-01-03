import time

# num_green_timur = 5
# num_green_selatan = 10 
# num_green_barat = 10
# num_green_utara = 10
ruas = [[0, 0, 5, True],
        [0, 0, 0, False],
        [0, 0, 0, False],
        [0, 0, 0, False]]

# ruas = {
#     "timur":["ON", "OFF", "OFF", True],
#     "selatan":["ON", "OFF", "OFF", False],
#     "barat":["ON", "OFF", "OFF", False],
#     "utara":["ON", "OFF", "OFF", False],
# }

def decrement_number():
    for i in range(len(ruas)):
        if ruas[i][2] >= 0 and ruas[i][3] is True:
            if i is 3:
                ruas[i][2] -= 1
                ruas[0][0] -= 1  
            else:
                ruas[i+1][0] -= 1
                ruas[i][2] -= 1

def decrement_yellow():
    for i in range(len(ruas)):
        if ruas[i][1] > 0 and ruas[i][3] is True:
            if i is 3:
                ruas[i][2] -= 1
                ruas[0][0] -= 1  
            else:
                # ruas[i+1][0] -= 1
                ruas[i][1] -= 1

def red_next_index():
    for i in range(len(ruas)):
        if ruas[i][3] is True:
            if ruas[i][2] < 0:
                if i is 3:
                    ruas[0][0] = 0  
                    ruas[i][2] = 0
                else:
                    ruas[i][2] = 0
                    ruas[i][1] = 1111
                    # ruas[i][1] = 2

                if ruas[i+1][0] == -1:
                    ruas[i+1][0] = 0
                    ruas[i+1][1] = 1111
            else:
                if i is 3:
                    ruas[0][0] = ruas[i][2] + 1
                else:
                    ruas[i+1][0] = ruas[i][2] + 1
        # i += 1

# def yellow_next_index():
#     for i in range(len(ruas)):
#         if ruas[i][2] > 0:
#             if i is 0:
#                 ruas[0][3] = True
#                 ruas[3][3] = False    
#             else:
#                 ruas[i][3] = True
#                 ruas[i-1][3] = False

def yellow_on():
    for i in range(len(ruas)):
        if ruas[i][3] is True:
            if ruas[i][2] is 0:
                ruas[i][1] = 1111

def set_active_status():
    for i in range(len(ruas)):
        if ruas[i][2] > 0:
            if i is 0:
                ruas[0][3] = True
                ruas[3][3] = False    
            else:
                ruas[i][3] = True
                ruas[i-1][3] = False
        # i += 1

while(True):
    decrement_number()
    red_next_index()
    decrement_yellow()
    # yellow_on()
    set_active_status()
    for i in range(len(ruas)):
        if ruas[i][1] == 1110:
            timur.light_on(yellow)
    print(ruas)


    time.sleep(1)




