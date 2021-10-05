#1~99のうち、奇数だけ表示
for i in `seq 1 99`;
do
    if [ $((i % 2 )) -ne 0 ];
    then 
        echo $i
    fi
done