from tabulate import tabulate; import random
idxx = 0 ##.
msg="I just don't want to be forgotten "*25
sc = open("script.txt").readlines()
print ''.join(open(__file__).readlines()[5:])

f = open(__file__);s = f.readlines();f.close();r = s


'''
    # Bug when openning from out of folder? Fix this shit by Tuesday.
'''
for idx,x in enumerate(s):
    if "##" in x and x[-2] == '.':
        r[idx] = ''.join([" " + str((int(m)+1)%len(sc)) + 
          " " if m.isdigit() else m for m in x.split()] + ["\n"])
    elif "#" in x and (x[-2] == '.' or x[-2] == '?'):
        r[idx] = sc[idxx]; idxx = (idxx + 1) % len(sc)


'''
    # There's probably a better way to do this, but w/e.
'''

tdpg=[['' for _ in xrange(27)] for _ in xrange(5)]
for x in xrange(27*5):tdpg[x/27][x%27] = random.randrange(0,10)

if idxx > 19:
    for x in xrange(5*27): tdpg[x/27][x%27] = msg[x]

#print ''.join(r)
print tabulate(tdpg);f = open(__file__,'w'); f.write(''.join(r)); f.close()

