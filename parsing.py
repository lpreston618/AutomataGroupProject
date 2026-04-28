# Code for parsing the S-expression form of the machine files

def parse_machine(m: str):
    # strip newlines and commas for simpler parsing
    m.replace("\n", "").replace(",", "")
    idx = m.find('(')
    idx = m.find('(', idx)
    alpha_str = m[idx:m.find(')', idx)]


