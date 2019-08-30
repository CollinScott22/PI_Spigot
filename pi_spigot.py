

def pi_digits() {
	a,b,c,d,e,f = 1,0,1,1,3,3
	while True:
		if 4*a+b-c < e*c:
			yield n
			a,b,c,d,e,f = (10*a,10*(b-e*c),c,d,(10*(3*a+b))/c-10*e,f)
		else:
			a,b,c,d,e,f = (a*d, (2*a+b)*f,c*f,d+1(a*(7*d+2)+b*f)/(c*f),f+2)


}


def run(n){
	digits = pi.pi_digits()
	for i in range n:
		print(digits.next())
}
### What makes this algorithm work is that 