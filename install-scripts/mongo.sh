#!/bin/bash

paru -S mongodb mongosh-bin mongodb-compass mongodb-tools mingo

sudo systemctl enable mongodb.service