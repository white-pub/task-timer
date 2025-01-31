"""
__main__.py
Anna Chen
2025-01-30
 
This file contains the main functions.
Now it only has the "say hello" print statment.
More functions will be added later.
"""
import click
 
@click.command()
def main():
    """This is my main cli."""
 
    click.echo("Hello World")
# def main():
#     print("Hello from task-timer!")
 
if __name__ == '__main__':
    main()