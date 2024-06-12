import click
from models import User, Task, Category

@click.group()
def cli():
    """Task Management CLI"""
    pass

@cli.group()
def user():
    """Commands related to users"""
    pass

@user.command()
def create():
    name = click.prompt("Enter user name", type=str)
    user = User(name)
    user.save()
    click.echo(f"User '{name}' created successfully")

@user.command()
def delete():
    user_id = click.prompt("Enter user ID to delete", type=int)
    User.delete(user_id)
    click.echo(f"User with ID {user_id} deleted successfully")

@user.command()
def list():
    users = User.get_all()
    for user in users:
        click.echo(f"{user[0]}: {user[1]}")

@user.command()
def find():
    user_id = click.prompt("Enter user ID to find", type=int)
    user = User.find_by_id(user_id)
    if user:
        click.echo(f"User: {user[1]}")
    else:
        click.echo("User not found")

@cli.group()
def category():
    """Commands related to categories"""
    pass

@category.command()
def create():
    name = click.prompt("Enter category name", type=str)
    category = Category(name)
    category.save()
    click.echo(f"Category '{name}' created successfully")

@category.command()
def delete():
    category_id = click.prompt("Enter category ID to delete", type=int)
    Category.delete(category_id)
    click.echo(f"Category with ID {category_id} deleted successfully")

@category.command()
def list():
    categories = Category.get_all()
    for category in categories:
        click.echo(f"{category[0]}: {category[1]}")

@category.command()
def find():
    category_id = click.prompt("Enter category ID to find", type=int)
    category = Category.find_by_id(category_id)
    if category:
        click.echo(f"Category: {category[1]}")
    else:
        click.echo("Category not found")

@cli.group()
def task():
    """Commands related to tasks"""
    pass

@task.command()
def create():
    title = click.prompt("Enter task title", type=str)
    user_id = click.prompt("Enter user ID", type=int)
    category_id = click.prompt("Enter category ID", type=int)
    task = Task(title, user_id, category_id)
    task.save()
    click.echo(f"Task '{title}' created successfully")

@task.command()
def delete():
    task_id = click.prompt("Enter task ID to delete", type=int)
    Task.delete(task_id)
    click.echo(f"Task with ID {task_id} deleted successfully")

@task.command()
def list():
    tasks = Task.get_all()
    for task in tasks:
        click.echo(f"{task[0]}: {task[1]} (User ID: {task[2]}, Category ID: {task[3]})")

@task.command()
def find():
    task_id = click.prompt("Enter task ID to find", type=int)
    task = Task.find_by_id(task_id)
    if task:
        click.echo(f"Task: {task[1]} (User ID: {task[2]}, Category ID: {task[3]})")
    else:
        click.echo("Task not found")

@task.command()
def find_by_user():
    user_id = click.prompt("Enter user ID to find tasks for", type=int)
    tasks = Task.find_by_user(user_id)
    for task in tasks:
        click.echo(f"{task[0]}: {task[1]} (Category ID: {task[3]})")

if __name__ == '__main__':
    cli()



