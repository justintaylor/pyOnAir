import getpass
import subprocess

USER_NAME = getpass.getuser()

SCRIPT_NAME = "auto-start-pyOnAir"

WORK_MACHINE_DIRECTORY = "/git/pyOnAir/work_machine"

PLIST_FILE = f"com.{USER_NAME}.{SCRIPT_NAME}.plist"

LAUNCH_AGENTS_DIR = f"/Users/{USER_NAME}/Library/LaunchAgents"

XML = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.{USER_NAME}.{SCRIPT_NAME}</string>
        <key>ServiceDescription</key>
        <string>Auto start monitoring for meeting</string>
        <key>ProgramArguments</key>
        <array>
            <string>/Users/{USER_NAME}{WORK_MACHINE_DIRECTORY}/watch_for_meetings.sh</string>
        </array>
        <key>StandardOutPath</key>
        <string>/Users/{USER_NAME}/tmp/{SCRIPT_NAME}.stdout.log</string>
        <key>StandardErrorPath</key>
        <string>/Users/{USER_NAME}/tmp/{SCRIPT_NAME}.stderr.log</string>
        <key>WorkingDirectory</key>
        <string>/Users/{USER_NAME}{WORK_MACHINE_DIRECTORY}</string>
        <key>KeepAlive</key>
        <true/>
     </dict>
  </plist>
  """


with open(file=f'{LAUNCH_AGENTS_DIR}/{PLIST_FILE}', mode='w') as plist:
    plist.write(XML)


subprocess.run(["launchctl", "load", f'{LAUNCH_AGENTS_DIR}/{PLIST_FILE}'])
