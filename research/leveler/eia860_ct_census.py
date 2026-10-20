import pandas as pd, sys
f=sys.argv[1]
xl=pd.ExcelFile(f); print(xl.sheet_names)
op=pd.read_excel(f,sheet_name=0,header=1)
print(op.columns.tolist()[:40])
gt=op[op['Prime Mover'].isin(['GT'])]
gt=gt[gt['Energy Source 1'].isin(['NG','DFO','KER','JF','RFO'])]
print('operable GT units',len(gt),'MW',round(gt['Nameplate Capacity (MW)'].sum()))
print(gt.groupby('Status')['Nameplate Capacity (MW)'].agg(['count','sum']).round())
gt['age']=2025-gt['Operating Year']
print(pd.cut(gt['age'],[0,10,20,30,40,80]).value_counts().sort_index())
print('>=30yr MW',round(gt[gt.age>=30]['Nameplate Capacity (MW)'].sum()))
for s in ['Planned Retirement Year']:
    if s in gt: 
        p=gt[pd.to_numeric(gt[s],errors='coerce').between(2025,2032)]
        print('planned retire 2025-32 units',len(p),'MW',round(p['Nameplate Capacity (MW)'].sum()))
sz=pd.cut(gt['Nameplate Capacity (MW)'],[0,20,60,120,400])
print(gt.groupby(sz)['Nameplate Capacity (MW)'].agg(['count','sum']).round())
rt=[s for s in xl.sheet_names if 'Retired' in s][0]
r=pd.read_excel(f,sheet_name=rt,header=1)
r=r[(r['Prime Mover']=='GT')]
r=r[pd.to_numeric(r['Retirement Year'],errors='coerce')>=2015]
print('retired GT since 2015 units',len(r),'MW',round(r['Nameplate Capacity (MW)'].sum()))
print(r.groupby('Retirement Year')['Nameplate Capacity (MW)'].agg(['count','sum']).round())
