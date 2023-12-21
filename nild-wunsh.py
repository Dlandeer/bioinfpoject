def eq(a,b):
    if a==b:
        return 0
    else:
        return 1
A=input()
B=input()
Av=str()
Bv=str()
l=[]
for i in range(len(A)+1):
    l.append([0]*(len(B)+1))
mismatch_penalty=-6
gap_penalty=mismatch_penalty*0.5
for i in range (len(A)+1):
    for j in range (len(B)+1):
        if i==0 and j==0:
            l[i][j]=0
        elif i==0:
            l[i][j]=l[i][j-1]+gap_penalty
        elif j==0:
            l[i][j]=l[i-1][j]+gap_penalty
        else:
            l[i][j]=max(l[i-1][j-1]+eq(A[i-1],B[j-1])*mismatch_penalty,l[i][j-1]+gap_penalty,l[i-1][j]+gap_penalty)
i=len(A)
j=len(B)
while i>0 and j>0:  
    delA=l[i-1][j]
    delB=l[i][j-1]
    ins=l[i-1][j-1]
    if l[i][j]==ins+mismatch_penalty*eq(A[i-1],B[j-1]):
        Av+=A[i-1]
        Bv+=B[j-1]
        i-=1
        j-=1
    elif l[i][j]==delA+gap_penalty:
        Av+=A[i-1]
        Bv+="_"
        i-=1
    elif l[i][j]==delB+gap_penalty:
        Av+="_"
        Bv+=B[j-1]
        j-=1
while i>0:
    Av+=A[i-1]
    Bv+="_"
    i-=1
while j>0:
    Av+="_"
    Bv+=B[j-1]
    j-=1
Av1=str()
Bv1=str()
for i in range(1,len(Av)+1):
    Av1+=Av[-i]
    Bv1+=Bv[-i]
print(Av1)
print(Bv1)