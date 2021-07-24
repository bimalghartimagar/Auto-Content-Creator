from dotenv import dotenv_values
from pathlib import Path

project_path = "~/personal/repos/acc/backend/"
path = Path(project_path).expanduser()

config = dotenv_values(f"{str(path)}/.env")