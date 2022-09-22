#!/bin/bash
# Bash script that takes a URL, sends a request, display and returns the size of the body
curl -w '%{size_download}\n' -so /dev/null $1
