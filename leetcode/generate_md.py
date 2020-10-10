s=open("in.txt").readlines()[0]
s_0=s[5:len(s)]
s_0=s_0.strip()
s_1=open("in.txt").readlines()[1]
s_2=open("in.txt").readlines()[2:len(open("in.txt").readlines())]
s_3=len(s_1)
s_4=s_3-2
l=s_1[30:s_4]
a="# Intervals"
b='+ [{d}](#{e})'.format(d=s_0,e=l)
c="## {f}".format(f=s_0)
p="'''python"
s_5=''.join(s_2)
n=s_5.strip('/n')
m="'''"
g=open('intervals.md', "x")
g.write(a+'\n'+'\n')
g.write(b+'\n'+'\n')
g.write(c+'\n'+'\n')
g.write(s_1+'\n')
g.write(p+'\n')
g.write(n+'\n')
g.write(m+'\n')