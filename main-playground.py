import datetime
import os
import time

import psutil
import requests

if __name__ == "__main__":

    in_meeting = False

    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            process_name = proc.name()
            process_id = proc.pid
            proc_dict = proc.as_dict()

            if process_name == "Microsoft Teams Helper (Renderer)":
                if proc_dict.get("connections"):
                    print(f'\t{len(proc_dict.get("connections"))}')
                    if (
                            len(proc_dict.get("connections")) >= 5
                            and not in_meeting
                    ):
                        print(
                            f"I believe you are in a call/meeting: {datetime.datetime.now().isoformat()}"
                        )
                        in_meeting = True

                        # call the api
                        try:
                            requests.post(
                                "http://onair.local:8000", json=dict(new_state=True)
                            )
                        except Exception as e:
                            print(e)

                    elif len(proc_dict.get("connections")) < 8 and in_meeting:
                        print(
                            f"I believe the call/meeting has ended: "
                            f"{datetime.datetime.now().isoformat()}{os.linesep}"
                        )
                        in_meeting = False

                        # call the api
                        try:
                            requests.post(
                                "http://onair.local:8000", json=dict(new_state=False)
                            )
                        except Exception as e:
                            print(e)

        except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess,
        ):
            pass


