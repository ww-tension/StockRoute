# === Stage 16: Add argparse support for the most common commands ===
# Project: StockRoute
import argparse

def main():
    parser = argparse.ArgumentParser(description="StockRoute CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all routes')
    list_parser.add_argument('--format', choices=['text', 'json'], default='text')
    
    # Add route command
    add_parser = subparsers.add_parser('add', help='Add a new delivery route')
    add_parser.add_argument('name', help='Route name')
    add_parser.add_argument('-c', '--checkpoints', nargs='+', required=True, help='Checkpoint IDs')
    
    # Transfer command
    transfer_parser = subparsers.add_parser('transfer', help='Transfer stock between checkpoints')
    transfer_parser.add_argument('--from_cp', dest='from_checkpoint', required=True)
    transfer_parser.add_argument('--to_cp', dest='to_checkpoint', required=True)
    transfer_parser.add_argument('--batch_id', required=True)
    
    # Exception command
    exception_parser = subparsers.add_parser('exception', help='Log an exception note')
    exception_parser.add_argument('--route', required=True)
    exception_parser.add_argument('--note', required=True)
    
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 1
    
    # Placeholder for actual logic implementation
    print(f"Executing command: {args.command}")
    return 0

if __name__ == "__main__":
    exit(main())
