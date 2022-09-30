#!/usr/bin/env python3

import os
import json

env = {}

for env_key, env_value in os.environ.items():
    env[env_key] = env_value

print("Content-Type: application/json")
print()

print(json.dumps(env, indent=2))

# cited:
# d01 lab recording
# https://ualberta-ca.zoom.us/rec/play/e1JU2sW0pErgKNN-PQzHTfWeinxg4zAZoFqGMsuj2uGaMJPhJoW75ek7pli-4a2eOt9uZVGLTKXq6E8U.qiwwOmSFexMCzWYY
# https://drive.google.com/drive/folders/1UxS4CfqsTFRde2iWYbdqP9tV6XYVaw6u
