import sys


class Node:
    def __init__(self,index,val):
        self.index=index
        self.value=val
        self.prev=None
        self.next=None

class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0

    def unshift(self,index,val):
        node=Node(index,val)

        if self.count==0:
            self.front=node
            self.rear=node
        else :
            front=self.front
            front.prev=node
            node.next=front
            self.front=node
        self.count+=1

    def shift(self):
        if self.count==0:
            return None
        value=self.front.value
        if self.count==1:
            self.__init__()
        else:
            self.front=self.front.next
            self.front.prev=None
            self.count-=1

        return self.count

    def push(self,index,val):
        node=Node(index,val)

        if self.count==0:
            self.front=node
            self.rear=node
        else:
            rear=self.rear
            rear.next=node
            node.prev=rear
            self.rear=node
        self.count+=1

    def pop(self):
        if self.count==0:
            return None
        value=self.rear.value
        if self.count==1:
            self.__init__()
        else:
            self.rear=self.rear.prev
            self.rear.next=None
            self.count-=1
        return self.count

    def size(self):
        return self.count

    def isEmpty(self):
        return self.size()==0

    def getFront(self):
        return self.front
    def getBack(self):
        return self.rear

input = sys.stdin.readline

N=int(input())
ballons=list(enumerate(map(int,input().split())))
deque=Deque()

for (index,value) in ballons:
    deque.push(index,value)

result=''

while not deque.isEmpty():
    node=deque.getFront()
    result+=f'{node.index+1} '
    cnt=node.value
    deque.shift()

    if deque.isEmpty():
        break

    if cnt>0:
        while cnt-1>0:
            tmp=deque.getFront()
            deque.push(tmp.index,tmp.value)
            deque.shift()
            cnt-=1
    else:
        while cnt<0:
            tmp=deque.getBack()
            deque.pop()
            deque.unshift(tmp.index,tmp.value)
            cnt+=1


print(result)