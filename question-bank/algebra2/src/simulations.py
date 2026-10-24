"""Seeded simulations that produced the histogram counts in data_stat.py. Run: python3 simulations.py"""
import random, statistics as st, math
def binsim(n,p,runs,seed):
    r=random.Random(seed); return [sum(r.random()<p for _ in range(n)) for _ in range(runs)]
def show(name, xs, edges):
    cnt=[sum(1 for x in xs if lo<=x<=hi) for lo,hi in edges]
    print(name, cnt, sum(cnt), 'mean',round(st.mean(xs),3),'sd',round(st.pstdev(xs),4))
# IC2
a=binsim(50,.5,200,1); show('coin50', a, [(0,19),(20,22),(23,25),(26,28),(29,31),(32,33),(34,50)]); print(' >=34',sum(x>=34 for x in a))
b=binsim(40,.25,200,2); show('spin40', b, [(0,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,40)]); print(' >=13',sum(x>=13 for x in b))
c=binsim(60,1/6,200,3); show('die60', c, [(0,5),(6,7),(8,9),(10,11),(12,13),(14,15),(16,60)]); print(' >=16',sum(x>=16 for x in c))
d=binsim(20,.7,200,4); show('ft20', d, [(0,9),(10,11),(12,13),(14,15),(16,17),(18,20)]); print(' <=11',sum(x<=11 for x in d))
e=binsim(100,.5,200,5); show('birth100', e, [(0,41),(42,45),(46,49),(50,53),(54,57),(58,100)]); print(' >=58',sum(x>=58 for x in e))
# IC4 prop
for n,p,s in [(100,.58,6),(300,.40,7),(50,.70,8)]:
    xs=[x/n for x in binsim(n,p,200,s)]; print('prop',n,p,'sd',round(st.pstdev(xs),4), 'min',min(xs),'max',max(xs), sorted(xs)[5], sorted(xs)[194])
    if n==100: show(' bins', xs, [(0,.459),(.46,.499),(.50,.539),(.54,.579),(.58,.619),(.62,.659),(.66,.699),(.70,1)])
# IC4 mean: bootstrap from a sample
r=random.Random(9); sleep=[round(min(10,max(4,r.gauss(6.8,1.35))),1) for _ in range(40)]
m=st.mean(sleep); print('sleep mean',round(m,3),'sd',round(st.stdev(sleep),3))
bs=[st.mean(r.choice(sleep) for _ in range(40)) for _ in range(200)]; print('boot sd',round(st.pstdev(bs),3)); show(' bins',bs,[(0,6.399),(6.4,6.549),(6.55,6.699),(6.7,6.849),(6.85,6.999),(7.0,7.149),(7.15,9)])
# IC5 rerandomization
def rerand(g1,g2,runs,seed):
    r=random.Random(seed); pool=g1+g2; n=len(g1); out=[]
    for _ in range(runs):
        r.shuffle(pool); out.append(st.mean(pool[:n])-st.mean(pool[n:]))
    return out
r=random.Random(10)
A=[22.1,25.3,24.8,27.0,23.9,26.4,25.1,28.2,24.6,26.6]; Bv=[21.0,23.2,22.5,21.8,24.1,22.9,20.7,23.5,22.0,23.3]
diff=st.mean(A)-st.mean(Bv); dd=rerand(A,Bv,200,11); print('fert diff',round(diff,2),'>=',sum(x>=diff-1e-9 for x in dd)); show(' bins',dd,[(-9,-2.0001),(-2,-1.0001),(-1,-0.0001),(0,0.9999),(1,1.9999),(2,2.9999),(3,9)])
