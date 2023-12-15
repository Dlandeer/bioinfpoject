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
for i in range(len(A)):
    l.append([0]*len(B))
mismatch_penalty=-6
gap_penalty=mismatch_penalty*0.5
for i in range (len(A)):
    for j in range (len(B)):
        if i==0 and j==0:
            l[i][j]=0
        elif i==0:
            l[i][j]=l[i][j-1]+gap_penalty
        elif j==0:
            l[i][j]=l[i-1][j]+gap_penalty
        else:
            l[i][j]=max(l[i-1][j-1]+eq(A[i],B[j])*mismatch_penalty,l[i][j-1]+mismatch_penalty,l[i-1][j]+mismatch_penalty)
i=len(A)-1
j=len(B)-1
while i>-1 or j>-1:
    if i==0 and j==0:
        Av+=A[i]
        Bv+=B[j]
        i-=1
        j-=1
    elif i==0:
        Av+="-"
        Bv+=B[j]
        j-=1
    elif j==0:
        Av+=A[i]
        Bv+="-"
        i-=1
    else:    
        delA=l[i][j]-l[i-1][j]
        delB=l[i][j]-l[i][j-1]
        ins=l[i][j]-l[i-1][j-1]
        min1=min(delA,delB,ins)
        if min1==ins:
            Av+=A[i]
            Bv+=B[j]
            i-=1
            j-=1
        elif min1==delA:
            Av+=A[i]
            Bv+="-"
            i-=1
        elif min1==delB:
            Av+="-"
            Bv+=B[j]
            j-=1
Av1=str()
Bv1=str()
for i in range(1,len(Av)+1):
    Av1+=Av[-i]
    Bv1+=Bv[-i]
print(Av1)
print(Bv1)