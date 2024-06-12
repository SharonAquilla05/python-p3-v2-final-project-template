import click
from models import User, Task, Category, Database

# Initialize database
Database()

@click.group()
def cli():
    """Command Line Interface for managing users, categories, and tasks."""
    pass

@click.command()
def add_user():
    """Add a new user to the system."""
    username = click.prompt("Input your username", type=str)
    User.create(username)
    click.echo(f"User {username} added successfully")

@click.command()
def list_users():
    """List all users."""
    users = User.get_all()
    if not users:
        click.echo("No users found.")
    else:
        for user in users:
            click.echo(f"ID: {user[0]}, Name: {user[1]}")

@click.command()
def add_category():
    """Add a new category."""
    category_name = click.prompt("Enter category name", type=str)
    Category.create(category_name)
    click.echo(f"Category {category_name} added successfully")

@click.command()
def list_categories():
    """List all categories."""
    categories = Category.get_all()
    if not categories:
        click.echo("No categories found.")
    else:
        for category in categories:
            click.echo(f"ID: {category[0]}, Name: {category[1]}")

@click.command()
def add_task():
    """Add a new task."""
    user_id = click.prompt("Enter user ID", type=int)
    category_id = click.prompt("Enter category ID", type=int)
    task_title = click.prompt("Enter task title", type=str)
    Task.create(task_title, user_id, category_id)
    click.echo(f"Task {task_title} added successfully")

@click.command()
def list_tasks():
    """List all tasks."""
    tasks = Task.get_all()
    if not tasks:
        click.echo("No tasks found.")
    else:
        for task in tasks:
            click.echo(f"ID: {task[0]}, Title: {task[1]}, User ID: {task[2]}, Category ID: {task[3]}")

@click.command()
def delete_user():
    """Delete a user by ID."""
    user_id = click.prompt("Enter user ID to delete", type=int)
    User.delete(user_id)
    click.echo(f"User ID {user_id} deleted successfully")

@click.command()
def delete_category():
    """Delete a category by ID."""
    category_id = click.prompt("Enter category ID to delete", type=int)
    Category.delete(category_id)
    click.echo(f"Category ID {category_id} deleted successfully")

@click.command()
def delete_task():
    """Delete a task by ID."""
    task_id = click.prompt("Enter task ID to delete", type=int)
    Task.delete(task_id)
    click.echo(f"Task ID {task_id} deleted successfully")

cli.add_command(add_user)
cli.add_command(list_users)
cli.add_command(add_category)
cli.add_command(list_categories)
cli.add_command(add_task)
cli.add_command(list_tasks)
cli.add_command(delete_user)
cli.add_command(delete_category)
cli.add_command(delete_task)

if __name__ == '__main__':
    cli()
