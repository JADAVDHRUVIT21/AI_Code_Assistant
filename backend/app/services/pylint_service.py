import subprocess
import json


class PylintService:

    @staticmethod
    def analyze(file_path):
        try:
            result = subprocess.run(
                [
                    "pylint",
                    file_path,
                    "--output-format=json"
                ],
                capture_output=True,
                text=True
            )

            if result.stdout.strip():
                return json.loads(result.stdout)

            return []

        except Exception as e:
            return {
                "error": str(e)
            }