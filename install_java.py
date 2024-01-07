#!/bin/python

#######################################################################################################
#
# This script is licensed under RedDo development
# https://discord.reddo.es/
#
# .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
#| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
#| |  _______     | || |  _________   | || |  ________    | || |  ________    | || |     ____     | |
#| | |_   __ \    | || | |_   ___  |  | || | |_   ___ `.  | || | |_   ___ `.  | || |   .'    `.   | |
#| |   | |__) |   | || |   | |_  \_|  | || |   | |   `. \ | || |   | |   `. \ | || |  /  .--.  \  | |
#| |   |  __ /    | || |   |  _|  _   | || |   | |    | | | || |   | |    | | | || |  | |    | |  | |
#| |  _| |  \ \_  | || |  _| |___/ |  | || |  _| |___.' / | || |  _| |___.' / | || |  \  `--'  /  | |
#| | |____| |___| | || | |_________|  | || | |________.'  | || | |________.'  | || |   `.____.'   | |
#| |              | || |              | || |              | || |              | || |              | |
#| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
# '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 


import os

global system
global downloads
global extension
if os.name == 'nt':
    extension = 'zip'
    system = 'win'
else:
    extension = 'tar.gz'
    system = 'linux'

downloads = {
    "Java6": f"https://cdn.azul.com/zulu/bin/zulu6.22.0.3-jdk6.0.119-{system}_x64.{extension}",
    "Java7": f"https://cdn.azul.com/zulu/bin/zulu7.56.0.11-ca-jdk7.0.352-{system}_x64.{extension}",
    "Java8": f"https://cdn.azul.com/zulu/bin/zulu8.74.0.17-ca-jre8.0.392-{system}_x64.{extension}",
    "Java9": f"https://cdn.azul.com/zulu/bin/zulu9.0.7.1-jdk9.0.7-{system}_x64.{extension}",
    "Java10": f"https://cdn.azul.com/zulu/bin/zulu10.3+5-jdk10.0.2-{system}_x64.{extension}",
    "Java11": f"https://cdn.azul.com/zulu/bin/zulu11.68.17-ca-jdk11.0.21-{system}_x64.{extension}",
    "Java12": f"https://cdn.azul.com/zulu/bin/zulu12.3.11-ca-jdk12.0.2-{system}_x64.{extension}",
    "Java13": f"https://cdn.azul.com/zulu/bin/zulu13.54.17-ca-jdk13.0.14-{system}_x64.{extension}",
    "Java14": f"https://cdn.azul.com/zulu/bin/zulu14.29.23-ca-jdk14.0.2-{system}_x64.{extension}",
    "Java15": f"https://cdn.azul.com/zulu/bin/zulu15.46.17-ca-jdk15.0.10-{system}_x64.{extension}",
    "Java16": f"https://cdn.azul.com/zulu/bin/zulu16.32.15-ca-jdk16.0.2-{system}_x64.{extension}",
    "Java17": f"https://cdn.azul.com/zulu/bin/zulu17.46.19-ca-jdk17.0.9-{system}_x64.{extension}",
    "Java18": f"https://cdn.azul.com/zulu/bin/zulu18.32.13-ca-jdk18.0.2.1-{system}_x64.{extension}",
    "Java19": f"https://cdn.azul.com/zulu/bin/zulu19.32.13-ca-jdk19.0.2-{system}_x64.{extension}",
    "Java20": f"https://cdn.azul.com/zulu/bin/zulu20.32.11-ca-jdk20.0.2-{system}_x64.{extension}",
    "Java21": f"https://cdn.azul.com/zulu/bin/zulu21.30.15-ca-jdk21.0.1-{system}_x64.{extension}",
    "Java22": f"https://cdn.azul.com/zulu/bin/zulu23.0.11-beta-jdk23.0.0-beta.1-{system}_x64.{extension}",
    "Java23": f"https://cdn.azul.com/zulu/bin/zulu23.0.11-beta-jdk23.0.0-beta.1-{system}_x64.{extension}"
}

def load(*imports):
    for import_data in imports:
        name = import_data['name']
        install = import_data['install']
        function = import_data['def']

        try:
            module = __import__(name)
            if not module:
                print(f'Error while importing: {name}')

            function(name, module)
        except Exception as error:
            print(f'Failed to import {name}: {error}')
            os.system(f'pip install {install}')

def defaultDefine(name, module):
    globals()[name] = module

def createImport(importName, installName=None, globalDef=defaultDefine):
    if installName == None:
        installName = importName

    return {
        'name': importName,
        'install': installName,
        'def': globalDef
    }

load(
    createImport('shutil'), 
    createImport('sys'), 
    createImport('signal'), 
    createImport('urllib.request', 'urllib', lambda n, md: globals().__setitem__('urllib', md)), 
    createImport('time'), 
    createImport('colorama', 'colorama', lambda n, md: globals().__setitem__('Fore', md.Fore)),
)

def close_program():
    print(f"\n{Fore.RED}Exiting program... {Fore.RESET}")
    time.sleep(2)
    os.system("cls || clear")
    sys.exit(0)

def ctrl_c(sig, frame):
    close_program()

global forceDownload
global overwriteJava
global overwriteSetjava

def main_menu():
    forceDownload = False
    overwriteJava = False
    overwriteSetjava = False
    firstTime = True

    isAny = False
    signal.signal(signal.SIGINT, ctrl_c)

    while not isAny:
        os.system("cls || clear")
        if firstTime:
            firstTime = False
            print(f'''
{Fore.CYAN}This script is licensed under RedDo development
{Fore.CYAN}https://discord.reddo.es/

{Fore.RED}  _____          _ _____        
{Fore.RED} |  __ \        | |  __ \       
{Fore.RED} | |__) |___  __| | |  | | ___  
{Fore.RED} |  _  // _ \/ _` | |  | |/ _ \ 
{Fore.RED} | | \ \  __/ (_| | |__| | (_) |
{Fore.RED} |_|  \_\___|\__,_|_____/ \___/ 
                                
{Fore.LIGHTBLACK_EX}Developed by: {Fore.MAGENTA}@KarmaDev{Fore.LIGHTBLACK_EX} and{Fore.MAGENTA} @MrGonci{Fore.RESET}
            ''')
            time.sleep(5)

        os.system("cls || clear")
        print(f'''
                {Fore.CYAN} WELCOME TO {Fore.BLUE}MULTI{Fore.CYAN}-JAVA SETUP FOR {Fore.LIGHTBLACK_EX}{system}{Fore.RESET}

        (1) Download java versions    {Fore.CYAN}( {Fore.MAGENTA}WILL IGNORE IF INSTALLED {Fore.CYAN}){Fore.RESET}
        (2) Overwrite java command    {Fore.CYAN}( {Fore.MAGENTA}WILL WRITE IF NOT EXISTS {Fore.CYAN}){Fore.RESET}
        (3) Overwrite setjava command {Fore.CYAN}( {Fore.MAGENTA}WILL WRITE IF NOT EXISTS {Fore.CYAN}){Fore.RESET}

{Fore.RED} Type {Fore.MAGENTA}CANCEL{Fore.RED} or {Fore.MAGENTA}EXIT{Fore.RED} to quit the program{Fore.RESET}
        ''')
        option = input(f"{Fore.CYAN}Select your option(s) {Fore.RESET} ").lower().strip()
        
        if "1" in option:
            isAny = True
            forceDownload = True
        if "2" in option:
            isAny = True
            overwriteJava = True
        if "3" in option:
            isAny = True
            overwriteSetjava = True
        if "exit" in option or "cancel" in option and not isAny:
            close_program()

    print(f'''
        {Fore.CYAN} PREPARING SETUP {Fore.BLUE}JAVA{Fore.CYAN} PLEASE FILL IN THE REQUIRED INFORMATION
         OR LEAVE EMPTY FOR DEFAULT VALUES{Fore.RESET}
        ''')

    option = input(f"{Fore.CYAN}Write in a install directory {Fore.LIGHTBLACK_EX}[{Fore.GREEN}/java_downloader/version{Fore.LIGHTBLACK_EX}] ({Fore.RED} WILL BE CREATED IF NOT EXISTS {Fore.CYAN}){Fore.RESET} ").lower().strip()
    option2 = input(f"{Fore.CYAN}Write in a scripts install directory   {Fore.LIGHTBLACK_EX}[{Fore.GREEN}/usr/local/bin{Fore.LIGHTBLACK_EX}] ({Fore.RED} WILL BE CREATED IF NOT EXISTS {Fore.CYAN}){Fore.RESET} ").lower().strip()

    if option == "":
        option = "/java_downloader/version"

    if option2 == "":
        option2 = "/usr/local/bin"

    absOption = os.path.abspath(option).replace('\\', '/')
    absOption2 = os.path.abspath(option2).replace('\\', '/')

    if not os.path.exists(option):
        try:
            os.makedirs(option)
        except Exception as error:
            print(f'{Fore.RED}Failed to create directory {option}. Exiting program{Fore.RESET}')
            print(f'{Fore.CYAN}Error details:{Fore.RESET} {error}')
            close_program()

    for key in downloads:
        value = downloads[key]
        print(f'{Fore.CYAN}Preparing to download {Fore.LIGHTBLACK_EX}{key}{Fore.CYAN} from{Fore.LIGHTBLACK_EX} {value}{Fore.CYAN} to{Fore.LIGHTBLACK_EX} {option}{Fore.RESET}')
        if not os.path.exists('downloads'):
            os.makedirs('downloads')
            
        file_name = f'downloads/{key}.{extension}'
        target_file = f'{option}/{key}'

        if not os.path.exists(target_file) and not os.path.exists(file_name) or forceDownload:
            try:
                with urllib.request.urlopen(value) as response, open(file_name, 'wb') as out_file:
                    try:
                        shutil.copyfileobj(response, out_file)
                        print(f'{Fore.GREEN}Successfully downloaded{Fore.LIGHTBLACK_EX} {key}{Fore.RESET}')
                    except Exception as error:
                        print(f'{Fore.RED}Successfully downloaded {Fore.LIGHTBLACK_EX}{key}{Fore.RED} but failed to copy{Fore.RESET}')
                        print(f'{Fore.CYAN}Error details:{Fore.RESET} {error}')
            except Exception as error:
                print(f'{Fore.RED}An error occurred while downloading {Fore.LIGHTBLACK_EX}{key}{Fore.RESET}')
                print(f'{Fore.CYAN}Error details:{Fore.RESET} {error}')
        else:
            print(f'{Fore.RED}Ignoring download of{Fore.LIGHTBLACK_EX} {key}{Fore.RED} because it already seems to be downloaded{Fore.RESET}')

    for key in downloads:
        file_name = f'downloads/{key}.{extension}'
        target_file = f'{option}/{key}'

        if os.path.exists(target_file):
            contents = os.listdir(target_file)
            if len(contents) < 2:
                shutil.rmtree(target_file)

            if os.path.exists(target_file) and forceDownload:
                shutil.rmtree(target_file)

            if not os.path.exists(target_file):
                print(f'{Fore.CYAN}Preparing to install {Fore.LIGHTBLACK_EX}{key}{Fore.CYAN} to {Fore.LIGHTBLACK_EX}{target_file} {Fore.RESET}')
                try:
                    os.makedirs(target_file)
                except Exception as error:
                    print(f'{Fore.RED}Failed to create directory{Fore.LIGHTBLACK_EX} {target_file}{Fore.RESET}')
                    print(f'{Fore.CYAN}Error details:{Fore.RESET} {error}')
                    close_program()
                
                try:
                    shutil.unpack_archive(file_name, target_file)
                    extracted = os.listdir(target_file)[0]
                    extracted = f'{target_file}/{extracted}'

                    for item in os.listdir(extracted):
                        source = os.path.join(extracted, item)
                        destination = os.path.join(target_file, item)

                        if os.path.isdir(source):
                            shutil.move(source, destination)
                        else:
                            shutil.move(source, target_file)

                    shutil.rmtree(extracted)
                    print(f'{Fore.GREEN}Successfully installed{Fore.LIGHTBLACK_EX} {key}{Fore.RESET}')
                except Exception as error:
                    print(f'{Fore.RED}Failed to extract{Fore.LIGHTBLACK_EX} {key}{Fore.RED}.{Fore.RESET}')
                    print(f'{Fore.CYAN}Error details:{Fore.RESET} {error}')
                    pass
            else:
                print(f'{Fore.RED}Ignoring installation of{Fore.LIGHTBLACK_EX} {key}{Fore.RED} because it already seems to be installed{Fore.RESET}')

            aliasFile = f'{option2}/{key.lower()}'
            absTarget = os.path.abspath(target_file).replace('\\', '/')
            aliasContents = ['#!/bin/bash', '', f'{absTarget}/bin/java $@']

            if not os.path.exists(aliasFile) or overwriteJava:
                parent = os.path.dirname(aliasFile)
                if not os.path.exists(parent):
                    os.makedirs(parent)

                print(f'{Fore.CYAN}Adding{Fore.LIGHTBLACK_EX} {key}{Fore.CYAN} to path ( {Fore.LIGHTBLACK_EX}{key.lower()} -version{Fore.CYAN} ){Fore.RESET}')
                if os.path.exists(aliasFile):
                    os.remove(aliasFile)
                
                with open(aliasFile, 'w') as targetFile:
                    for line in aliasContents:
                        targetFile.write(f'{line}\n')
                
                os.chmod(aliasFile, os.stat(aliasFile).st_mode | 0o111)
            else:
                print(f'{Fore.RED}Ignoring creation of{Fore.LIGHTBLACK_EX} {aliasFile}{Fore.RESET}')

    javaFile = f'{option2}/java'
    javaContent = [
        '#!/bin/bash', 
        '', 
        f'if [ ! -f "{absOption2}/java_version" ]; then',  
        '   setjava 20',
        'fi',
        '',
        f'version=$(cat "{absOption2}/java_version")',
        f'{absOption}/Java$version/bin/java $@'
    ]

    if not os.path.exists(javaFile) or overwriteJava:
        parent = os.path.dirname(javaFile)
        if not os.path.exists(parent):
            os.makedirs(parent)

        print(f'{Fore.CYAN}Adding{Fore.LIGHTBLACK_EX} java{Fore.CYAN} to path ( {Fore.LIGHTBLACK_EX}java -version{Fore.CYAN} ){Fore.RESET}')
        if os.path.exists(javaFile):
            os.remove(javaFile)

        with open(javaFile, 'w') as targetFile:
            for line in javaContent:
                targetFile.write(f'{line}\n')
                
        os.chmod(javaFile, os.stat(javaFile).st_mode | 0o111)

    setJavaFile = f'{option2}/setjava'
    setJavaContent = [
        '#!/bin/bash', 
        '', 
        'function setJava() {',  
        '   local version="$1"',
        '   if ((version >= 6 && version <= 23)); then',
        f'       touch "{absOption2}/java_version"',
        f'       echo $version > "{absOption2}/java_version"',
        '        echo "Successfully updated java version to $version"',
        '   else',
        '       echo "Invalid java version"',
        '   fi',
        '}',
        '',
        'setJava $1'
    ]

    if not os.path.exists(setJavaFile) or overwriteSetjava:
        parent = os.path.dirname(setJavaFile)
        if not os.path.exists(parent):
            os.makedirs(parent)

        print(f'{Fore.CYAN}Adding{Fore.LIGHTBLACK_EX} setjava{Fore.CYAN} to path ( {Fore.LIGHTBLACK_EX}setjava <version>{Fore.CYAN} ){Fore.RESET}')
        if os.path.exists(setJavaFile):
            os.remove(setJavaFile)

        with open(setJavaFile, 'w') as targetFile:
            for line in setJavaContent:
                targetFile.write(f'{line}\n')
                
        os.chmod(setJavaFile, os.stat(setJavaFile).st_mode | 0o111)

if __name__ == "__main__":    
    main_menu()