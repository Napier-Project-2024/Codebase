#!/bin/bash

cd /usr/Hexasense_API && python -m uvicorn main:app --host 0.0.0.0 --port 5000 --reload

