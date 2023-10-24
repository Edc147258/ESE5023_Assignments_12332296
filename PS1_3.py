def Pascal_triangle(k):
    list=[0,1,0]
    list2=[]
    for i in range(k):
        list2.append(0)
        left=0
        right=1
        while right<len(list):
            list2.append(list[left]+list[right])
            left+=1
            right+=1
        list2.append(0)
        list.clear()
        for item in list2:
            list.append(item)
        list2.clear()
    return list[1:-1]

if __name__ == '__main__':
    k=int(input())
    ret=Pascal_triangle(k)
    print(ret)