#!/bin/bash


pkill -9 uv
pkill -9 python3

source ./scripts/cpu-governor.sh

./robyn_test.py &

sleep 1

cat >README$(./scripts/cpu.sh | tr ' ' '-').md <<-EOF




Robyn:$(./scripts/cpu.sh)

---


$(./scripts/test.sh)

EOF
