import os
import json
import csv
import pickle


class ScanDirectory:
    def __init__(self, directory):
        self.directory = directory
        self.result = self.traverse_directory()

    def traverse_directory(self):
        result = []

        for root, dirs, files in os.walk(self.directory):
            current_dir = {
                'name': os.path.basename(root),
                'type': 'directory',
                'size': 0,
                'parent_directory': os.path.dirname(root)
            }

            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                current_dir['size'] += file_size

                result.append({
                    'name': file,
                    'type': 'file',
                    'size': file_size,
                    'parent_directory': os.path.basename(root)
                })

            result.append(current_dir)

        return result

    def save_as_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.result, file, indent=4)

    def save_as_csv(self, filename):
        keys = self.result[0].keys()
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.result)

    def save_as_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.result, file)


my_dir = ScanDirectory("c:\\JavaScript")

my_dir.save_as_json('result.json')
my_dir.save_as_csv('result.csv')
my_dir.save_as_pickle('result.pickle')
