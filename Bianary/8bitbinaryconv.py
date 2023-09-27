b=str()
a=str()
Digit=str() 
binary1=str()
binary2=str()
binary3=str()
binary4=str()
binary5=str()
binary6=str()
binary7=str()
binary8=str()

Dennum=str()
y= 7
for x in range(0,8):
 a=y-x
 Digit = 2**a 
 if x == 0:
  binary1=Digit
 if x ==1:
  binary2=Digit
 if x==2:
  binary3=Digit
 if x==3:
  binary4=Digit
 if x==4:
  binary5=Digit
 if x==5:
  binary6=Digit
 if x==6:
  binary7=Digit
 if x==7:
  binary8=Digit
Dennum=int(input("What is the number you wish to converter to binary between 0 and 255"))
if Dennum<0 or Dennum>255:
 print ('error please input valid number')  
if Dennum>=binary1:
 Dennum=Dennum-binary1
 binary1="1"
else:
  binary1="0"
if Dennum>=binary2:
  Dennum=Dennum-binary2
  binary2="1"
else:
  binary2="0"
if Dennum>=binary3:
  Dennum=Dennum-binary3
  binary3="1"
else:
  binary3="0"
if Dennum>=binary4:
  Dennum=Dennum-binary4
  binary4="1"
else:
  binary4="0"    
if Dennum>=binary5:
  Dennum=Dennum-binary5
  binary5="1"
else:
  binary5="0"  
if Dennum>=binary6:
  Dennum=Dennum-binary6
  binary6="1"
else:
 binary6="0"  
if Dennum>=binary7:
  Dennum=Dennum-binary7
  binary7="1"
else:
  binary7="0"
if Dennum>=binary8:
  Dennum=Dennum-binary8
  binary8="1"
else:
  binary8="0"
if Dennum==0:
 a=[binary1,binary2,binary3,binary4,binary5,binary6,binary7,binary8]
 b= "".join(a)
 print("The binary number is",b)