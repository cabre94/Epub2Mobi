"""
File: epub2mobi.py
Author: Facundo Martin Cabrera
Email: cabre94@hotmail.com
GitLab: https://github.com/cabre94
Description:
    Script para convertir libros .epub a .mobi. Es para Linux y hay que tener instalado Calibre
"""
import os

path = os.getcwd()

# Crea el directorio para guardar
save_path = os.path.join(path, 'MOBI')

# Carpetas
folders = os.listdir(path)

if not os.path.exists(save_path):
	os.makedirs(save_path)

for f in folders:
	if os.path.isdir(f):
		f_save = os.path.join(save_path, f)
		if not os.path.exists(f_save):
			os.makedirs(f_save)

		books = os.listdir(os.path.join(path, f))
		for b in books:
			mobi = b.replace('epub', 'mobi')
			if not os.path.exists(os.path.join(save_path, f, mobi)):
				os.system('ebook-convert ' + os.path.join(path, f, b) + ' ' + os.path.join(save_path, f, mobi))
			print("\nSe convirtio {}\n".format(mobi))
