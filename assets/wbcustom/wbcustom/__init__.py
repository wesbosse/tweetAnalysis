def hello():
    print('hello')


# import os, json, shutil
#
#

# class NotebookManipulator:
#
#     def __init__(self, student_filename=False, ):
#
#         self.solution = self.parse_notebook(student_filename, solutions=True)
#         self.submission = self.parse_notebook()
#
#     @staticmethod
#     def parse_notebook(self, filename=False, solutions=False):
#
#         try:
#             with open(filename, "r") as fp:
#                 if solutions:
#                     return json.load(fp)
#                 else:
#                     return json.load(fp)
#         except:
#             assert "Could not open ", filename
#
#     @staticmethod
#     def get_cell_contents(self, notebook, source_only=True, source_type='code'):
#
#         cells = [cell for cell in notebook['cells'] if cell['cell_type'] == source_type]
#
#         if source_only:
#             return [r for v in [cell['source'] for cell in cells] for r in v]
#         else:
#             return cells
#
#     def generate_file(self, notebook, file_type='code', destination='./temp'):
#
#         content = self.get_cell_contents(notebook, source_type=file_type)
#
#         extension = 'py' if file_type == 'code' else 'md'
#         name = 'src' if notebook == self.solution else 'sub'
#
#         with open(f"{destination}/{name}.{extension}", "w+") as file:
#             for line in content:
#                 file.write(line)
#
#     def check_plagiarism(self, file_dir='./temp'):
#         try:
#             shutil.rmtree(file_dir)
#         except:
#             pass
#
#         os.mkdir('temp')
#
#         for notebook in (self.solution_notebook, self.submission_notebook):
#             for file_type in ('code', 'markdown'):
#                 self.generate_file(notebook, file_type)
#
#         for file_pair in [(f'{file_dir}/src.py', f'{file_dir}/sub.py'), (f'{file_dir}/src.md', f'{file_dir}/sub.md')]:
#             with open(file_pair[0], 'r') as file1, open(file_pair[1], 'r') as file2:
#                 label = file_pair[0][-2:]
#                 similar_lines = set(file1).intersection(file2)
#                 print(file_pair[0][-2:], len(similar_lines))