#  https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
elements = list(map(int, input().split()))

n = len(elements)%k
roomSet = set(elements) 
sumRoomSet = sum(roomSet) 
sumelements = sum(elements) 
temp = sumRoomSet * k - sumelements  
print(temp//(k - 1))