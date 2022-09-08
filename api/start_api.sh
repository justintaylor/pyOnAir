#!/bin/bash

source ../../venvs/pyOnAirApi/activate
uvicorn main:app --host 0.0.0.0 --workers 2
