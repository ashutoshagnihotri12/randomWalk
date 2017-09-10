import sys
sys.path.append('/ufs/agnihotr/randomWalk/stdlib-python') #linux-path
sys.path.append('/Users/ashutosh/randomWalk/stdlib-python') #mac-path
import stdio
import random
f = open('output_file.dat','w')
# f.write('1-Success!\n')
# f.write('2-Success-repeated!')
pos_1 = 0.0
t = 0
for j in range(0,100):
	q = random.choice([-1,1])
	pos_1 = pos_1 + q
	t = t + 1
	# stdio.writeln(pos_1)
	f.write("%i %i\n" % (j,pos_1))
f.close()
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