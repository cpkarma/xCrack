import os
import sys
import time
import shutil
import platform
from colorama import init, Fore, Back, Style

init()

xKai_name = "Result"
os.makedirs(xKai_name, exist_ok=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    columns, rows = shutil.get_terminal_size()
    return columns, rows

def set_terminal_size(columns, lines):
    system = platform.system()
    if system == "Windows":
        os.system(f'mode con: cols={columns} lines={lines}')
    elif system in ["Linux", "Darwin"]:
        print(f"\033[8;{lines};{columns}t")
    else:
        print(f"{Fore.RED}[!] Unsupported operating system: {system}{Style.RESET_ALL}")

def print_typing_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_banner():
    columns, _ = get_terminal_size()
    banner_title = f"{Fore.WHITE + Style.BRIGHT + Back.CYAN}{' ' * ((columns - len('xCrack')) // 2)}xCrack{' ' * ((columns - len('xCrack')) // 2)}{Style.RESET_ALL}\n\n{Fore.YELLOW}Telegram:{Style.RESET_ALL} https://t.me/KarmaSyndicate\n"
    print(banner_title)

    banner_subtitle = f"{Fore.YELLOW}Note:{Style.RESET_ALL} Use At Your Own Risk\n"
    print_typing_effect(banner_subtitle, delay=0.02)

def options_menu():
    columns, _ = get_terminal_size()
    menu_items = [
        f"{Style.BRIGHT + Fore.WHITE} [► cPanel Section ◄]{Style.RESET_ALL}\n",
        f"   → 01.{Style.BRIGHT + Fore.GREEN} Mass cPanel Active Checker{Style.RESET_ALL}",
        f"   → 02.{Style.BRIGHT + Fore.GREEN} Mass cPanel To Shell Uploader{Style.RESET_ALL}",
        f"   → 03.{Style.BRIGHT + Fore.GREEN} Mass cPanel To SMTP Cracker{Style.RESET_ALL}",
        f"   → 04.{Style.BRIGHT + Fore.GREEN} Mass cPanel To Webmail Cracker{Style.RESET_ALL}",
        f"   → 05.{Style.BRIGHT + Fore.GREEN} Mass cPanel To WHM Cracker{Style.RESET_ALL} (Reseller)",
        f"   → 06.{Style.BRIGHT + Fore.GREEN} Mass cPanel To WHM Cracker{Style.RESET_ALL} (Root)",

        f"\n{Style.BRIGHT + Fore.WHITE} [► Shell Section ◄]{Style.RESET_ALL}\n",
        f"   → 07.{Style.BRIGHT + Fore.GREEN} Mass Shell To Any File Uploader{Style.RESET_ALL}",
        f"   → 08.{Style.BRIGHT + Fore.GREEN} Mass Shell To cPanel Cracker{Style.RESET_ALL}",
        f"   → 09.{Style.BRIGHT + Fore.GREEN} Mass Shell To SMTP Cracker{Style.RESET_ALL}",
        f"   → 10.{Style.BRIGHT + Fore.GREEN} Mass Shell To WHM Cracker{Style.RESET_ALL}",
        f"   → 11.{Style.BRIGHT + Fore.GREEN} Mass Shell Checker{Style.RESET_ALL}",

        f"\n{Style.BRIGHT + Fore.WHITE} [► WHM Section ◄]{Style.RESET_ALL}\n",
        f"   → 12.{Style.BRIGHT + Fore.GREEN} Mass WHM Checker{Style.RESET_ALL}",
        f"   → 13.{Style.BRIGHT + Fore.GREEN} Mass WHM To cPanel Reset{Style.RESET_ALL}",

        f"\n{Style.BRIGHT + Fore.WHITE} [► SMTP Section ◄]{Style.RESET_ALL}\n",
        f"   → 14.{Style.BRIGHT + Fore.GREEN} Mass Working SMTP Checker{Style.RESET_ALL}",

        f"\n{Style.BRIGHT + Fore.WHITE} [► Combo Section ◄]{Style.RESET_ALL}\n",
        f"   → 15.{Style.BRIGHT + Fore.GREEN} Combo To cPanel Cracker{Style.RESET_ALL}",

        f"\n{Style.BRIGHT + Fore.WHITE} [► Webmail Section ◄]{Style.RESET_ALL}\n",
        f"   → 16.{Style.BRIGHT + Fore.GREEN} Mass Webmail Checker{Style.RESET_ALL}",

        f"\n{Style.BRIGHT + Fore.WHITE} [► Others Section ◄]{Style.RESET_ALL}\n",
        f"   → 17.{Style.BRIGHT + Fore.GREEN} SSH Login Checker{Style.RESET_ALL}",
        f"   → 18.{Style.BRIGHT + Fore.GREEN} cPanel List Filter{Style.RESET_ALL} {Style.BRIGHT + Fore.WHITE}(Filter Your List Before Using){Style.RESET_ALL}",
        f"   → 19.{Style.BRIGHT + Fore.GREEN} Any List Splitter{Style.RESET_ALL} {Style.BRIGHT + Fore.WHITE}(Split Your Single List To Multiple){Style.RESET_ALL}",
        f"   → 20.{Style.BRIGHT + Fore.GREEN} Duplicate Shell List Filter{Style.RESET_ALL} {Style.BRIGHT + Fore.WHITE}(Remove Duplicate Shells){Style.RESET_ALL}",
        
        f"\n{Style.BRIGHT + Fore.WHITE + Back.RED}Type 'x' to quit the program.{Style.RESET_ALL}"
    ]

    for item in menu_items:
        print(item)

def execute_choice(choice):
    file_mapping = {
        "1": "xKai/xCrackA.py",
        "2": "xKai/xCrackB.py",
        "3": "xKai/xCrackC.py",
        "4": "xKai/xCrackD.py",
        "5": "xKai/xCrackE.py",
        "6": "xKai/xCrackF.py",
        "7": "xKai/xCrackG.py",
        "8": "xKai/xCrackH.py",
        "9": "xKai/xCrackI.py",
        "10": "xKai/xCrackJ.py",
        "11": "xKai/xCrackK.py",
        "12": "xKai/xCrackL.py",
        "13": "xKai/xCrackM.py",
        "14": "xKai/xCrackN.py",
        "15": "xKai/xCrackO.py",
        "16": "xKai/xCrackP.py",
        "17": "xKai/xCrackQ.py",
        "18": "xKai/xCrackR.py",
        "19": "xKai/xCrackS.py",
        "20": "xKai/xCrackT.py"
    }

    file_path = file_mapping.get(choice)

    if file_path:
        if os.path.exists(file_path):
            os.system(f"python {file_path}")
        else:
            print(f"\n{Fore.RED}[!] File not found: {file_path}{Style.RESET_ALL}\n")
    else:
        print(f"\n{Fore.RED}[!] Invalid choice, please try again.{Style.RESET_ALL}\n")

def main():
    set_terminal_size(100, 51)

    try:
        while True:
            clear_screen()
            print_banner()
            time.sleep(1)
            options_menu()

            choice = input(f"\n{Style.BRIGHT + Fore.CYAN}Enter your choice: {Style.RESET_ALL}").strip()

            if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]:
                execute_choice(choice)
            elif choice.lower() == "x":
                print(f"\n{Fore.LIGHTMAGENTA_EX}Thank you for using xCrack! Goodbye!{Style.RESET_ALL}\n")
                time.sleep(2)
                sys.exit()
            else:
                print(f"\n{Fore.RED}[!] Please select a valid option.{Style.RESET_ALL}\n")

            time.sleep(1)

    except KeyboardInterrupt:
        print(f"\n\n{Style.BRIGHT + Fore.WHITE + Back.GREEN}Thanks For Be With Karma Syndicate....Take Care!{Style.RESET_ALL}")
        time.sleep(2)
        sys.exit()

if __name__ == "__main__":
    main()
