#!/bin/bash

source /home/jet/.bashrc
. /home/jet/venvs/pyOnAirApi/bin/activate
cd /home/jet/pyOnAir/api/
uvicorn main:app --host 0.0.0.0 --workers 2