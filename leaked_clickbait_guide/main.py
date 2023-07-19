import random

def first(arg):
    if arg == None or arg == 'None':
        one_list = []
        with open("one.txt", 'r') as f:
            for line in f:
                one_list.append(line.strip())
        return random.choice(one_list)
    else:
        return arg

def second(arg):
    if arg == None or arg == 'None':
        two_list = []
        with open("two.txt", 'r') as f:
            for line in f:
                two_list.append(line.strip())
        return random.choice(two_list)
    else:
        return arg

def third(arg):
    if arg == None or arg == 'None':
         three_list = []
         with open("three.txt", 'r') as f:
             for line in f:
                 three_list.append(line.strip())
         return random.choice(three_list)
    else:
        return arg
def main():
    one = first('Using a knife to get') # Replace None with some word to make it always print out that word, just always put " between the word
    two = second('None') # Replace None with some word to make it always print out that word, just always put " between the word
    three = third('None') # Replace None with some word to make it always print out that word, just always put " between the word

    print(f"{one}\n{two}\n{three}")

main()

