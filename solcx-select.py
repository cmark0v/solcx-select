#!/usr/bin/python3
import solcx
from os import getenv
import sys
from dotenv import load_dotenv
from os import system
def setsolc(v):
    try:
        try:
            solcx.set_solc_version(v)
        except:
            solcx.install_solc(v)
            solcx.set_solc_version(v)
        o = system("ln -sf $HOME/.solcx/solc-v%s $HOME/.local/bin/solc" % (v,))
        if o == 0:
            print("version set to ", v, "symlink in .local/bin/solc")
    except Exception as e:
        print(e)
        print('using ',solcx.get_solc_version())

load_dotenv()
SOLC_VERSION = getenv("SOLC_VERSION", False)
if SOLC_VERSION:
    setsolc(SOLC_VERSION)


argvx = sys.argv[1::]

# print(solcx.__dir__())
if len(argvx) > 0:
    for j, l in enumerate(argvx):
        if l.lower() == "install":
            try:
                print("installing...")
                solcx.install_solc(argvx[j + 1])
            except Exception as e:
                print(e)
            break
        elif l.lower() == "show" or l.lower() == "version":
            print(solcx.get_solc_version())
            break
        elif l.lower() == "ls" or l.lower() == "versions" or l.lower() == "available":
            print(solcx.get_installed_solc_versions())
        elif l.lower() == "set" or l.lower() == "use":
            setsolc(argvx[j+1])
            break
        else:
            f = getattr(solcx, l.lower(), lambda x: print("what is ", l.lower()))
            if len(argvx) >= (j + 2):
                print(f(argvx[j + 1]))
            else:
                print(f([]))
else:
    print(solcx.get_solc_version())

