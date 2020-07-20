import sys

if len(sys.argv) !=2:
    print(f"usage: python {sys.argv[0]} [fasta]")
    sys.exit()

f = sys.argv[1]
dic = {}
with open(f,'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        line.upper()
        for s in line.strip():
            if s in dic:
                dic[s] += 1
            else:
                dic[s] = 1

f= open('res.txt','w',encoding='utf-8')
f.write(f"A: {dic['A']}")
f.write(f"T: {dic['T']}")
f.write(f"G: {dic['G']}")
f.write(f"C: {dic['C']}")

f.close

     
total = 0
for k,v in dic.items():
    total +=v
with open('res.txt', 'a') as handle:
    handle.write(str(total))





