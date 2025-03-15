import os
import sys
import time
import shutil
import platform
import requests
from colorama import init, Fore, Back, Style

init()

xKai_name = "Result"
os.makedirs(xKai_name, exist_ok=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_for_updates():
    update_url = "https://cpkarma.cc/updates.txt"
    current_version = "2.0"

    try:
        response = requests.get(update_url, timeout=5)
        if response.status_code == 200:
            latest_version = response.text.strip()
            if latest_version > current_version:
                message = f"A new version ({latest_version}) is available! Please update your script"
                display_centered_message(message, Fore.YELLOW)
            else:
                message = f"You are using the latest version ({current_version})"
                display_centered_message(message, Style.BRIGHT + Fore.GREEN)
        else:
            message = f"Failed to check for updates (status code: {response.status_code})"
            display_centered_message(message, Fore.RED)
    except requests.RequestException as e:
        message = f"Error checking for updates"
        display_centered_message(message, Fore.RED)

def display_centered_message(message, color=Fore.WHITE):
    columns, _ = get_terminal_size()
    padded_message = message.center(columns)
    print(f"{color}{padded_message}{Style.RESET_ALL}\n")

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
        "1": "xKai/xCrackv2-A.py",
        "2": "xKai/xCrackv2-B.py",
        "3": "xKai/xCrackv2-C.py",
        "4": "xKai/xCrackv2-D.py",
        "5": "xKai/xCrackv2-E.py",
        "6": "xKai/xCrackv2-F.py",
        "7": "xKai/xCrackv2-G.py",
        "8": "xKai/xCrackv2-H.py",
        "9": "xKai/xCrackv2-I.py",
        "10": "xKai/xCrackv2-J.py",
        "11": "xKai/xCrackv2-K.py",
        "12": "xKai/xCrackv2-L.py",
        "13": "xKai/xCrackv2-M.py",
        "14": "xKai/xCrackv2-N.py",
        "15": "xKai/xCrackv2-O.py",
        "16": "xKai/xCrackv2-P.py",
        "17": "xKai/xCrackv2-Q.py",
        "18": "xKai/xCrackv2-R.py",
        "19": "xKai/xCrackv2-S.py",
        "20": "xKai/xCrackv2-T.py"
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
    set_terminal_size(100, 53)

    try:
        while True:
            clear_screen()
            print_banner()
            check_for_updates()
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
