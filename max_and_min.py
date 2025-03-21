a, b, c= input().split() 

x, y, z = input().split()

if (a == b):
  print("Max :",max(int(x),int(y),int(z)))

elif (a == c):
    print("Min :",min(int(x),int(y),int(z)))

else  :
    print("none")
    