t = int(input())

for i in range(1,t+1):
    s = input()
    y = s[0:4]
    m = s[4:6]
    d = s[6:8]
    if int(m) ==1:
        if int(d) >0 and int(d) < 32:
            print(f"#{i} {s[0:4]}/{s[4:6]}/{s[6:8]}")
        else:
            print(f"#{i} -1")
    elif int(m) ==2:
        if int(d) >0 and int(d) < 29:
            print(f"#{i} {s[0:4]}/{s[4:6]}/{s[6:8]}")
        else:
            print(f"#{i} -1")    
    elif int(m) ==3:
        if int(d) >0 and int(d) < 32:
            print(f"#{i} {s[0:4]}/{s[4:6]}/{s[6:8]}")
        else:
            print(f"#{i} -1")     
    elif int(m) ==4:
        if int(d) >0 and int(d) < 31:
            print(f"#{i} {s[0:4]}/{s[4:6]}/{s[6:8]}")

    elif int(m) ==5:
        if int(d) >0 and int(d) < 32:
            print(f"#{i} {s[0:4]}/{s[4:6]}/{s[6:8]}")
        else:
            print(f"#{i} -1") 
    elif int(m) ==6:
        if int(d) >0 and int(d) < 31:
            print(f"#{i} {s[0:4]}/{s[4:6]}/{s[6:8]}")
        else:
            print(f"#{i} -1") 
    elif int(m) ==7:
        if int(d) >0 and int(d) < 32:
            print(f"#{i} {s[0:4]}/{s[4:6]}/{s[6:8]}")
        else:
            print(f"#{i} -1") 
    elif int(m) ==8:
        if int(d) >0 and int(d) < 32:
            print(f"#{i} {s[0:4]}/{s[4:6]}/{s[6:8]}")
        else:
            print(f"#{i} -1") 
    elif int(m) ==9:
        if int(d) >0 and int(d) < 31:
            print(f"#{i} {s[0:4]}/{s[4:6]}/{s[6:8]}")
        else:
            print(f"#{i} -1") 
    elif int(m) ==10:
        if int(d) >0 and int(d) < 32:
            print(f"#{i} {s[0:4]}/{s[4:6]}/{s[6:8]}")
        else:
            print(f"#{i} -1") 
    elif int(m) ==11:
        if int(d) >0 and int(d) < 31:
            print(f"#{i} {s[0:4]}/{s[4:6]}/{s[6:8]}")
        else:
            print(f"#{i} -1") 
    elif int(m) ==12:
        if int(d) >0 and int(d) < 32:
            print(f"#{i} {s[0:4]}/{s[4:6]}/{s[6:8]}")
        else:
            print(f"#{i} -1") 
    else:
        print(f"#{i} -1")
    