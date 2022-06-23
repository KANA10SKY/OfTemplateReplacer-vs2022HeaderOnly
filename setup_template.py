import os
import shutil

if !os.path.exists('../../../scripts') or !os.path.exists('../../scripts/templates') or !os.path.exists('../vs'):
  print('put this folder \'vs-headeronly\' to the directory '\${OF_ROOT}/scripts/templates''.)

shutil.rmtree('../vs/')
shutil.copytree('./vs2022-headeronly', '../vs')
# os.remove('README.md')
# shutil.rmtree('.git/')
# os.remove
