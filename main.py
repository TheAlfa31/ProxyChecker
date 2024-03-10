import os, sys, time
import requests
import json
from colorama import Fore, Back, Style, init

def kayan_yazi(icerik):
    for karakter in icerik:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(0.1)
            
init()

red=Fore.RED
green=Fore.GREEN
yellow=Fore.YELLOW

backred=Back.RED
backgreen=Back.GREEN

reset=Style.RESET_ALL

tic=f"{yellow}[{green}✓{yellow}]{reset}"
carpi=f"{yellow}[{red} ! {yellow}]{reset}"
inputt=f"{green}[{yellow}*{green}] - {reset}"


set_surum="v1.0"

url = "http://ip-api.com/json/"

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()
kayan_yazi(f"\n{inputt} {yellow}Please wait, the version is being checked and messages are being fetched...\n")  

qw=requests.get("https://raw.githubusercontent.com/TheAlfa31/DevilProjects/main/check.json")
a=json.loads(qw.text)

yu=a["active"]
yuuu=a["sürüm"]

if yu=="True":
    pass
if yu=="False":
    kayan_yazi(f"{carpi} - I had to close it for a specific reason, stay tuned.")





if yuuu==set_surum:
    kayan_yazi(f"{tic} - {green}The version is up to date, good use.{reset}")
    time.sleep(3)
if yuuu!=set_surum:
    kayan_yazi(f"{carpi} - {red}The version is not up to date, the new version is on github.{reset}")
    time.sleep(5)


clear_terminal()

banner=f"""
{red}
⠀⢀⡀⠀⠀⣿⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀{green}Socks4 & socks5 Proxy Checker{reset}{red}
⠀⣾⡇⠀⢸⣿⡇⠀⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀{green}Dev: TC ALFA - https://t.me/officialalfa{reset}{red}
⣰⣿⡇⠀⠺⣿⠇⠀⢿⣿⡀⠀⠀⠀⠀⠀⠀ {green}Version: v1.0{reset}{red}
⢻⣿⡅⠀⢀⣿⡄⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⡇⠀⢸⣿⡇⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠻⣿⣷⣾⣿⣷⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⣹⣿⡏⠉⠀⠀⢀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⡇⠀⠀⠀⢸⣧⣄⣤⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣿⣿⣿⡇⠀⠀⠀⣸⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⣿⣿⣿⡇⠀⠀⣼⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⣿⣿⣿⣇⣀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡗⢿⣿⣿⣿⣿⣿⣿⡟⠁⠙⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠉⠙⣿⣿⣿⣿⠁⠀⠀⠘⣿⣷⡀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⢻⣿⣿⣿⣶⣶⠿⠟⠛⠛⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⢸⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣼⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⡀⠀⠀⠀⠀⠀
⠀⠀⢿⣿⣿⣿⡏⠉⠁⠀⠀⣿⣿⣿⣿⠋⠉⠛⣿⡆⠀⠀⠀⠀
⠀⠀⠈⢿⣿⣿⡇⠀⠀⠀⠀⢿⣿⣿⣿⡄⠀⣸⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠈⢿⣿⡇⠀⠀⠀⠀⠸⣿⣿⣿⣧⠀⠻⣷⣦⣶⡀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⢻⣿⣿⡟⠀⠀⠀⣿⣿⣷⣄⠀
⠀⠀⠀⠀⢸⣿⣿⣷⡀⠀⠀⠀⠀⣿⣿⣧⠀⠀⠀⠀⠀⠀⠉⠓
⠀⠀⠀⠀⢸⣿⣿⣿⣿⡀⠀⠀⠀⠸⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣇⣿⡇⠑⠀⠀⠀⠀⢹⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡿⠋⠀⠀⠀⠀⠀⠀⢸⣿⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⢰⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⢀⣴⡿⠉⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠉⠉⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀
{reset}
"""
suc = 0
nott = 0
alfa=[""]
tc=[""]
print(banner)

def main(url, proxy, port, ip, type):
    global results
    global suc
    global nott
    
    try:
        #os.system("cls")
        response = requests.get(url, proxies=proxy, verify=False)
        a = json.loads(response.text)

        if response.status_code == 200:
            success = True
            response_code = "200"
            
                #a.write(port,"\n")
        elif response.status_code == 400:
            success = False
            response_code = "400"
            
        message = f"{tic} {green}This proxy alive, has been saved!{reset}"
        ip = a["query"]
        country = a["country"]
        countryCode = a["countryCode"]
        region = a["region"]
        regionName = a["regionName"]
        zip_code = a["zip"]
        lat = a["lat"]
        lon = a["lon"]
        if proxy not in alfa:
            suc+=1
            alfa.append(proxy)
            with open("verified.txt", "a") as e:
                e.write("\n")
                e.write(a["query"])
                e.write(":")
                e.write(port)
        if success == True:
            results=f"\n{yellow}Succes: {green}{success}{reset}\nmessage:{message}\nİp Adress: {ip} \nCountry: {country} \nCountry code: {countryCode} \nRegion: {region} \nRegion name: {regionName}\nZip code: {zip_code}\nLat: {lat}\nLon: {lon}"
                    
    except requests.exceptions.ConnectionError:
        if proxy not in tc:
            nott+=1
            tc.append(proxy)
        success = f"{red}False{reset}"
        message=f"{carpi} {red}Could not connect, not save!{reset}"
        ip = 0
        port = 0
        country = 0
        countryCode = 0
        region = 0
        regionName = 0
        zip_code = 0
        lat = 0
        lon = 0        
        results=f"\n{yellow}Succes: {red}{success}{reset}\nmessage:{message}\nİp Adress: {ip} \nCountry: {country} \nCountry code: {countryCode} \nRegion: {region} \nRegion name: {regionName}\nZip code: {zip_code}\nLat: {lat}\nLon: {lon}"
            
    bannr=f"""{red}
    
⠀⢀⡀⠀⠀⣿⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⡇⠀⢸⣿⡇⠀⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀          {green}_-TC ALFA-_{red}
⣰⣿⡇⠀⠺⣿⠇⠀⢿⣿⡀⠀⠀⠀⠀⠀⠀  
⢻⣿⡅⠀⢀⣿⡄⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⡇⠀⢸⣿⡇⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{yellow}Success: {green}{success}{red}
⠀⠻⣿⣷⣾⣿⣷⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{yellow}Message: {green}{message}{red}
⠀⠀⠈⠉⣹⣿⡏⠉⠀⠀⢀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀{yellow}Type: {green}{type}{red}
⠀⠀⠀⣼⣿⣿⡇⠀⠀⠀⢸⣧⣄⣤⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀{yellow}İp Address: {green}{ip}{red}
⠀⠀⢰⣿⣿⣿⡇⠀⠀⠀⣸⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀{yellow}Port: {green}{port}{red}
⠀⠀⣼⣿⣿⣿⡇⠀⠀⣼⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀{yellow}Number of verified: {backgreen}{suc}{reset}{red}
⠀⠀⢿⣿⣿⣿⣇⣀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀{yellow}Number of unconnected: {backred}{nott}{reset}{red}
⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡗⢿⣿⣿⣿⣿⣿⣿⡟⠁⠙⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠉⠙⣿⣿⣿⣿⠁⠀⠀⠘⣿⣷⡀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⢻⣿⣿⣿⣶⣶⠿⠟⠛⠛⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⢸⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣼⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⡀⠀⠀⠀⠀⠀
⠀⠀⢿⣿⣿⣿⡏⠉⠁⠀⠀⣿⣿⣿⣿⠋⠉⠛⣿⡆⠀⠀⠀⠀
⠀⠀⠈⢿⣿⣿⡇⠀⠀⠀⠀⢿⣿⣿⣿⡄⠀⣸⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠈⢿⣿⡇⠀⠀⠀⠀⠸⣿⣿⣿⣧⠀⠻⣷⣦⣶⡀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⢻⣿⣿⡟⠀⠀⠀⣿⣿⣷⣄⠀
⠀⠀⠀⠀⢸⣿⣿⣷⡀⠀⠀⠀⠀⣿⣿⣧⠀⠀⠀⠀⠀⠀⠉⠓
⠀⠀⠀⠀⢸⣿⣿⣿⣿⡀⠀⠀⠀⠸⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣇⣿⡇⠑⠀⠀⠀⠀⢹⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡿⠋⠀⠀⠀⠀⠀⠀⢸⣿⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⢰⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⢀⣴⡿⠉⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠉⠉⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀
    """               
    clear_terminal()
    print(bannr)
    return results





if __name__ == "__main__":
    set_type=input(f"{inputt}Enter type(Example: socks4 or socks5): ")

    if set_type == "socks4":
        type="socks4"
    if set_type == "socks5":
        type="socks5"


    with open("proxy.txt") as f:
        line = f.readline()
        while line:
            ip, port = line.strip().split(":")
            proxies = {"http": f"{type}://{ip}:{port}", "https": f"{type}://{ip}:{port}"}
            result = main(url, proxies, port, ip, type)
            line = f.readline()







