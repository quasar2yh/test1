import sys
import gzip

if len(sys.argv) != 2:
    print(f"usage : python {sys.argv[0]} [fasta.gz]")
    sys.exit()

f = sys.argv[1]

dic = {}
tot=0

with gzip.open(f,'rb') as handle:
    for line in handle:
        line = line.decode("utf-8").strip()
        if line.startswith('>'):
            continue
        for i in line:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] =1
                
            tot+=1                 
print(dic)
print(f'total base:{tot}')

with open('result0721.txt','w') as handle:
    handle.write(f'A : {dic["A"]}\n')
    handle.write(f'T : {dic["T"]}\n')
    handle.write(f'G : {dic["G"]}\n')
    handle.write(f'C : {dic["C"]}\n')
