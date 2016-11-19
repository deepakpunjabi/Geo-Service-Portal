from owslib.wms import WebMapService

wms = WebMapService('http://10.14.81.6:8080/iitkgp-geoservices/wms', version='1.1.1')

print("Service Metadata ---> "+wms.identification.type)
print()
print("Title ---> "+wms.identification.title)
print()
print('List of available layers --->')
for i in list(wms.contents):
    print(i)
print()

print("Available operations --->")
for op in wms.operations:
    print(op.name)
print()

print('Format Options --->')
for i in wms.getOperationByName('GetMap').formatOptions:
    print(i)
print()

print('------------- Details about particular layer: POPULATION -------------')

print('Title ---> '+wms['kgp:POPULATION'].title)
print('Name ---> '+wms['kgp:POPULATION'].name)
print('Is Queryable ---> '+str(wms['kgp:POPULATION'].queryable))
print('Is Opaque ---> '+str(wms['kgp:POPULATION'].opaque))

print('Bounding Box ---> ')
print('minx ---> '+str(wms['kgp:POPULATION'].boundingBox[0]))
print('miny ---> '+str(wms['kgp:POPULATION'].boundingBox[1]))
print('maxx ---> '+str(wms['kgp:POPULATION'].boundingBox[2]))
print('maxy ---> '+str(wms['kgp:POPULATION'].boundingBox[3]))
print()

print('styles ---> ')
for i in wms['kgp:POPULATION'].styles:
    print(i)
print()

print('crs options ---> ')
for i in wms['kgp:POPULATION'].crsOptions:
    print(i)
print()

img = wms.getmap(layers=['kgp:POPULATION'],
                 styles=['kgp:Population'],
                 srs='EPSG:4326',
                 bbox=(68, 8, 97, 35),
                 size=(500, 450),
                 format='image/jpeg',
                 transparent=True
                 )
out = open('jpl_mosaic_visb.jpg', 'wb')
out.write(img.read())
out.close()