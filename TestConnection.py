from commonvm import core

# Note: Initial Routines for Testing
#       Replace with Pytest


print("Starting 'TestConnection.py'...");


core.getAccessToken();
core.getAccessToken(); # if the LRU cache works, the env vars should only be printed out once

print("Program terminated.");
