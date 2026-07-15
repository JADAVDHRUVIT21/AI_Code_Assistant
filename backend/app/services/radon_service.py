import subprocess


class RadonService:

    @staticmethod
    def analyze(file_path):
        try:
            result = subprocess.run(
                [
                    "radon",
                    "cc",
                    file_path,
                    "-j"
                ],
                capture_output=True,
                text=True
            )

            return result.stdout

        except Exception as e:
            return str(e)