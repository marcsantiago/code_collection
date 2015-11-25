import urllib
import os

company_symbol = ["ACGL", "AFSI", "AGII", "AGNC", "ANAT", "ARCP", "ASBC", "ASPS", "BANF", "BBCN", "BGCP", "BNCL", "BOKF", "BPOP", "BRKL", "CACC", "CATY", "CBOE", "CBSH", "CFFN", "CHFC", "CINF", "CME ", "COLB", "CVBF", "ERIE", "ESGR", "ETFC", "EWBC", "EZPW", "FCFS", "FCNC", "FFBC", "FFIN", "FITB", "FMBI", "FMER", "FNFG", "FNGN", "FSRV", "FULT", "GBCI", "GLPI", "GLRE", "HBAN", "HBHC", "HLSS", "HOMB", "IBKC", "IBKR", "IBOC", "IPCC", "ISBC", "KRNY", "LPLA", "MBFI", "MHLD", "MKTX", "MTGE", "NAVG", "NBTB", "NDAQ", "NFBK", "NPBC", "NTRS", "NWBI", "ORIT", "OZRK", "PACW", "PBCT", "PCH ", "PNFP", "PRAA", "PVTB", "ROIC", "SAFT", "SBNY", "SBRA", "SCBT", "SEIC", "SIGI", "SIVB", "SLM ", "STFC", "SUSQ", "TCBI", "TFSL", "TRMK", "TROW", "UBSI", "UMBF", "UMPQ", "VRTS", "WABC", "WAFD", "WETF", "WRLD", "WTFC", "Z", "ZION"]

for company in company_symbol:
    url = 'http://finance.google.com/finance/info?client=ig&q={0}:{1}'.format(company, 'NASDAQ')
    nasdaq = urllib.urlopen(url)
    text = nasdaq.read()
    filename = 'nasdaq.txt'.format(company)
    with file(filename, 'a') as output:
        output.write(str(text))


with file('nasdaq.txt') as cleandata:
    clean = cleandata.read()
    clean = clean.rstrip().strip().replace('"', '').replace('/', "").replace('{', '').replace(',', '')\
        .replace('}', '').replace('[', '').replace(']', '')

with file('nasdaq_summary.txt', 'w') as c:
    c.write(clean)

os.remove('nasdaq.txt')

'''
list = []
with file('names.txt', 'r') as names:
    text = names.read().split('\n')
    for i in text:
        list.append(i[:4])

newlist = ', '.join('"{0}"'.format(w) for w in list).replace('\t', '')
print newlist
'''
