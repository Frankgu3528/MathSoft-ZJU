#!/bin/bash
arr=(21 34 45 213 44)
echo "你的数组是：${arr[*]}"
#定义数组前一个元素
for ((i=0;i<${#arr[*]};i++))
do
  #定义数组后一个元素
  for ((a=$i+1;a<${#arr[*]};a++))
  do
#条件判断，如果前一个元素大于后一个元素，就交换位置，否则下一次循环
  if [ ${arr[$i]} -gt ${arr[$a]} ];then
    temp=${arr[$i]}
    arr[$i]=${arr[$a]}
    arr[$a]=$temp
  fi
  done
done
echo "你的数组升序排列为：${arr[*]}"