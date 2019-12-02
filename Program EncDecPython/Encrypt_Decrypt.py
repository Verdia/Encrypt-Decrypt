#!/usr/bin/env python

from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
import zipfile

class Encryptor:
	def __init__(self, key):
		self.key=key

	def pad(self, s):
		return s+b"\0" * (AES.block_size - len(s) % AES.block_size)

	def encrypt(self, message, key, key_size = 512):
		message = self.pad(message)
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(key, AES.MODE_CBC, iv)
		return iv + cipher.encrypt(message)

	def encryptFile(self, filename):
		with open(filename, 'rb') as fo:
			plainttext = fo.read()
		enc = self.encrypt(plainttext, self.key)
		with open(filename + ".yey", 'wb') as fo:
			fo.write(enc)
		os.remove(filename)

	def decrypt(self,cipherText, key):
		iv = cipherText[:AES.block_size]
		cipher = AES.new(key, AES.MODE_CBC, iv)
		plainttext = cipher.decrypt(cipherText[AES.block_size:])
		return plainttext.rstrip(b"\0")

	def decryptFile(self, filename):
		with open(filename, 'rb') as fo:
			cipherText = fo.read()
		dec = self.decrypt(cipherText, self.key)
		with open(filename[:-4], 'wb') as fo:
			fo.write(dec)
		os.remove(filename)

	def getAllFiles(self):
		dir_path = os.path.dirname(os.path.realpath(__file__))
		dirs = []
		for dirName, subDirList, fileList in os.walk(dir_path):
			for fname in fileList:
				if (fname!='Encrypt_Decrypt.py' and fname!='data.txt.enc'):
					dirs.append(dirName+"\\"+fname)
		return dirs

	def encrypt_All(self):
		dirs = self.getAllFiles()
		for filename in dirs:
			self.encryptFile(filename)

	def decrypt_All(self):
		dirs = self.getAllFiles()
		for filename in dirs:
			self.decryptFile(filename)

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)

if os.path.isfile('password.txt.enc'):
	while(1):
		password = str(input("Masukkan Password: "))
		enc.decryptFile("password.txt.enc")
		p = ''
		with open("password.txt", "r") as f:
			p = f.readlines()
		if p[0] == password:
			enc.encryptFile("password.txt")
			break

	while(1):
		choice = int(input(
			"A. Press 1 to Encrypt.\nB. Press 2 to Decrypt.\nC. Press 3 to Encrypt All.\nD. Press 4 for Decrypt All.\nE. Press 5 to exit.\n"))
		if choice == 1:
			enc.encryptFile(str(input("Enter Filename to Encrypt : ")))
		elif choice == 2:
			enc.decryptFile(str(input("Enter Filename to Decrypt : ")))
		elif choice == 3:
			enc.encrypt_All()
		elif choice == 4:
			enc.decrypt_All()
		elif choice == 5:
			exit()
		else:
			print("Enter valid option")
else:
	while (1):
		password = str(input("Enter password for Decrypt : "))
		repassword = str(input("Confirm password : "))
		if password == repassword:
			break
		else:
			print("Wrong Password!")
	f = open("password.txt", "w+")
	f.write(password)
	f.close()
	enc.encryptFile("password.txt")
	print("Restart program for complete setup")
	time.sleep(1)
