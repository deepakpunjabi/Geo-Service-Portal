from owslib.wms import WebMapService
import time
wms = WebMapService('http://demo.mapserver.org/cgi-bin/wms', version='1.1.1')
p1 = wms.identification.type
print(p1)
time.sleep(5)
