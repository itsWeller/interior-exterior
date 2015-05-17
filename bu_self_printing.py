idxx= 0 ##.
sc = open("script.txt").readlines()

print open(__file__).read()

#Test.......
f = open(__file__)
s = f.readlines()

r = s

f.close()

for idx,x in enumerate(s):
    if "##" in x and x[-2] == '.':
        r[idx] = ''.join([" " + str((int(m)+1)%len(sc)) + " " if m.isdigit() else m for m in x.split()] + ["\n"])
    elif "#" in x and (x[-2] == '.' or x[-2] == '?'):
        r[idx] = sc[idxx]

#print ''.join(r)
f = open(__file__,'w')
f.write(''.join(r))
f.close()

