#!/bin/bash
uvicorn chatbot:app --host 0.0.0.0 --port $PORT
