"""
this script copies .po files from their prospective language directories in
translation projects, and creates a list of language names (lang_list.txt).
Merge the blocks and editor files into one.

--adlogi@media
"""

import os, os.path
import shutil

def importProject():
	if not os.path.exists('scratch2'):
		os.makedirs('scratch2')
	blocksPath = os.path.join(os.getcwd(), '..', 'blocks')
	editorPath = os.path.join(os.getcwd(), '..', 'editor')
	dirList = os.listdir(blocksPath)
	print blocksPath
	for dname in dirList:
		subpath = os.path.join(blocksPath, dname)
		if os.path.isdir(subpath):
			print dname
			for fname in os.listdir(subpath):
				if fname.endswith(".po"):
					f1name = os.path.join(subpath, fname)
					f2name = os.path.join(editorPath, dname, fname)
					print f1name
					print f2name
					content = open(f1name).read() + '\n#User Interface\n' + open(f2name).read()
					open(os.path.join('scratch2', fname),'wb').write(content)
					#shutil.copy2(fname, projectName)

def generateLanguagesList():
	print 'Generating language list'
	path = 'blocks'
	fout = open('lang_list.txt', 'w')
	for fname in os.listdir(path):
		if fname.endswith(".po"):
			fout.write(fname[:len(fname) - 3] + ',')
			fin = open(os.path.join(path, fname), 'r')
			stage = 0
			for line in fin:
				if 'msgid "Language-Name"' in line:
					stage = 1
				elif 'msgstr' in line and stage == 1:
					fout.write(line[line.find('"') + 1:line.rfind('"')] + '\n')
					break


importProject()
#generateLanguagesList()