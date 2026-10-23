import numpy as np
# approx nameplate MW, Nevada hydrothermal fields (from memory/ repo; unverified), (MW, first-power year, blind?)
d=[("McGinness",160,2012,1),("Steamboat",100,1986,0),("Dixie Valley",65,1988,0),("Blue Mtn",49.5,2009,1),
("Patua",48,2013,0),("Stillwater",47,1989,1),("Don A Campbell",42,2013,1),("Brady+DesertPeak",48,1985,1),
("Tungsten Mtn",26,2017,1),("North Valley",25,2022,0),("Soda Lake",23,1987,1),("Salt Wells",23,2009,0),
("Tuscarora",18,2012,0),("Jersey Valley",22,2011,1),("Beowawe",17,1985,0),("San Emidio",14,1987,0),
("Dixie Meadows",12,2024,0),("Wabuska",2,1984,0)]
mw=np.array([x[1] for x in d]); yr=np.array([x[2] for x in d]); bl=np.array([x[3] for x in d])
l=np.log(mw); print("n",len(mw),"sum",mw.sum(),"median",np.median(mw),"mean",mw.mean())
print("lognormal mu,sigma",l.mean(),l.std(ddof=1),"median",np.exp(l.mean()))
m=mw[mw>=15]; print("Hill alpha (xmin 15)",len(m)/np.sum(np.log(m/15)))
print("blind mean",mw[bl==1].mean(),"nonblind mean",mw[bl==0].mean(),"blind median",np.median(mw[bl==1]),np.median(mw[bl==0]))
o=np.argsort(yr); print("cumulative by year:"); c=np.cumsum(mw[o]);
for y,s,n in zip(yr[o],c,mw[o]): print(y,n,round(s))
import math
def rank(a):
    o=np.argsort(a); r=np.empty(len(a)); r[o]=np.arange(len(a)); return r
print("spearman",np.corrcoef(rank(yr),rank(mw))[0,1])
mu,sg=l.mean(),l.std(ddof=1)
ncdf=lambda z:0.5*(1+math.erf(z/math.sqrt(2)))
for t in [10,20,30,50,100]: print(t,1-ncdf((math.log(t)-mu)/sg))
rng=np.random.default_rng(0)
for beta in [0,0.5,1.0]:
  for N in [30,60,120]:
    rem=[];rs=[]
    for k in range(2000):
      x=np.exp(rng.normal(mu,sg,N)); w=x**beta; idx=rng.choice(N,18,replace=False,p=w/w.sum())
      m=np.ones(N,bool); m[idx]=False; rem.append(np.median(x[m])); rs.append(np.median(x[idx]))
    print("beta",beta,"N",N,"found",round(np.mean(rs),1),"left",round(np.mean(rem),1))
