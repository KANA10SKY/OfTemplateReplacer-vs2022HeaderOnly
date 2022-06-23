import os
import shutil

dir_scripts = '../../scripts'
dir_templates = dir_scripts+'/templates'
dir_vs = dir_templates+'/vs'

if not os.path.exists(dir_scripts) or not os.path.exists(dir_templates) or not os.path.exists(dir_vs):
  print('put this folder \'vs-headeronly\' to the directory \'${OF_ROOT}/other\'.')
  exit(1)
  

#if os.path.exists(dir_vs):
shutil.rmtree(dir_vs)
shutil.copytree('./vs2022-headeronly', dir_vs)
# os.remove('README.md')
# shutil.rmtree('.git/')
# os.remove

print('Completed replacing template \'vs\'.')
exit(0)
