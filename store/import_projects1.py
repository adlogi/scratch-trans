"""
this script copies .po files from their prospective language directories in
translation projects, and creates a list of language names (lang_list.txt)

--adlogi@media
"""

import os, os.path
import shutil

def importProject(projectName):
	print 'Importing files from ' + projectName
	if not os.path.exists(projectName):
		os.makedirs(projectName)
	projectPath = os.path.join(os.getcwd(), '..', projectName)
	dirList = os.listdir(projectPath)
	print projectPath
	for dname in dirList:
		subpath = os.path.join(projectPath, dname)
		if os.path.isdir(subpath):
			print dname
			for fname in os.listdir(subpath):
				if fname.endswith(".po"):
					fname = os.path.join(subpath, fname)
					print fname
					shutil.copy2(fname, projectName)

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


importProject('blocks')
importProject('editor')
#generateLanguagesList()