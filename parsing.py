# Code for parsing the S-expression form of the machine files

def parse_machine(m: str):
    # strip newlines and commas for simpler parsing
    print(m)
    m = m.replace("\n", "").replace(",", " ")
    print(m)
    idx = m.find('(') ; print(idx)
    idx = m.find('(', idx+1) ; print(idx)
    idx = m.find('(', idx+1) ; print(idx)
    alpha_str = m[idx+1:m.find(')', idx)]
    new_alphastr = ''.join(alpha_str.replace(",", "").split(" "))
    print(new_alphastr)
    idx = m.find('(', idx+1)
    states = m[idx+1:m.find(")", idx)].split(" ")
    states = [s for s in states if s] # filter empty strings from list
    print(states)
    idx = m.find(')', idx+1)
    # idx = m.find(',', idx+1) # consume the comma before the next symbol
    initial = m[idx+1:m.find("(", idx)].strip()
    print(initial)
    idx = m.find("(", idx+1)
    final = m[idx+1:m.find(")", idx+1)]
    print(final)
    # Gonna have to do some looping for this part.






