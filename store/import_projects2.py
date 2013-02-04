"""
this script merges po files from their language directories (blocks, editor) in
translation projects.
It imports po files from 'django' directory and arranges them in a proper
directory tree for django.
It creates a list of language names (lang_list.txt).

--adlogi@media
"""

import os, os.path
import shutil

def importProject_editor():
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
					f1name = os.path.join(subpath, 'blocks.po')
					f2name = os.path.join(editorPath, dname, 'editor.po')
					print f1name
					print f2name
					uiHeader = '\n##################\n# User Interface #\n##################\n'
					content = open(f1name).read() + uiHeader + open(f2name).read()
					langCode = dname + '.po'
					open(os.path.join('scratch2', langCode),'wb').write(content)
					#shutil.copy2(fname, projectName)

def importProject_django():
	localeDir = 'locale'
	#if not os.path.exists(localeDir):
	#	os.makedirs(localeDir)
	djangoPath = os.path.join(os.getcwd(), '..', 'django')
	shutil.copytree(djangoPath, localeDir)
	dirList = os.listdir(localeDir)
	for dname in dirList:
		subpath = os.path.join(localeDir, dname)
		if os.path.isdir(subpath):
			os.makedirs(os.path.join(subpath, 'LC_MESSAGES'))
			#print dname
			for fname in os.listdir(subpath):
				if fname.endswith(".po"):
					f1name = os.path.join(subpath, fname)
					shutil.move(f1name, os.path.join(subpath, 'LC_MESSAGES'))

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