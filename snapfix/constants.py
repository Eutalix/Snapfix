import os
from pathlib import Path

# Caminhos padrão
SNAP_DESKTOP_DIR = "/var/lib/snapd/desktop/applications"
MENU_DIR = Path.home() / ".local/share/applications"
AUTOSTART_DIR = Path.home() / ".config/autostart"
SNAP_MOUNT_DIR = "/snap"
DEFAULT_CONFIG_PATH = Path.home() / ".config/snapfix/config.json"

# Padrões de skip
DEFAULT_SKIP_PATTERNS = [
    'url-handler', 'show-updates', 'show_updates', 'url_handler',
    'refresh', 'update', 'desktop-launch', 'helper', 'preferences',
    'settings', 'xdg-open', 'open-url', 'install-launcher',
    'uninstall', 'register'
]
DEFAULT_SKIP_NAME_PATTERNS = ['url handler', 'show updates', 'update', 'refresh']

# Categorias FreeDesktop padrão (simplificado)
DEFAULT_FREEDESKTOP_CATEGORIES = {
    "AudioVideo": "AudioVideo", "Audio": "Audio", "Video": "Video",
    "Development": "Development", "Education": "Education", "Game": "Game",
    "Graphics": "Graphics", "Network": "Network", "Office": "Office",
    "Settings": "Settings", "System": "System", "Utility": "Utility",
    "Accessibility": "Accessibility", "ActionGames": "ActionGames",
    "AdventureGames": "AdventureGames", "ArcadeGames": "ArcadeGames",
    # ... outras categorias ...
    "Multimedia": "AudioVideo"
}
DEFAULT_MAPPING = {
    "Entertainment": "AudioVideo", "Games": "Game",
    "Multimedia": "AudioVideo", "Music": "AudioVideo",
    "Video": "AudioVideo", "Audio": "AudioVideo"
}

# Mensagens de feedback localizado
MESSAGES = {
    'en': {
        'start': "Starting snapfix...",
        'manual_mode': "Manual mode: organizing once.",
        'auto_mode': "Auto mode: organizing continuously. Press Ctrl+C to stop.",
        'no_snaps': "No Snap applications found or none new to add.",
        'added': "Added Snap app to menu:",
        'warn_no_category': "Warning: no mapped category; may appear under 'Other':",
        'uninstall_action': "Uninstall",
        'uninstall_exec': "pkexec snap remove {snap_name}",
        'background_spawned': "snapfix launched in background.",
        'autostart_ok': "snapfix added to startup applications.",
    },
    'pt': {
        'start': "Iniciando snapfix...",
        'manual_mode': "Modo manual: organizando uma vez.",
        'auto_mode': "Modo automático: organizando continuamente. Pressione Ctrl+C para parar.",
        'no_snaps': "Nenhum app Snap encontrado ou nenhum novo para adicionar.",
        'added': "App Snap adicionado ao menu:",
        'warn_no_category': "Aviso: nenhuma categoria mapeada; pode aparecer em 'Outros':",
        'uninstall_action': "Desinstalar",
        'uninstall_exec': "pkexec snap remove {snap_name}",
        'background_spawned': "snapfix iniciado em segundo plano.",
        'autostart_ok': "snapfix adicionado aos aplicativos de inicialização.",
    }
}
