pos =-1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals() ['pos']=i
            return True
        i=+1
        return False

list =[3,5,1,7,5,9,8,6]
n=int(input('enter the element u want to search=\n'))
if search(list, n):
    print('found at index value is=',pos)
else:
    print('not found')
