#!/bin/bash
#
curl -sI "$1" | grep "Content-Length:" | sed 's/[^0-9]//g'
