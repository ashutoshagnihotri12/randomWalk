import sys
sys.path.append('/ufs/agnihotr/randomWalk/stdlib-python')
import stdio
import random
pos_1 = 0.0
t = 0
for j in range(0,10):
	q = random.choice([-1,1])
	pos_1 = pos_1 + q
	t = t + 1
	stdio.writeln(pos_1)
# p=random.randrange(0,2)
# if p==0:
	# stdio.writeln('Heads')
# else:
# 	stdio.writeln('Tails')
# stdio.writeln(q)


#--------------------------------------------------------------------#
# Junk code
#--------------------------------------------------------------------#
# sys.path.append('/ufs/agnihotr/randomWalk/stdlib-python')
# print(sys.path)