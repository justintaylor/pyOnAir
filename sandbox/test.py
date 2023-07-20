import json

import psutil

if __name__ == '__main__':
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            process_name = proc.name()
            process_id = proc.pid
            proc_dict = proc.as_dict()

            match process_name:
                case "Microsoft Teams":
                    print('Teams')
                    print(f"\t{json.dumps(proc_dict['connections'])}")
                    # TODO would types of connections help?

                case "zoom.us":
                    print('zoom')
                    print(f"\t{json.dumps(proc_dict['connections'])}")
                    # TODO would types of connections help?

        except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess,
        ):
            pass
