import os

def create_shelly_script():
    # Sadržaj shelly.sh fajla
    shelly_script_content = '''#!/bin/bash

# Promeni prompt na ~shelly
echo "running..."
sleep 4
cd bin
cd usr
cd home
clear
export PS1="~shelly$ "

# Pokreni interaktivni shell
bash --noprofile --norc
'''

    # Putanja do shelly.sh fajla
    shelly_file_path = './shelly.sh'

    # Kreiranje shelly.sh fajla
    with open(shelly_file_path, 'w') as file:
        file.write(shelly_script_content)

    # Postavljanje fajla kao izvršan
    os.chmod(shelly_file_path, 0o755)

    print(f'Fajl {shelly_file_path} je uspešno kreiran i postavljen kao izvršan.')
    print(f'Za pokretanje OS-a, pokrenite komandu: ./shelly.sh')

def main():
    print("Instalacija počinje...")
    print("Čitanje database")
    create_shelly_script()
    print("Instalacija završena.")

if __name__ == "__main__":
    main()
