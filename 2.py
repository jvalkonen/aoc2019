# Advent of Code - day 2

input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,2,13,23,27,2,27,13,31,2,31,10,35,1,6,35,39,1,5,39,43,1,10,43,47,1,5,47,51,1,13,51,55,2,55,9,59,1,6,59,63,1,13,63,67,1,6,67,71,1,71,10,75,2,13,75,79,1,5,79,83,2,83,6,87,1,6,87,91,1,91,13,95,1,95,13,99,2,99,13,103,1,103,5,107,2,107,10,111,1,5,111,115,1,2,115,119,1,119,6,0,99,2,0,14,0]


def int_code_interpreter(program):
    #print(program)
    i = 0
    while i < len(program):
        opcode = program[i]
        if opcode == 99:
            #print("Returning")
            return program

        a = program[program[i+1]]
        b = program[program[i+2]]
        output = program[i+3]

        #print(program[i:i+4])
        #print("Index: {} Opcode:{} a={} b={} output={}".format(i, opcode, a, b, output))

        if opcode == 1:
            #print("Add: {}+{}={} => saving to position {}".format(a, b, a+b, output))
            program[output]=a+b

        elif opcode == 2:
            #print("Multiply: {}*{}={} => saving to position {}".format(a, b, a*b, output))
            program[output]=a*b

        else:
            print("ERROR (Opcode:{})".format(opcode))

        i += 4
        #print(program)

#print(int_code_interpreter([1,9,10,3,2,3,11,0,99,30,40,50]))
#print(int_code_interpreter([1,0,0,0,99]))
#print(int_code_interpreter([2,3,0,3,99]))
#print(int_code_interpreter([2,4,4,5,99,0]))
#print(int_code_interpreter([1,1,1,4,99,5,6,0,99]))
expected = 19690720
for noun in range(0,99):
    for verb in range(0,99):
        prg = input[:]
        prg[1]=noun
        prg[2]=verb
        print("noun={} verb={}".format(noun, verb))
        print(prg)
        result = int_code_interpreter(prg)
        print("Noun={} verb={} results {}".format(noun, verb, result[0]))
        if expected == result[0]:
            print("Match found, exiting!")
            exit()
