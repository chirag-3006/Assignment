name=input("Enter your name ")

gender=input("Enter your gender ")

item_1=input("Enter Name item 1 ")
qty_1=int(input("Enter no. Quantity "))
price_1=10

t1=price_1*qty_1

if qty_1>4:
    r1=(t1*5)/100
    dt1=t1-r1
    v1=dt1
else:
    v1=t1

item_2=input("Enter Name item 2 ")
qty_2=int(input("Enter no. Quantity "))
price_2=20

t2=price_2*qty_2

item_3=input("Enter Name item 3 ")
item_3qty=int(input("Enter no. Quantity "))
price_3=30

t3=price_3*item_3qty

item_4=input("Enter Name item 4 ")
qty_4=int(input("Enter no. Quantity "))
price_4=40

t4=price_4*qty_4

item_5=input("Enter Name item 5 ")
qty_5=int(input("Enter no. Quantity "))
price_5=50

t5=price_5*qty_5

r5=(t5*10)/100
dt5=t5-r5
v5=dt5

item_6=input("Enter Name item 6 ")
qty_6=int(input("Enter no. Quantity "))
price_6=60

t6=price_6*qty_6


item_7=input("Enter Name item 7 ")
qty_7=int(input("Enter no. Quantity "))
price_7=70


t7=price_7*qty_7


item_8=input("Enter Name  item 8 ")
qty_8=int(input("Enter no. Quantity "))
price_8=80


t8=price_8*qty_8


item_9=input("Enter Name item 9 ")
qty_9=int(input("Enter no. Quantity "))
price_9=90

t9=price_9*qty_9

item_10=input("Enter Name item 10 ")
qty_10=int(input("Enter no. Quantity "))
price_10=100

t10=price_10*qty_10

r10=(t10*15)/100
dt10=t10-r10
v10=dt10

# AP = Actual Price
AP=t1+t2+t3+t4+t5+t6+t7+t8+t9+t10

# DP = Price after product discounts
DP=v1+t2+t3+t4+v5+t6+t7+t8+t9+v10



# Bill level discount

if DP>10000:
    rt=(DP*15)/100
    dtt=DP-rt

elif DP>=5000:
    rt=(DP*10)/100
    dtt=DP-rt

else:
    rt=0
    dtt=DP


rdtt=(dtt*10)/100
after_gst=dtt+rdtt

after_gst_AP=AP+rdtt


y=input("Do you need bag? ")

if y.lower()=="yes":
    bag=10
    after_gst=after_gst+10

else:
    bag=0





print()
print("                         D-Mart")
print("   Name :",name,"\t\t\tData : 12/9/2022")
print("   -----------------------------------------------------------")
print("   Item Name\tQuantity\tPrice\tTotal\tAfter-Discount")
print("   -----------------------------------------------------------")

print("   ",item_1,"\t\t",qty_1,"\t\t",price_1,"\t",t1,"\t",v1)
print("   ",item_2,"\t\t",qty_2,"\t\t",price_2,"\t",t2,"\t",t2)
print("   ",item_3,"\t\t",item_3qty,"\t\t",price_3,"\t",t3,"\t",t3)
print("   ",item_4,"\t\t",qty_4,"\t\t",price_4,"\t",t4,"\t",t4)
print("   ",item_5,"\t\t",qty_5,"\t\t",price_5,"\t",t5,"\t",v5)
print("   ",item_6,"\t\t",qty_6,"\t\t",price_6,"\t",t6,"\t",t6)
print("   ",item_7,"\t\t",qty_7,"\t\t",price_7,"\t",t7,"\t",t7)
print("   ",item_8,"\t\t",qty_8,"\t\t",price_8,"\t",t8,"\t",t8)
print("   ",item_9,"\t\t",qty_9,"\t\t",price_9,"\t",t9,"\t",t9)
print("   ",item_10,"\t\t",qty_10,"\t\t",price_10,"\t",t10,"\t",v10)

print("   -----------------------------------------------------------")

print("\t\t\t\t\tA.P\tD.P")
print("\t\t\t\t\t",AP,"\t",DP)

print()
print("Gift :",end=" ")

if gender.lower()=="female":
    print("Cadbury")
else:
    print("Ledger Wallet")

print("\t\t\t\t\t0.00\t\t0.00")

print()
print("Carry Bag :",y,"\t\t\t10.00\t\t10.00")

print()
print("GST (10%)\t\t\t\t",rdtt,"\t",rdtt)

print("   -----------------------------------------------------------")

print("\t\t\t\t",after_gst_AP,"\t",after_gst)

print()
print("                       Thank You")
print("                        To Visit")
print("                         D-Mart")

print("   -----------------------------------------------------------")