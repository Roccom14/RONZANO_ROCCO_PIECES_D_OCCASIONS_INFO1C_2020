#!"C:\Users\rocco\Google�Drive (rocco.ronzano@epfl.ch)\HOMEWORK\EPSIC\1�re ann�e\ICT-104 - Impl�menter un mod�le de donn�es\RONZANO_ROCCO_PIECES_D_OCCASIONS_INFO1C_2020\.Venv\Scripts\python.exe" -x
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==19.0.3','console_scripts','pip3.8'
__requires__ = 'pip==19.0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==19.0.3', 'console_scripts', 'pip3.8')()
    )
