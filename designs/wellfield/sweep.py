import sys, json, numpy as np
from multiprocessing import Pool
from operate import *

def one(args):
    seed, pname, kw = args
    pol = {'conv': Conventional, 'cl': ClosedLoop}[pname](**kw)
    r = run(Scenario(seed), pol)
    r.pop('monthly')
    return seed, pname, json.dumps(kw), r

if __name__ == '__main__':
    seeds = range(int(sys.argv[1]), int(sys.argv[2]))
    jobs = []
    for s in seeds:
        for c in (None, 10, 20, 30):
            jobs.append((s, 'conv', {'cutoff_mgL': c}))
        jobs.append((s, 'cl', {}))
    with Pool(4) as p:
        out = p.map(one, jobs)
    with open(sys.argv[3], 'w') as f:
        json.dump(out, f)
