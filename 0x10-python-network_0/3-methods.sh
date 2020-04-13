#!/bin/bash
#
curl -sX OPTIONS "$1" -I | grep "Allow" | cut -d ' ' -f2-
