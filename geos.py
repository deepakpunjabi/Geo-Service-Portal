from owslib.wfs import WebFeatureService
wms = WebFeatureService('http://10.14.81.6:8080/iitkgp-geoservices/wfs', version='1.1.1')
for i in wms.contents:
    print(i)
