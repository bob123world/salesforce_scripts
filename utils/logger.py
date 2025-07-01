from rich.console import Console
from rich.logging import RichHandler
import logging
import os
from datetime import datetime

# Ensure the logs folder exists
os.makedirs("logs", exist_ok=True)

# Create a timestamped log file
log_filename = datetime.now().strftime("logs/log_%Y-%m-%d_%H-%M-%S.log")

# Set up the basic formatter for the file handler
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# File handler
file_handler = logging.FileHandler(log_filename, encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)

# Rich (console) handler
console = Console()
rich_handler = RichHandler(console=console, rich_tracebacks=True)
rich_handler.setLevel(logging.INFO)  # show less verbose logs in console

# Combine both handlers
logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",  # RichHandler ignores this format
    handlers=[rich_handler, file_handler]
)

logger = logging.getLogger("rich_logger")