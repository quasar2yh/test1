import sys

if len(sys.argv) != 2:
    print(f"#usage : python {sys.argv[0]} [num]")
    sys.exit()

# multiple try is possible
# if you don't write sys.exit(), error will arise
try:
    num = int(sys.argv[1])
    print(10/num)
except ValueError:
    print('input not valid')
    sys.exit()
except ZeroDivisionError:
    print('0 cannot divide')
    sys.exit()

