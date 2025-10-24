# EnvSync Tool

A DevOps productivity tool to **safely sync `.env` environment variable files** across multiple machines or team members **with AES encryption**.

Perfect for teams who need to share environment configs securely without leaking secrets in Git.

## Features
- Encrypt `.env` files with a shared key
- Decrypt files securely when needed
- Sync multiple environment versions (`.env.dev`, `.env.prod`, etc.)
- Designed for Git-based workflows

## Install
```bash
pip install -r requirements.txt
pip install -e .
```

## Usage
```bash
# Encrypt .env using a shared key
envsync encrypt .env --key YOUR_SECRET_KEY

# Decrypt to restore original
envsync decrypt .env.enc --key YOUR_SECRET_KEY

# Sync multiple files
envsync sync .env.dev .env.prod --key MYSECRET
```

## Security Notes
- Uses AES-256 encryption
- Keys are **never** stored
- Safe to commit encrypted `.env.enc` to Git

## License
MIT
