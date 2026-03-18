"""CLI for nritya."""
import sys, json, argparse
from .core import Nritya

def main():
    parser = argparse.ArgumentParser(description="Nritya — Classical Dance Corrector. AI pose correction for Bharatanatyam, Kathak, and other classical dances.")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = Nritya()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.process(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"nritya v0.1.0 — Nritya — Classical Dance Corrector. AI pose correction for Bharatanatyam, Kathak, and other classical dances.")

if __name__ == "__main__":
    main()
