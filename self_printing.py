# -*- coding: utf-8 -*-
from tabulate import tabulate; import random
idxx = 0 ##.
sc = open("script.txt").readlines()
msg="Stop. It's already too late"*25
if idxx>25:
    aas=unicode("\n\n\t\tG̮͔̯͓̻̣͖̠͉̳̯͕͈͙̤̱̓̿̈ͬͨ͗ͤ͒ͪ̈́̇̀̃̅̈͐̚ ̰̺͉̭̳̝͎̙̠̞̻͑̔̈́̄͒̚ o̖̜͔̪̳̺͚̠̩̦͍͖̖͚͎̍̎͊̄̿̒̊͑̎͐ͣ̌ͭ͑ ͍̫̺̒͊̈ͨ̇́̚ o̰̰͓̮͇̮̹̖̜̼͔̦̪ͭ̓̅͊ͭͮ̊̅̋̇́͌̎͑͐̒ ̖̩͈̱̤̥̗̭̤͖̜̻̼̯͆̒ͧ̎ͧ͛̇̓̒ ḋ̫͍̱͇̙͙̳̖̰͉̜̤̳̘̥͕̤ͩ͗ͪ̈́͂ͧ̈̏͑̌͊̆ͫͅ ̦͈̘͙̩̗̆ͦ̊ͧͮ̀̄ͦ̽ͧͤ̄̏ͪ̂̚ b̬͙͓̙̬̳͇̰̖͇̻͕ͧ̾͑̑ͦ̑̈͂ͯ͊ ̜̱̰̰͉̱͔̜̹͎̞̙͓̺͖̞̹̿̿ͤ͗̏͋ͅ y̘̺̙̣̰̮̮̰̟͓̦͉̼̺̠̱͍͓ͤ͒ͭ̋ͬ͂͋͐̎̇̈́̍̽ ̳̳̫̭͙̬̦ͮͣͤ͗̊ͨ e̹̫̻̱̘͈̭͔͉̎͛͗͑̌ͤ͗̍̋̂̇\n\n",'utf-8')
    print aas
    exit();
print ''.join(open(__file__).readlines()[10:])

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
    # There's probably a better way to do this, but w/e.
'''

tdpg=[['' for _ in xrange(27)] for _ in xrange(5)]
for x in xrange(27*5):tdpg[x/27][x%27] = str(random.randrange(0,10))

for _ in xrange((idxx)*7): 
    na=random.randrange(0,27*5);tdpg[na/27][na%27]=msg[na%len(sc)]
if idxx > 22:
    for x in xrange(5*27): tdpg[x/27][x%27] = msg[x]

#print ''.join(r)
print tabulate(tdpg);f = open(__file__,'w'); f.write(''.join(r)); f.close()

