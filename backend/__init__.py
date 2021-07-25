from dotenv import dotenv_values
from pathlib import Path

project_path = "/backend"
path = Path(project_path).resolve()

config = dotenv_values(f"{str(path)}/.env")