'''
sswitch_CLI allows dumping registers value based on name and index.
We have 8192 register instances.
Our key is ETH_SRC,ETH_DST.
The problem is that dumping the (crc32(2)%8192)-th register instance returns always state 0.
Probably the crc32 is not calculated on plain 9-bit field.

This script dumps all the register instances to find the correct index!
NB: launch './run_demo.py', bring down link s3-eth2 and then 'python dump_reg_det.py'
'''

import subprocess
SWITCH_ID = 1
REG_NAME = 'reg_state_red'
INSTANCE_COUNT = 8192
JSON = 'SPIDER_remote.json'

DUMP_ALL = True

if DUMP_ALL:
	non_zero_reg = []
	for i in range(INSTANCE_COUNT):
		cmd = 'echo "register_read '+REG_NAME+' '+str(i)+'" | ~/bmv2/targets/simple_switch/sswitch_CLI '+JSON+' '+str(22222+SWITCH_ID-1)+' | grep '+REG_NAME
		ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		output = ps.communicate()[0]
		reg_state = int(output.split()[-1])
		print 'Trying index',i,': state is',reg_state
		if reg_state!=0:
			print output
			non_zero_reg.append(i)
	print 'non_zero_reg =',non_zero_reg
else:
	i = 5795
	while True:
                cmd = 'echo "register_read '+REG_NAME+' '+str(i)+'" | ~/bmv2/targets/simple_switch/sswitch_CLI '+JSON+' '+str(22222+SWITCH_ID-1)+' | grep '+REG_NAME
	        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	        output = ps.communicate()[0]
	        r=int(output.split()[-1])
	        print output

