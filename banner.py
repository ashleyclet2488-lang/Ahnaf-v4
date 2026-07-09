# banner.py

import random
from colorama import Fore, Style, init
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

init(autoreset=True)
console = Console()

def random_color():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    return random.choice(colors)

def show_banner():
    color = random_color()
    banner = f"""
{color}
    █████╗ ██╗  ██╗███╗   ██╗ █████╗ ███████╗    ██╗   ██╗██╗  ██╗
   ██╔══██╗██║  ██║████╗  ██║██╔══██╗██╔════╝    ██║   ██║██║  ██║
   ███████║███████║██╔██╗ ██║███████║█████╗      ██║   ██║███████║
   ██╔══██║██╔══██║██║╚██╗██║██╔══██║██╔══╝      ╚██╗ ██╔╝╚════██║
   ██║  ██║██║  ██║██║ ╚████║██║  ██║██║          ╚████╔╝      ██║
   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝           ╚═══╝       ╚═╝
{Style.RESET_ALL}
"""
    console.print(banner, style="bold")
    panel = Panel(
        Text("⚡ Ahnaf v4 — Instagram Pentest Toolkit ⚡\n"
             "👑 Owner: Ahnaf\n"
             "📌 Version: 4.0\n"
             "⚙ Mode: Multi-Proxy + Temp Mail Account Generator\n"
             "🔥 Features: Like | Comment | Follow | Share | Save | Report | Broadcast Join",
             justify="center", style="bold cyan"),
        border_style="bright_red",
        title="[bold yellow]★  WELCOME TO AHNAF v4  ★[/bold yellow]",
        subtitle="[bold green]Authorized Security Testing Only[/bold green]"
    )
    console.print(panel)
    print(Fore.YELLOW + "=" * 70)
    print(Fore.GREEN + "        ⚡ AUTHORIZED SECURITY TESTING ONLY ⚡")
    print(Fore.YELLOW + "=" * 70 + "\n")
