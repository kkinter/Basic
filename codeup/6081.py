a= input()
#  d = int(input(),16)
#  print(a)
for i in range(1,16):
    print("{}*{}={}".format(a,format(i,'X'),format(int(a,16)*i,'X')))