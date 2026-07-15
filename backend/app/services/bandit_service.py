import subprocess
import json


class BanditService:

    @staticmethod
    def analyze(file_path):
        try:
            result = subprocess.run(
                [
                    "bandit",
                    "-f",
                    "json",
                    file_path
                ],
                capture_output=True,
                text=True
            )

            if result.stdout.strip():
                return json.loads(result.stdout)

            return {}

        except Exception as e:
            return {
                "error": str(e)
            }