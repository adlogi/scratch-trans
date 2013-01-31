import os, os.path

path = os.getcwd()
dirList=os.listdir(path)
for dirname in dirList:
	if os.path.isdir(dirname):
		fileList = os.listdir(os.path.join(path, dirname))
		for filename in fileList:
			if filename.endswith("blocks.po"):
				print filename
				#os.remove(os.path.join(path, dirname, filename))
				os.rename(os.path.join(path, dirname, filename), os.path.join(path, dirname, "editor.po"))
