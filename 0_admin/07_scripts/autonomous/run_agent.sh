#!/bin/bash
cd /home/ian/NEUROMANCER/0_admin/07_scripts/autonomous
source venv/bin/activate
python3 neuromancer_autonomous.py > /dev/null 2>&1
