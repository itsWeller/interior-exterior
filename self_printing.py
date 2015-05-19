from tabulate import tabulate; import random
idxx = 0 ##.
sc = open(".script.txt").readlines()
#msg="Stop. It's already too late"*25
msg="Sorry.Time's up.Say goodbye"*25
if idxx>28:
    f = open(__file__,'w'); f.write("'''\n# Don't worry, you'll be seeing me again soon\n'''\nprint('Goodbye.')\n"); f.close()
print ''.join(open(__file__).readlines()[9:])
f = open(__file__);s = f.readlines();f.close();r = s


'''
    # Bug when openning from out of folder? Fix this shit by Tuesday.
'''
for idx,x in enumerate(s):
    if "##" in x and x[-2] == '.':
        r[idx] = ''.join([" " + str((int(m)+1)) + 
          " " if m.isdigit() else m for m in x.split()] + ["\n"])
    elif "#" in x and (x[-2] == '.' or x[-2] == '?'):
        r[idx] = sc[idxx]; idxx = (idxx + 1) 


'''
    # There's probably a better way to do this, but w/e. I'm lazy.
'''

tdpg=[['' for _ in xrange(27)] for _ in xrange(5)]
for x in xrange(27*5):tdpg[x/27][x%27] = str(random.randrange(0,10))

for _ in xrange((idxx)*7): 
    na=random.randrange(0,27*5);tdpg[na/27][na%27]=msg[na%len(sc)]
if idxx > 26:
    for x in xrange(5*27): tdpg[x/27][x%27] = msg[x]

print tabulate(tdpg);f = open(__file__,'w'); f.write(''.join(r)); f.close()

