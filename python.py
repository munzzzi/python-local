greeting="bong ju!!"

print(greeting)
print(greeting)
print(greeting)
print(greeting)
print(greeting)

import random
menu=["삼겹살","샤브샤브","치킨","국밥"]
pick = random.choice(menu)
#랜덤으로 뽑을때
print(pick)

import random
#numbers에1부터45넣기
numbers= range(1,46)
a=random.sample(numbers,6)
#오름차순정렬 a.sort()
#내림차순정렬 a.sort(reverse=True)
a.sort(reverse=True)
print(a)
##