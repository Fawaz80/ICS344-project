# Caldera Setup
Below are the steps for setting up Caldera

## Prerequisites
- Python 3.9+
- Git

## Installation
bash
git clone https://github.com/mitre/caldera.git --recursive
cd caldera
pip install -r requirements.txt
python3 server.py

Access

    URL: http://localhost:8888
    Default credentials: admin / admin

Debugging Common Issues

    Ensure all dependencies are installed: pip install -r requirements.txt.
    Check logs: caldera/logs.

ftp_attack.json (Adversary Profile):

    {
      "id": "ftp_attack",
      "name": "FTP Attack",
      "description": "Brute-force FTP credentials",
      "atomic_ordering": [1],
      "phases": {
        "1": [{"id": "1234", "name": "Hydra Brute Force", "executor": "linux"}]
      }
    }

