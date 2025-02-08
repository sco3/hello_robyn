#!/usr/bin/env -S v run

import time

if execute('lsof -i:8000').exit_code == 0 {
	println('Port 8000 is in use. Stop process.')
	exit(1)
}

execute('sudo cpupower frequency-set --governor performance')
gov := execute('cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor').output.replace('\n','')
cpu := execute("cat /proc/cpuinfo | grep 'model name' | sort -u | awk -F':' '{print $2}'").output.replace('\n','')
cpu_minus := cpu.replace_char(` `, `-`, 1).trim_space()

mut proc := new_process('./.venv/bin/python3')
proc.args = ['robyn_test.py']
proc.run()
println('Started: ${proc.filename} ${proc.args} pid: ${proc.pid}')

time.sleep(time.millisecond * 1100)

mut output := execute('wrk http://127.0.0.1:8000 -d 10 -t 2 -c 200').output


proc.signal_term()
proc.signal_kill()
println('Process: ${proc.pid} ${proc.status}')

output='
Robyn: ${cpu} - cpu governor: ${gov}
===
```
${output}
```
'
println('${output}')
write_file('README${cpu_minus}.md', output)!
