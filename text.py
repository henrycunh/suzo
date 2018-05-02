from colorama import Fore, Back, Style
LINE_LEN = 38

def line():
    print(f'\t{"─" * LINE_LEN}')

def inTxt(message):
    line()
    print(f"\t  {message}")
    print( '\t  > ', end='', flush=1)
    
def centeredTxt(line1, line2 = None): #eu faço xixi nas pessoas
    
    tl1 = len(line1) # Comprimento do texto
    tl2 = len(line2) if line2 is not None else 0# Comprimento do texto
    line()
    print(f"\t{' ' * ((LINE_LEN - tl1) // 2)}{line1}{' ' * ((LINE_LEN - tl1) // 2)}")
    if tl2:
        print(f"\t{' ' * ((LINE_LEN - tl2) // 2)}{line2}{' ' * ((LINE_LEN - tl2) // 2)}")
    line()
header = """
{0}
\t   ██████  █    ██ ▒███████▒ ▒█████  
\t ▒██    ▒  ██  ▓██▒▒ ▒ ▒ ▄▀░▒██▒  ██▒
\t ░ ▓██▄   ▓██  ▒██░░ ▒ ▄▀▒░ ▒██░  ██▒
\t   ▒   ██▒▓▓█  ░██░  ▄▀▒   ░▒██   ██░
\t ▒██████▒▒▒▒█████▓ ▒███████▒░ ████▓▒░
\t ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▒▒ ▓░▒░▒░ ▒░▒░▒░ 
\t ░ ░▒  ░ ░░░▒░ ░ ░ ░░▒ ▒ ░ ▒  ░ ▒ ▒░ 
\t ░  ░  ░   ░░░ ░ ░ ░ ░ ░ ░ ░░ ░ ░ ▒  
\t       ░     ░       ░ ░        ░ ░  
\t                   ░                 
{1}
\t┌────────┬───────────────────────────┐
\t│ {0}author {1}│ henrique cunha            │
\t│ {0}github {1}│ @muztake                  │
\t│ {0}repo   {1}│ /suzo                     │
\t│ {0}email  {1}│ henrycunh@gmail.com       │
\t├────────┴─────────────────────  ⌠  ─┤
\t│     {0} made with love @ ufscar {1}  ⌡   │
\t└────────────────────────────────────┘
""".format(Fore.RED, Fore.RESET)