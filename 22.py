import sys

# string substitution
def comp(seq: str)->str:
    comp = ''
    for s in seq:
        if s=='A':
            comp += 'T'
        elif s == 'T':
            comp += 'A'
        elif s == 'G':
            comp += 'C'
        elif s == 'C':
            comp +='G'
    return comp

# dictionary
def comp2(seq: str)->str:
    d_comp = {'A':'T','G':'C','C':'G','T':'A'}
    comp=''
    for s in seq:
        comp += d_comp[s]
    return comp

# if file is accessed, run below code
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'#usage: python{sys.argv[0]} [string]')
        sys.exit()
    seq = sys.argv[1]
    res = comp(seq)
    print(res)
