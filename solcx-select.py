#!/usr/bin/python3
import types
import solcx
from os import getenv
import sys
from dotenv import load_dotenv
from os import system

load_dotenv()
SOLC_VERSION = getenv("SOLC_VERSION", False)
SOLC_PATH = getenv("SOLC_PATH", getenv("HOME", "~") + "/.local/bin")


def setsolc(v):
    try:
        solcx.set_solc_version(v)
        path = solcx.get_solcx_install_folder()
        o = system("ln -sf %s/solc-v%s %s/solc" % (path, v, SOLC_PATH))
        if o == 0:
            print("version set to ", v, "symlink in %s/solc" % (SOLC_PATH,))
        else:
            print("symlink %s/solc failed with nonzero exit status" % (SOLC_PATH,))
    except Exception as e:
        print(e)
        print("using ", solcx.get_solc_version())


if SOLC_VERSION:
    setsolc(SOLC_VERSION)


argvx = sys.argv[1::]
alias_install = ["install", "add"]
alias_v = ["show", "version", "get"]
alias_ls = ["ls", "versions", "installed"]
alias_set = ["set", "use"]
alias_get_solcx_path = ["path", "solcx_path"]
alias_ls_installable = ["bin", "installable", "lsbin", "available"]
alias_solc_path = ["link","solc_path"]

funz = [
    "compile_solc",
    "get_compilable_solc_versions",
    "get_installable_solc_versions",
    "get_installed_solc_versions",
    "get_solc_version",
    "get_solcx_install_folder",
    "import_installed_solc",
    "install_solc",
    "install_solc_pragma",
    "set_solc_version",
    "set_solc_version_pragma",
]


def help():
    print("solcx-select [cmd] [arg]", "\n")
    print(
        "solcx-select adds version of solc selected by solcx to your shell path", "\n"
    )
    print(
        "if SOLC_VERSION is set, it will link to this version before processing other args",
        "\n",
    )

    print(str(alias_install), " - installs version(s) supplied", "\n")
    print(str(alias_v), " - display current version", "\n")
    print(str(alias_ls), " - show versions installed/available", "\n")
    print(str(alias_set), "  - set version", "\n")
    print(str(alias_get_solcx_path), "  - get path to solcx binaries", "\n")
    print(str(alias_ls_installable), "  - list versuions available to install", "\n")
    print(str(alias_solc_path), "  - path to solc symlink, set by env var SOLC_PATH defaulting to ~/.local/bin", "\n")
    
    print("others: ", funz, "\n")


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
        for ve in solcx.get_installed_solc_versions():
            print(str(ve))
    elif cmd in alias_ls_installable:
        for ve in solcx.get_installable_solc_versions():
            print(str(ve))
    elif cmd in alias_set:
        setsolc(argvx[1])
    elif cmd in alias_get_solcx_path:
        print(str(solcx.get_solcx_install_folder()))
    elif cmd in alias_solc_path:
        print(SOLC_PATH)
    elif cmd in funz:
        f = getattr(solcx, cmd, lambda x: "what is %s" % (cmd,))
        if len(argvx) >= 2:
            print(f(argvx[1]))
        else:
            print(f([]))
    else:
        help()
else:
    help()
    print(solcx.get_solc_version())
