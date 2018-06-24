import textwrap 

def marqueeprint(text):
    print('{:=^70}'.format(text.upper()))


# Left-justify print
def leftprint(text):
    print('{:<70}'.format(text))


# right-justify print
def rightprint(text):
    print('{:>70}'.format(text))


# centered print
def centerprint(text):
    wrapstring = textwrap.wrap(text, width=70)
    for line in wrapstring:
        # print(line)
        print('{:^70}'.format(line))


def lr_justify(left, right, width):
    return '{}{}{}'.format(left, ' ' * (width - len(left + right)), right)
