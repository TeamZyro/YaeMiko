import re
from Mikobot.plugins import ALL_MODULES
import importlib

def extract_commands_from_text(text):
    """Extract all commands starting with / from a text block"""
    command_pattern = r"(?:^|\n)\s*/(\w+)(?:\s|$)"
    commands = re.findall(command_pattern, text)
    return sorted(set(commands))  # Remove duplicates and sort

def get_all_commands():
    """Get all commands from all modules' help texts"""
    all_commands = []
    
    for module_name in ALL_MODULES:
        try:
            imported_module = importlib.import_module("Mikobot.plugins." + module_name)
            if hasattr(imported_module, "__help__") and imported_module.__help__:
                help_text = imported_module.__help__
                commands = extract_commands_from_text(help_text)
                if commands:
                    all_commands.extend(commands)
        except Exception as e:
            print(f"Error processing module {module_name}: {e}")
    
    # Also check the main help callbacks for additional commands
    additional_sources = [
        # AI commands
        "*Command: /meinamix\n  • Description: Generates an image using the meinamix model.",
        "*Command: /darksushi\n  • Description: Generates an image using the darksushi model.",
        "*Command: /meinahentai\n  • Description: Generates an image using the meinahentai model.",
        "*Command: /darksushimix\n  • Description: Generates an image using the darksushimix model.",
        "*Command: /anylora\n  • Description: Generates an image using the anylora model.",
        "*Command: /cetsumix\n  • Description: Generates an image using the cetsumix model.",
        "*Command: /anything\n  • Description: Generates an image using the anything model.",
        "*Command: /absolute\n  • Description: Generates an image using the absolute model.",
        "*Command: /darkv2\n  • Description: Generates an image using the darkv2 model.",
        "*Command: /creative\n  • Description: Generates an image using the creative model.",
        "➽ /askgpt <write query>: A chatbot using GPT for responding to user queries.",
        "➽ /palm <write prompt>: Performs a Palm search using a chatbot.",
        "➽ /upscale <reply to image>: Upscales your image quality.",
        
        # Anime commands
        "**╔ /anime: **fetches info on single anime",
        "**╠ /character: **fetches info on multiple possible characters",
        "**╠ /manga: **fetches info on multiple possible mangas",
        "**╠ /airing: **fetches info on airing data for anime",
        "**╠ /studio: **fetches info on multiple possible studios",
        "**╠ /schedule: **fetches scheduled animes",
        "**╠ /browse: **get popular, trending or upcoming animes",
        "**╠ /top: **to retrieve top animes for a genre or tag",
        "**╠ /watch: **fetches watch order for anime series",
        "**╠ /fillers: **to get a list of anime fillers",
        "**╠ /gettags: **get a list of available tags",
        "**╠ /animequotes: **get random anime quotes",
        "**╚ /getgenres: **Get list of available Genres",
        "**╔**\n**╠ /anisettings: **to toggle NSFW lock and airing notifications",
    ]
    
    for text in additional_sources:
        commands = extract_commands_from_text(text)
        all_commands.extend(commands)
    
    # Remove duplicates and sort
    all_commands = sorted(set(all_commands))
    return all_commands

def generate_commands_list():
    """Generate a formatted list of all commands"""
    commands = get_all_commands()
    formatted_commands = []
    
    for cmd in commands:
        formatted_commands.append(f"/{cmd}")
    
    return "\n".join(formatted_commands)

if __name__ == "__main__":
    commands_list = generate_commands_list()
    print("=== ALL BOT COMMANDS ===")
    print(commands_list)
    print(f"\nTotal commands: {len(commands_list.splitlines())}")
