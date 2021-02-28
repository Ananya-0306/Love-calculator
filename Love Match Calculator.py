import collections

print("*****************************")  
print("*   Love Match Calculator   *")  
print("*****************************") 
bn="Gunjan"
gn="Ananya"

print("Boy Name: "+bn)
print("Girl Name: "+gn)
print("\nCalculating...")

thestring=bn+"love"+gn
d = collections.defaultdict(int)
for c in thestring:
    d[c] += 1
a=list(d.values())
while True:
	print(" ".join(map(str, a)))
	if len(a)==2:
	 break
	b=[]
	for x,y in enumerate(a):
		b=b+list(map(int,str(a[len(a)-1-x]+y)))
		if x+1==int(len(a)/2):
			if len(a)%2!=0:
				b.append(a[len(a)-2-x])
			break
	a=b

print("\nLove match % for '"+bn+"' and '"+gn+"' is")
print(f'''
						   Love        Love
						 Love Love  Love Love
						Love     Love     Love
						Love              Love
						 Love     {"".join(map(str, a))}%    Love
						  Love          Love
						    Love      Love
						      Love  Love
						         Love
						         ''')
