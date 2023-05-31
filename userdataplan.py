udays=84
ucalls=3000
umsg=100
udata=2
calls=int(input("Calls: "))
msg=int(input("Messages: "))
days=int(input("Days: "))
data=float(input("Data: "))
remcalls=ucalls-calls if ucalls>=calls and calls>0 else "invalid"
remmsg=umsg-msg if umsg>=msg and msg>0 else "invalid"
remdata=round(udata-data,2) if udata>=data and data>0 else "invalid"
remdays=udays-days if udata>=data and days>0 else "invalid"
print("Remaining calls: ",remcalls)
print("Remaining messages: ",remmsg)
print("Remaining data: ", remdata)
print("Remaining days: ",remdata)