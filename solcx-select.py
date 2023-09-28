#!/usr/bin/python3
import solcx
from os import getenv
import sys
from dotenv import load_dotenv
from os import system

load_dotenv()
SOLC_VERSION = getenv("SOLC_VERSION", False)
SOLC_VERSION = getenv("SOLC_VERSION", False)


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
        print("using ", solcx.get_solc_version())


if SOLC_VERSION:
    setsolc(SOLC_VERSION)


argvx = sys.argv[1::]
alias_install = ["install", "add"]
alias_v = ["show", "version", "get"]
alias_ls = ["ls", "versions", "available"]
alias_set = ["set", "use"]

afunz = dir(solcx)
funz = []
for f in funz:
    if type(getattr(solcx, f)) == function:
        funz.append(f)


def help():
    print("solcx-select [cmd] [arg]", "\n")
    print(
        "solcx-select adds version of solc selected by solcx to your shell path", "\n"
    )
    print(
        "if no args provided, it will link to version declared by env var SOLC_VERSION",
        "\n",
    )

    print(str(alias_install, " - installs version","\n"))
    print(str(alias_v, " - display current version [default] ","\n"))
    print(str(alias_ls, " - show versions available","\n"))
    print(str(alias_set, "  - set version","\n"))
    print("others: ",funz,"\n")

if len(argvx) > 0:
    cmd = argvx[0].lower()
    if cmd in alias_install:
        try:
            print("installing...")
            for a in argvx[1::]:
                solcx.install_solc(a)
                print("installed ", a)
        except Exception as e:
            print(e)
    elif cmd in alias_v:
        print(solcx.get_solc_version())
    elif cmd in alias_ls:
        print(solcx.get_installed_solc_versions())
    elif cmd in alias_set:
        setsolc(argvx[2])
    elif cmd in afunz:
        f = getattr(solcx, cmd, lambda x: "what is %s" % (cmd,))
        if len(argvx) >= 2:
            print(f(argvx[2]))
        else:
            print(f([]))
    else:
        help()
else:
    help()
    print(solcx.get_solc_version())
