# solcx-select
cli wrapper for py-solc-x

unix systems only. WSL and mac should be okay. 

Manages py-solc-x from unix command line a la solc-selector, uses symlinks from  ``$SOLC_PATH/solc`` to binaries installed by py-solc-x. Will read env variable ``SOLC_VERSION`` and set to version thereof without any other arguments. ``SOLC_VERSION=0.8.7 solcx-select`` 

Will read pragma from solidity file and install/set a compliant version: ``solcx-select for contract.sol``


