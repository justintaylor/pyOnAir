#!/bin/bash

source ../../venvs/pyOnAirApi/bin/activate
uvicorn main:app --host 0.0.0.0 --workers 2 > uvicorn.log
