import click
import shutil
import psutil as psutil

from utils.json_commands import add_key_value_to_json, remove_key_from_json, json_save_one, json_upload_key


@click.group()
def analyze_system_cli():
    pass


@click.command(name='del_command', help='Name commands, replace space on _')
@click.argument('key')
def delete_command(key):
    remove_key_from_json(key)
    click.echo(f'Command {key} been delete')


@click.command(name='add_command')
@click.option("--key", "-k", required=True, help="Name command, replace space on _")
@click.option("--value", "-v", required=True, help="File name in data_files folder")
def add_command(key, value):
    add_key_value_to_json(key, value)
    click.echo(f'Command {key} with file {value} been added')


@click.command(name='add_file', help='Path to folder that been added')
@click.argument('path')
def copy_file_to_folder(path):
    shutil.copy2(path, './data_files')
    click.echo(f'File {path} been add')

@click.command(name='start_system')
def system_start():
    process = psutil.Popen(['D:\Programs\Python 3.11\python', 'start_system.py'])
    json_save_one(process.ppid(), 'ppid')
    print('System running')

@click.command(name='stop_system')
def system_stop():
    for process in psutil.process_iter():
        if process.ppid() == json_upload_key('ppid'):
            process.kill()
            print("System stopped")
            json_save_one(-1, 'ppid')
            break
    else:
        json_save_one(-1, 'ppid')
        print("System is not running")


analyze_system_cli.add_command(delete_command)
analyze_system_cli.add_command(add_command)
analyze_system_cli.add_command(copy_file_to_folder)
analyze_system_cli.add_command(system_start)
analyze_system_cli.add_command(system_stop)

if __name__ == '__main__':
    analyze_system_cli()
