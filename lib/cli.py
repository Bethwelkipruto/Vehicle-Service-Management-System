#!/usr/bin/env python3
"""
Vehicle Service Management System CLI
Main entry point for the application
"""

from helpers import run

def main():
    """Main function to run the CLI application"""
    print('\n' + '='*50)
    print('   VEHICLE SERVICE MANAGEMENT SYSTEM')
    print('='*50)
    print('Welcome! Manage customers, vehicles, and services.')
    
    try:
        run()
    except KeyboardInterrupt:
        print('\n\nOperation cancelled by user.')
    except Exception as e:
        print(f'\nAn error occurred: {e}')
    finally:
        print('\nThank you for using Vehicle Service Management System!')
        print('Goodbye!')

if __name__ == '__main__':
    main()