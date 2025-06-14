import os
import json
import shlex
from colorama import Fore, init

init(autoreset=True)

def color(name):
    return {
        "GREEN": '\033[32m',
        "LIGHTGREEN_EX": '\033[92m',
        "LIGHTYELLOW_EX": '\033[33m',
        "LIGHTLIGHTYELLOW_EX_EX": '\033[93m',
        "CYAN": '\033[36m',
        "LIGHTCYAN_EX": '\033[96m',
        "BLUE": '\033[34m',
        "LIGHTBLUE_EX": '\033[94m',
        "MAGENTA": '\033[35m',
        "LIGHTMAGENTA_EX": '\033[95m',
        "RED": '\033[31m',
        "LIGHTRED_EX": '\033[91m',
        "BLACK": '\033[30m',
        "LIGHTBLACK_EX": '\033[90m',
        "WHITE": '\033[37m',
        "LIGHTWHITE_EX": '\033[97m'
    }.get(name, '\033[37m')

lightwhite = color("LIGHTWHITE_EX")
banner = rf"""
{Fore.MAGENTA}███████╗ ██████╗ ██╗         {Fore.LIGHTYELLOW_EX}██████╗ {Fore.LIGHTGREEN_EX}██╗   ██╗{lightwhite}
{Fore.MAGENTA}██╔════╝██╔═══██╗██║         {Fore.LIGHTYELLOW_EX}██╔══██╗{Fore.LIGHTGREEN_EX}╚██╗ ██╔╝{lightwhite}
{Fore.MAGENTA}███████╗██║   ██║██║         {Fore.LIGHTYELLOW_EX}██████╔╝{Fore.LIGHTGREEN_EX} ╚████╔╝ {lightwhite}
{Fore.MAGENTA}╚════██║██║   ██║██║         {Fore.LIGHTYELLOW_EX}██╔═══╝ {Fore.LIGHTGREEN_EX}  ╚██╔╝  {lightwhite}
{Fore.MAGENTA}███████║╚██████╔╝███████╗    {Fore.LIGHTYELLOW_EX}██║     {Fore.LIGHTGREEN_EX}   ██║   {lightwhite}
{Fore.MAGENTA}╚══════╝ ╚═════╝ ╚══════╝    {Fore.LIGHTYELLOW_EX}╚═╝     {Fore.LIGHTGREEN_EX}   ╚═╝   {lightwhite}
"""

def run_main_menu():
    while True:
        os.system("clear" if os.name != "nt" else "cls")
        print(banner)
        print(f"""
[{Fore.MAGENTA}01{lightwhite}] See Your {Fore.MAGENTA}Solana {lightwhite}Address
[{Fore.MAGENTA}02{lightwhite}] See Your {Fore.MAGENTA}Solana {lightwhite}Balance
[{Fore.MAGENTA}03{lightwhite}] Create A Mint Address ( NEEDED )
[{Fore.MAGENTA}04{lightwhite}] Save Mint Address ( NEEDED )
[{Fore.MAGENTA}05{lightwhite}] Change Metadata For Mint ( Means Profile )
[{Fore.MAGENTA}06{lightwhite}] Give yourself money ( DevNet ) [ MINT ]
[{Fore.MAGENTA}07{lightwhite}] Check Mint Balance
[{Fore.MAGENTA}08{lightwhite}] Transfer Tokens
[{Fore.MAGENTA}09{lightwhite}] Change Metadata ( Means Profile )
[{Fore.MAGENTA}10{lightwhite}] Disable Mint ( For Market Place ) [ MainNet Only ]
[{Fore.MAGENTA}11{lightwhite}] Important Websites
[{Fore.MAGENTA}12{lightwhite}] {Fore.RED}Exit{lightwhite}
""")
        choice = input(f"[{Fore.MAGENTA}Sol{Fore.LIGHTYELLOW_EX}P{Fore.LIGHTGREEN_EX}Y{lightwhite}]: ").strip()

        if choice not in [str(i) for i in range(1, 13)]:
            input("Invalid choice. Press Enter...")
            continue

        if choice == "1":
            os.system("solana address")
        elif choice == "2":
            os.system("solana balance")
        elif choice == "3":
            mint_name = input("Change the mint name? (Y/N): ").strip().lower()
            if mint_name == "y":
                name = input("New mint name: ")
                os.system(f"solana-keygen grind --starts-with {shlex.quote(name)}:1")
            else:
                os.system("solana-keygen grind --starts-with mnt:1")
        elif choice == "4":
            mint_address = input("Enter mint.json (WITHOUT .json): ").strip()
            os.system(f"""spl-token create-token \
--program-id TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb \
--enable-metadata \
--decimals 9 \
{shlex.quote(mint_address)}.json""")
        elif choice == "5":
            print("Must be square image (512x512 or 1024x1024) under 100KB.\nUse https://app.pinata.cloud/")
            name = input("Coin Name: ")
            symbol = input("Symbol: ")
            desc = input("Description: ")
            image = input("Image URL: ")
            metadata = {
                "name": name,
                "symbol": symbol,
                "description": desc,
                "image": image
            }
            with open("metadata.json", "w") as f:
                json.dump(metadata, f, indent=2)
            os.system("nano metadata.json")
            mnt = input("Mint Address (no .json): ")
            link = input("Metadata link: ")
            os.system(f"spl-token initialize-metadata {shlex.quote(mnt)} \"{name}\" \"{symbol}\" {shlex.quote(link)}")
            os.system(f"spl-token create-account {shlex.quote(mnt)}")
        elif choice == "6":
            mnt = input("Mint Address (no .json): ")
            amount = input("Amount: ")
            os.system(f"spl-token mint {shlex.quote(mnt)} {amount}")
        elif choice == "7":
            mnt = input("Mint Address (no .json): ")
            os.system(f"spl-token balance {shlex.quote(mnt)}")
        elif choice == "8":
            sender = input("Sender Address (no .json): ")
            amount = input("Amount: ")
            receiver = input("Receiver Address (no .json): ")
            os.system(f"spl-token transfer {shlex.quote(sender)} {amount} {shlex.quote(receiver)} --fund-recipient --allow-unfunded-recipient")
        elif choice == "9":
            mnt = input("Mint Address (no .json): ")
            link = input("Metadata link: ")
            os.system(f"spl-token update-metadata {shlex.quote(mnt)} uri {shlex.quote(link)}")
        elif choice == "10":
            mnt = input("Mint Address (no .json): ")
            os.system(f"spl-token authorize {shlex.quote(mnt)} mint --disable")
            os.system(f"spl-token authorize {shlex.quote(mnt)} freeze --disable")
        elif choice == "11":
            print("""
https://app.pinata.cloud/ipfs/files
https://faucet.solana.com/
https://raydium.io/swap/
https://raydium.io/liquidity-pools/
https://solscan.io/
https://sol-incinerator.com/
https://dexscreener.com/
""")
            input("Press Enter to go back...")
        elif choice == "12":
            break

def setup_or_enter():
    print(banner)
    if input(f"{lightwhite}Did you use this before? (Y/N): ").strip().lower() == "y":
        token_folder = input("Enter Your Token folder name: ")
        os.chdir(token_folder)
        os.system("docker run -it -v $(pwd):/solana-token -v $(pwd)/solana-data:/root/.config/solana heysolana bash -c 'cd /solana-token && python3 main.py'")
    else:
        if input("Install Docker? (Y/N): ").strip().lower() == "y":
            os.system("sudo apt-get update")
            os.system("sudo apt-get install -y ca-certificates curl gnupg lsb-release")
            os.system("sudo install -m 0755 -d /etc/apt/keyrings")
            os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg")
            os.system("sudo chmod a+r /etc/apt/keyrings/docker.gpg")
            os.system('echo \"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] '
                      'https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\" | '
                      'sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
            os.system("sudo apt-get update")
            os.system("sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin")
            os.system("sudo usermod -aG docker $USER")
            os.system("newgrp docker")
            os.system("sudo dockerd > /dev/null 2>&1 &")
            input("Press Enter...")

        if input("Test Docker? (Y/N): ").strip().lower() == "y":
            os.system("docker run hello-world")

        token_name = input("Enter Your Token Name: ")
        os.makedirs(token_name, exist_ok=True)
        os.chdir(token_name)

        with open("Dockerfile", "w") as f:
            f.write("""\
FROM debian:bookworm-slim
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \\
    curl build-essential libssl-dev pkg-config nano python3 \\
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \\
    && apt-get clean && rm -rf /var/lib/apt/lists/*
ENV PATH="/root/.cargo/bin:$PATH"
RUN rustc --version
RUN curl -sSfL https://release.anza.xyz/stable/install | sh \\
    && echo 'export PATH="$HOME/.local/share/solana/install/active_release/bin:$PATH"' >> ~/.bashrc
ENV PATH="/root/.local/share/solana/install/active_release/bin:$PATH"
RUN solana --version
RUN solana config set -ud
WORKDIR /solana-token
CMD ["/bin/bash"]
""")

        os.system("docker build -t heysolana .")
        os.system("docker run -it -v $(pwd):/solana-token -v $(pwd)/solana-data:/root/.config/solana heysolana bash -c 'cd /solana-token && python3 main.py'")

if __name__ == "__main__":
    setup_or_enter()
