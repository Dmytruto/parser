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
amount = len(illnesses)
i = 0
while i < amount:
    fileName = 'text' + str(i) + '.txt'
    f = open(fileName, 'w')
    f.write(allSymthoms[i] + '\n')
    f.write(str(len(illnesses[i])) + '\n')
    for x in illnesses[i]:
        f.write(x + '\n')
    f.close()
    i = i + 1
