# pyOnAir

Trigger an on air light (via GPIO) when REST api is called



## work machine
1. Sends a REST POST request to the onair machine to enable/disable the light; which is hosting a REST api via FastAPI and uvicorn
    `https://onair.local:8000`
  sample body: `{"new_state": true}`

  - a GET to the same root path will return the current onair state

### how to setup work machine monitoring as a service
1. Replace `<your_username>` with the username in your local machine.
2. Correct the path to this repository (lines 13 and 20)
3. Ensure the std. out and std. error directories in lines 16 and 18 exist
  Notes: For StandardOutPath and StandardErrorPath in the .plist, you can use whatever path you want, but please remember to make sure that the paths exist and your user has enough permissions to modify their contents.

#### Make sync_zshrc run as a background service
1. Copy com.<username>.auto-sync-zshrc.plist to ~/Library/LaunchAgents/:

   `cp com.<username>.auto-sync-zshrc.plist ~/Library/LaunchAgents/`
1. Navigate to ~/Library/LaunchAgents/ and start the service:
 
   `launchctl load com.<username>.auto-sync-zshrc.plist`
1. If you get Load failed: 5: Input/output error, please check if the .plist file is in the correct format, and you are in the right directory.
You can check files at StandardErrorPath and StandardOutPath to debug if there is anything wrong. In that case, you could use LaunchControl for easier debugging. You can install it using Homebrew:
 
   `brew install --cask launchcontrol`

## api machine/lights controller

`sudo apt install python3-rpi.gpio`

https://sourceforge.net/p/raspberry-gpio-python/wiki/install/

`export GPIOZERO_PIN_FACTORY=rpigpio`

- add a call to the start_api.sh script to the /etc/rc.local file to run it at startup
  -  `/home/jet/pyOnAir/api/start_api.sh &`
  - the `&` at the end indicates it should be run in a separate process
  - [startup methods](https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/all)

#### FastAPI
##### for testing and development
Docker *could* be used if desired (FastAPI wouldn't run on my Windows machine)

- to make the API accessible on the network the host command has to be added
  `uvicorn main:app --reload --host 0.0.0.0`