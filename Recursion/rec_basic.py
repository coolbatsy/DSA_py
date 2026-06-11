
count = 0

def func():
    global count
    if count == 4:
        return
    count+=1
    print("nigga") #primary obj
    func() #recursive call later

func()




def func1():
    global count 
    if count ==4:
        return 
    count+=1
    func1() #recursive call earlier
    print("niggi") #primary obj

func1()

