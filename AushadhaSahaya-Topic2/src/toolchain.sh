#!/bin/sh
# CP toolchain / environment capture for 1BCP308 Topic 2
echo "== CP toolchain / environment capture =="
echo "$ python3 --version"
python3 --version
echo "$ python3 -c \"import sys; print(sys.executable)\""
python3 -c "import sys; print(sys.executable)"
echo "$ python3 -c \"import numpy; print(numpy.__version__)\""
python3 -c "import numpy; print(numpy.__version__)"
echo "$ python3 -c \"import pandas; print(pandas.__version__)\""
python3 -c "import pandas; print(pandas.__version__)"
echo "$ uname -srm"
uname -srm
echo "RESULT: toolchain captured -- PASS"
