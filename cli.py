import argparse, os
from .crypto import encrypt_file, decrypt_file

def main():
    parser = argparse.ArgumentParser(description="EnvSync Tool")
    sub = parser.add_subparsers(dest="cmd")

    p_enc = sub.add_parser("encrypt")
    p_enc.add_argument("file")
    p_enc.add_argument("--key", required=True)

    p_dec = sub.add_parser("decrypt")
    p_dec.add_argument("file")
    p_dec.add_argument("--key", required=True)

    p_sync = sub.add_parser("sync")
    p_sync.add_argument("files", nargs="+")
    p_sync.add_argument("--key", required=True)

    args = parser.parse_args()

    if args.cmd == "encrypt":
        encrypt_file(args.file, args.key)
    elif args.cmd == "decrypt":
        decrypt_file(args.file, args.key)
    elif args.cmd == "sync":
        for f in args.files:
            encrypt_file(f, args.key)
    else:
        parser.print_help()
