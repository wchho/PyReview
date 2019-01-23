# Ex13: fibonacci generator

def get_num(default = "Enter a fibonacci sequence length: "):
    return int(input(default))

def fib_gen(seqLen):
    MySeq = list(range(1,2))
    while len(MySeq) < seqLen:
        if len(MySeq) == 1:
            MySeq.append(1) # only for 2nd item in Fib sequence (1)

        else: # main code
            nextNum = MySeq[-1] + MySeq[-2]
            MySeq.append(nextNum)

    return MySeq

seq_length = get_num()
seq = fib_gen(seq_length)
print(f"Your fibonacci sequence is :\n{seq}")
