#操作命令合集
#1.Rabbitmq查询队列数
rabbitmqctl list_queues -p /prd  name messages_ready |grep 队列名

#2.Centos6.5系统改变分区inode数量
umount /ReportFile
mkfs.ext4 /dev/mapper/rootvg-lv_reportfile -N 131072000
mount /dev/rootvg/lv_reportfile /ReportFile

#git命令
git status  查看状态
git add  文件或者文件目录
git commit 提交版本库