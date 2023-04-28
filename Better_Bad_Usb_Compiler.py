import os
go = 0
with open('run_out.txt', 'w') as o:
    o.write('')
outputname = input('Input the name of your project (if you leave it blank it will defolt to "output")\n:')

if outputname == (''):
    outputname = ('output')
code = []

commands = ['ctrl','shift','alt','gui','windows','ctrl-alt','ctrl-shift','alt-shift','alt-gui','gui-shift','down','left','right','up','enter','break','pause','capslock','delete','backspace','end','escape','home','insert','numlock','pageup','pagedown','printscreen','scrollock','space','tab','menu', 'app', 'sysrq','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18','f19','f20','f21','f22','23','f24']


with open('run.txt') as f:
    line = f.readlines()



for c in line:
    c = c.replace('\n','')



    if c == ('run'):
        code.append('GUI r')
        
    elif c.startswith('s'):
        l = c.replace('s',' ', 1)
        code.append('STRING' + l)
        
    elif c.startswith('d'):
        l = c.replace('d',' ', 1)
        
        code.append('DELAY' + l)

    elif c.startswith('r'):
        l = c.replace('r',' ', 1)
        
        code.append('REPEAT' + l)
    else:
        for p in commands:
            if c == p:
                code.append(c.upper())


with open(outputname+'.txt', 'a') as o:
    for i in code:
        o.write(i+'\n')


