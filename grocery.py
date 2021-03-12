b=int(input('Enter Your budget : '))
d={}
f=0
while(True):
    if b==0:
      print('Budget is zero.No more items can be added.')
      break
    else:
      print('1 .Add an item\n 2 .Exit')
      c=int(input('Enter your choice : '))
      if c==2:
        break
      else:
        s=input('Enter product : ')
        q=input('Enter quantity : ')
        p=int(input('Enter Price : '))
        if s not in d:
          d[s]=p
          if b>p:
            b=b-p
            print('Amount left : ',b)
          else:
            print('Over price')
        else:
          d[s]=d[s]+p
          if b>p:
            b=b-p
            print('Amount left : ',b)
          else:
            print('Over price')
for i in d:
  if b>=d[i]:
    print('Amount left can buy you',i)
  else:
    f=1
if f==1:
  print('No amount left.')
print('Grocery List')
for i in d:
  print(i,' ',d[i])
