#2
print(5**9)
print(3//2)
print(7//3)
print(6==6)
a = 20; a+=30; a%3; print(a)
print(True * False)
print(True & False)
print(True and False)
print(((6>3) and (7<4) or (18 ==3)) and (9>3))
print(True is False)
#print ('False in 'False') --> shows error
print((True== False) or (False > True)) and (False <= True)


#3
s1="Nice to have it"
s2="here"
print(s1+" "+s2)

#4
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#5
a.insert(0,s1)
a.append(s2)
print(a)

#6
numbers=[386,462,47,418,907,344,236,375,823,566,597.978,328,615,953,345,399,162,758,219,918,237,412,566,826,248,866,950,626,949,687,217,815,67,104,58,512,24,892,894,767,553,81,379,843,831,445,742,717,958,743,527]
for x in numbers:
    if(x%2==0):
        print(x)
    elif(x==237):
            break
    
  

        
        
#7
color_list_1 = set(["White","Black","Red"])
color_list_2 = set(["Red","Green"])
print(color_list_1 - color_list_2)

#8
string= input("Entera string")
string = set(string)
alpha=list('abcdefghijklmnopqrstuvwxyz')
i=0
for word in string:
    if(word in alpha):
        i+=1
if(i==26):
    print('String is Pangarm')
else:
    print('String is not Pangram')


            
#9
a=int(input("enter an integer"))
n=int("%d" % a)
nn=int("%d%d" % (a,a))
nnn=int("%d%d%d" % (a,a,a))
print(n+nn+nnn)

#11
a=input("enter the words")
a_list = a.split(",")
a_list.sort()
print((',').join(a_list))

#12
d={'Student':[ 'Rahul','Kishore','Vidhya','Raakhi'],'Marks':[57,87,67,79]}
marks_list= d.get('Marks')
student_list=d.get('Student')
num = marks_list.index(max(marks_list))
print(student_list[num])

#13
s=input("Enter a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
        print("Letters",l)
        print("Digits",d)

#16
up= eval(input("UP"))
down=eval(input("DOWN"))
left=eval(input("LEFT"))
right=eval(input("RIGHT"))
print(int((((up-down)**2)+((left-right)**2))**0.5))                  
           
         
                  


                    
    
