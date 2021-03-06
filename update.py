import urllib,urllib2,sys,platform,os,re
class bcolors:
	HEADER = '\033[95m'
	OKGREEN = '\033[92m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
ghc=open("githubcli","r")
code=ghc.read()
ghc.close()
ln=1
for line in code.splitlines():
	if ln==3:
		av=''.join(re.findall(r'#(.*?)#',line)).replace("v ","")
		break
	else:
		ln=ln+1
vl="https://raw.githubusercontent.com/Bytezz/GitHub-CLI/master/githubcli"
print "Connecting..."
try:
	urllib2.urlopen(vl)
	print "Success."
	site=urllib.urlopen(vl)
	page=site.read()
	ln=1
	for line in page.splitlines():
		if ln==3:
			line=line.replace("#","").replace("v ","")
			print "Actual version:",bcolors.BOLD+bcolors.OKGREEN+line+bcolors.ENDC
			if line==av:
				print "Your version:",bcolors.BOLD+bcolors.OKGREEN+av
				print "Your software is at the latest version."+bcolors.ENDC
			else:
				print "Your version:",bcolors.BOLD+bcolors.FAIL+av+bcolors.ENDC
				while True:
					up=raw_input("Update? [y or n]: ")
					if up.upper()=="Y" or up.upper()=="YES":
						if platform.system()=="Linux":
							try:
								print "Update..."
								os.system("git clone https://github.com/Bytezz/GitHub-CLI temp && cd temp/ && mv ../temp/* .. && rm -rf ../temp && make reinstall")
								print "(If reinstall not completed, type:)"
								print "sudo make reinstall"
								print "Completed."
							except:
								print "Git not installed."
								print "Go here for download:"
								print "https://github.com/Bytezz/GitHub-CLI"
							sys.exit()
						else:
							print "Go here for download:"
							print "https://github.com/Bytezz/GitHub-CLI"
							sys.exit()
					elif up.upper()=="N" or up.upper()=="NO":
						print "Don't update."
						sys.exit()
					else:
						print "Error. Retry."
		elif ln>3:
			break
		ln+=1
except urllib2.HTTPError, e:
	print "Error:"
	print(e.code)
except urllib2.URLError, e:
	print bcolors.FAIL+bcolors.BOLD+"Error:"+bcolors.ENDC
	print(e.args)
