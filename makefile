pre=/usr/local/bin/

install:
	mkdir -p $(pre)
	cp githubcli $(pre)githubcli
	chmod +x $(pre)githubcli

uninstall:
	rm $(pre)githubcli

reinstall:
	rm $(pre)githubcli
	cp githubcli $(pre)githubcli
	chmod +x $(pre)githubcli
