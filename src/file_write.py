import json
import os
from pathlib import Path


class FileWrite:
    def __init__(self):
        self.file_all_list = 'all_domains.json'
        self.file_selected_list = 'selected_domains.json'
        self.save_dir = Path(__file__).resolve().parent.parent / 'out'

    def update_to_all(self, domain):
        file_name = self.save_dir / self.file_all_list

        self.update_file(domain, file_name)

    def update_to_selected(self, domain):
        file_name = self.save_dir / self.file_selected_list

        self.update_file(domain, file_name)

    def update_file(self, domain, file_name):
        if not os.path.isdir(self.save_dir):
            os.mkdir(self.save_dir)

        if not os.path.isfile(file_name):
            with open(file_name, 'w') as f:
                f.write('[]')

        with open(file_name, 'r') as f:
            file_data = f.read()

            if file_data == '':
                print(123)
                file_data = '[]'

        with open(file_name, 'w') as f:
            to_update = json.loads(file_data)

            to_update.append(domain)

            print(to_update)

            json.dump(to_update, f, indent=4)
