# ФИНМЕНЕДЖЕР: GUI-ОБОЛОЧКА

import sys

sys.path.append('./G0')
sys.path.append('./G1')
sys.path.append('./G2')
sys.path.append('./G3')

sys.path.append('./L0')
sys.path.append('./L1')
sys.path.append('./L2')
sys.path.append('./L3')
sys.path.append('./L4')
sys.path.append('./L5')
sys.path.append('./L6')
sys.path.append('./L7')
sys.path.append('./L8')
sys.path.append('./L9')

sys.path.append('./ui/form_accounts')
sys.path.append('./ui/form_analytics')
sys.path.append('./ui/form_backups')
sys.path.append('./ui/form_export')
sys.path.append('./ui/form_import')
sys.path.append('./ui/form_main')
sys.path.append('./ui/form_operations')
sys.path.append('./ui/form_processing')


from L90_application import C90_Application

app_finmanager = C90_Application()
app_finmanager.Start()
