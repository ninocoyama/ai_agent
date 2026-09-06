from functions.get_files_info import schema_get_files_info
from functions.write_files import schema_write_file
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file

available_functions = [
    schema_get_files_info,
    schema_write_file,
    schema_get_file_content,
    schema_run_python_file
]
