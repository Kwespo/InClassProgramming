d=int()
a=int()
Num_Letter={'A':'10','B':'11','C':'12','D':'13','E':'14','F':'15'}
binary1=int()
binary2=int()
binary3=int()
binary4=int()
binary5=int()
binary6=int()
binary7=int()
binary8=int()
Num=str(input("Input hex character you want to convert to Binary"))
a= int(Num_Letter.get(Num))
for x in range(0,8):
    d = 7-x
    if x==0:
       binary1=2**d
    if x==1:
        binary2=2**d
    if x==2:
        binary3=2**d
    if x==3:
        binary4=2**d
    if x==4:
        binary5=2**d
    if x==5:
        binary6=2**d
    if x==6:
        binary7=2**d
    if x==7:
        binary8=2**d
if a>= binary1:
   a=a-binary1
   binary1='1'
else:
    binary1='0'
if a>=binary2:
    a=a-binary2
    binary2='1'
else:
 binary2='0'
if a>=binary3:
    a=a-binary3
    binary3='1'
else:
    binary3='0' 
if a>=binary4:
    a=a-binary4
    binary4='1'
else:
    binary4='0'        
if a>=binary5:
    a=a-binary5
    binary5='1'
else:
    binary5='0'
if a>=binary6:
    a=a-binary6
    binary6='1'
else:
    binary6='0'
if a>=binary7:
    a=a-binary7
    binary7='1'
else:
    binary7='0'
if a>=binary8:
    a=a-binary8
    binary8='1'
else:
    binary8='0'
if a==0:    
    b=[binary1,binary2,binary3,binary4,binary5,binary6,binary7,binary8]
    c=''.join(b)
print("Your binary number is",c)


