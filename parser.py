import requests
import re
response = requests.get('http://healthtools.aarp.org/symptomsearch')
try:
    doc = response.content.decode('utf-8',errors ='ignore')
except:
    doc = response.content.decode('cp1251', errors='ignore')
doc=doc.replace('\n','')
doc=doc.replace('\t','')
doc=doc.replace('  ','')
allSymthoms = []
allUrls = []
illnesses = []
columns = re.findall('<td width="33%">(.+?)</td>',doc)
for x in columns:
    sympthoms = re.findall('">(.+?)</a>',x)
    urls = re.findall('<a href="(.+?)"',x)
    allSymthoms.extend(sympthoms)
    allUrls.extend(urls)
for x in allUrls:
    response = requests.get('http://healthtools.aarp.org' + x)
    try:
        doc = response.content.decode('utf-8',errors ='ignore')
    except:
        doc = response.content.decode('cp1251', errors='ignore')
    illness = re.findall('title="Click to view article">(.+?)</a>',doc)
    illnesses.append(illness)
