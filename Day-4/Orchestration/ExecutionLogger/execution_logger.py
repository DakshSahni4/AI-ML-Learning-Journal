import os
import json

from dataclasses import asdict


class ExecutionLogger:

    def __init__(self):

        self.file_path = os.path.join(
            os.path.dirname(__file__),
            "execution_logs.json"
        )

        if not os.path.exists(self.file_path):

            with open(self.file_path, "w") as file:
                json.dump([], file, indent=4)

    def log(self, execution_log):

        try:

            with open(self.file_path, "r") as file:
                logs = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):

            logs = []

        logs.append(asdict(execution_log))

        with open(self.file_path, "w") as file:
            json.dump(logs, file, indent=4)

    def getAllLogs(self):

        try:

            with open(self.file_path, "r") as file:
                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):

            return []

    def filterByProvider(self, provider):

        logs = self.getAllLogs()

        return [
            log
            for log in logs
            if log["provider"].lower() == provider.lower()
        ]

    def filterByStatus(self, success):

        logs = self.getAllLogs()

        return [
            log
            for log in logs
            if log["success"] == success
        ]

    def filterByDate(self, date):

        logs = self.getAllLogs()

        return [
            log
            for log in logs
            if log["timestamp"].startswith(date)
        ]