#!/bin/sh
#模拟器运行NDP协议组合模型，设置相关参数
../../datacenter/htsim_ndp_permutation -o logfile -strat perm -conns 432 -nodes 432 -cwnd 23 -q 8 > debugout
#运行程序将参数存于日志中
python process_data.py logfile
#模拟器运行DCTCP协议组合模型，设置相关参数
../../datacenter/htsim_dctcp_permutation -o dctcp_logfile -nodes 432 -conns 432 -ssthresh 15 -q 100 > debug_dctcp
#运行程序将参数存于日志中
python process_dctcp_data.py dctcp_logfile
#模拟器运行TCP协议组合模型，设置相关参数
../../datacenter/htsim_tcp_permutation -o mptcp_logfile -nodes 432 -conns 432 -ssthresh 15 -q 100 -sub 8 > debug_mptcp
#运行程序将参数存于日志中
python process_mptcp_data.py mptcp_logfile
#根据permutation.plot设定的日志里的参数画图
gnuplot permutation.plot
