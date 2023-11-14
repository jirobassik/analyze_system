from analyze.matcher import Matcher
from analyze.normalize import Normalize
from utils.file_usage import FileUsage
from analyze.error import MatchError


class Commands:
    def __init__(self, command):
        self.file_util = FileUsage('./compositions')
        self.data_file_util = FileUsage('./data_files')
        self.command = Normalize(command)()
        self.commands = {'commands': self.list_commands,
                         'literature definition': self.literature,
                         'known russian literature': self.known_russian_literature,
                         'known english literature': self.known_english_literature,
                         'literature genre': self.literature_genres,
                         'system list composition': self.list_composition} | \
                        {f'print {file_name}': FileDataRead(file_name, self.data_file) for file_name in
                         self.file_util.get_file_names()}

    def found_command(self):
        for name_com, com in self.commands.items():
            if Matcher(a=self.command, b=name_com).match():
                return name_com, com()
        raise MatchError('Command not found')

    def list_commands(self):
        commands = ''
        for name_com in self.commands.keys():
            commands += f"Command name: {name_com}\n"
        return commands

    def literature(self):
        return self.data_file_util.read_file('literature_def')

    def known_russian_literature(self):
        return self.data_file_util.read_file('known_rus_lit')

    def known_english_literature(self):
        return self.data_file_util.read_file('known_eng_lit')

    def literature_genres(self):
        return self.data_file_util.read_file('literature_gen')

    def list_composition(self):
        file_names = self.file_util.get_file_names()
        return ', '.join(file_names)

    def data_file(self, file_name):
        return self.file_util.read_file(file_name)


class FileDataRead:
    def __init__(self, file_name: str, read_meth):
        self.read_meth = read_meth
        self.file_name = file_name

    def __call__(self, *args, **kwargs):
        return self.read_meth(self.file_name)
