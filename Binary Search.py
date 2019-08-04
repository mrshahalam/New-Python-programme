pos =-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid = (l+u)//2
        if list[mid]==n:
            globals() ['pos'] = mid
            return  True
        else:
            if list[mid]<n:
                l=mid;
            else:
                u=mid
list=[4,65,54,6,5,47,47,8,68,5,68,54,68,4,24,24,64,22]
n=int(input('enter the number which u want to search\n'))
if search(list,n):
    print('found at index value=',pos)
else:
    print('not found')
