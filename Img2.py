import numpy as np

def forward (j,y,b,a,current_state,fast_dict):
    if (fast_dict[(j),(current_state)]==0):
        base=int(y[j])
        if (j==0):
            return b[0][base]
        else:
            bar=0
            if (a[0][current_state]!=0):                                                  #is it possible to go from some state to this state
                bar+=a[0][current_state]*forward(j-1,y,b,a,0,fast_dict)
            if (a[1][current_state]!=0):
                bar+=a[1][current_state]*forward(j-1,y,b,a,1,fast_dict)
            if (a[2][current_state]!=0):
                bar+=a[2][current_state]*forward(j-1,y,b,a,2,fast_dict)
            if (a[3][current_state]!=0):
                bar+=a[3][current_state]*forward(j-1,y,b,a,3,fast_dict)
            print('symbol ', j,' state ', current_state)
            return b[current_state][base]*bar
    else:
        return fast_dict[j,current_state]

foo=True
a=[[0.0,1.0,0.0,0.0,0.0],   #E1 (E1,E2,E3,I,Stop)
   [0.0,0.0,1.0,0.0,0.0],   #E2
   [0.3,0.0,0.0,0.3,0.4],   #E3
   [0.5,0.0,0.0,0.5,0.0]]   #I
b=[[0.27,0.25,0.31,0.17],   #E1 (A,C,G,T)
   [0.31,0.23,0.19,0.27],   #E2
   [0.19,0.30,0.29,0.22],   #E3
   [0.30,0.20,0.20,0.30]]   #E4
y_raw=input('Print sequence ')
y=''
for i in range(len(y_raw)):
    if y_raw[i]=='A':
        y+='0'
    elif y_raw[i]=='C':
        y+='1'
    elif y_raw[i]=='G':
        y+='2'
    elif y_raw[i]=='T':
        y+='3'
    else:
        print('Incorrect input: use A,C,G and T only')
        foo=False
        break
print('reworked y is ', y)
if foo:
    j=len(y_raw)-1
    current_state=2
    fast_dict=np.zeros(((j+1),(j+1)))
    probability=0.4*forward(j,y,b,a,current_state,fast_dict)
    print('Probability=', probability)
