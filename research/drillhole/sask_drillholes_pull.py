import json,urllib.request,urllib.parse,sys
base="https://gis.saskatchewan.ca/arcgis/rest/services/Economy/Mineral_Exploration/MapServer/3/query"
flds="OBJECTID,COMPANY,DATE_DRILLED,TOTAL_DH_LENGTH_M,WEDGE_HOLE,BASE_OF_ATHABASCA_SG_DEPTH_M,TOP_CRYSTALLINE_BSMT_DEPTH_M,COMMODITY_OF_INTEREST,COREAVAILABILITY,STORAGE_LOCATIONS,DISPOSITION,EASTING_UTM,NORTHING_UTM"
out=[];off=0
while True:
    q=urllib.parse.urlencode({"where":"1=1","outFields":flds,"returnGeometry":"false","f":"json","resultOffset":off,"resultRecordCount":1000,"orderByFields":"OBJECTID"})
    d=json.load(urllib.request.urlopen(base+"?"+q,timeout=120))
    fs=d.get("features",[])
    out+= [f["attributes"] for f in fs]
    if not fs or not d.get("exceededTransferLimit") and len(fs)<1000: break
    off+=len(fs)
json.dump(out,open(sys.argv[1],"w"));print(len(out))
