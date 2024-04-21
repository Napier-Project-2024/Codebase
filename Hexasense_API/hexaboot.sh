#!/bin/bash

cd home/team-member/Codebase/Experiments/fastapi && python -m uvicorn main:app --host 0.0.0.0 --port 5000 --reload

