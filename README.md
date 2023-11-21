# solcx-select
cli wrapper for py-solc-x

Manages py-solc-x from unix command line a la solc-selector, uses symlinks from  ``$SOLC_PATH/solc`` to binaries installed by py-solc-x. Will read env variable ``SOLC_VERSION`` and set to version thereof without any other arguments. ``SOLC_VERSION=0.8.7 solcx-select`` 

