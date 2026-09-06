import os
import subprocess
import sys

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.abspath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir is False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_dir) is False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_dir.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_dir, *(args or [])]
        result = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"

        output = []
        if result.stdout.strip():
            output.append(f"STDOUT: {result.stdout.strip()}")
        if result.stderr.strip():
            output.append(f"STDERR: {result.stderr.strip()}")

        return "\n".join(output) if output else "No output produced"

    except Exception as error:
        return f"Error: executing Python file: {error}"