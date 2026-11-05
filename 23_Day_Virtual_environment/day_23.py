# Day 23 - Exercise 1: Create a project directory with a virtual environment
# Same steps as the lesson (mkdir flask_project, create venv, pip install Flask, pip freeze),
# using the stdlib venv module instead of the virtualenv package.
import subprocess
import venv
from pathlib import Path

project = Path(__file__).parent / 'flask_project'
env_dir = project / 'venv'

project.mkdir(exist_ok=True)
if not env_dir.exists():
    venv.create(env_dir, with_pip=True)
print(sorted(p.name for p in project.iterdir()), flush=True)  # like `ls`

# Keep the venv out of git, as the lesson recommends
(project / '.gitignore').write_text('venv/\n')

# Equivalent of activating the venv and running pip: call the venv's own python
python = env_dir / 'bin' / 'python'  # Windows: venv/Scripts/python.exe
subprocess.run([python, '-m', 'pip', 'install', '-q', 'Flask'], check=True)
subprocess.run([python, '-m', 'pip', 'freeze'], check=True)
