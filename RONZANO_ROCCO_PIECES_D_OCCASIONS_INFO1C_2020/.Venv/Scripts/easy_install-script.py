#!"C:\Users\rocco\Google�Drive (rocco.ronzano@epfl.ch)\HOMEWORK\EPSIC\1�re ann�e\ICT-104 - Impl�menter un mod�le de donn�es\RONZANO_ROCCO_PIECES_D_OCCASIONS_INFO1C_2020\.Venv\Scripts\python.exe" -x
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==40.8.0','console_scripts','easy_install'
__requires__ = 'setuptools==40.8.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('setuptools==40.8.0', 'console_scripts', 'easy_install')()
    )
