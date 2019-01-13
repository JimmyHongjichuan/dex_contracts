rm new.txt
rm get.txt
cat abi.txt | tr "\n" " "| tr " *" " " >> get.txt
sed  's/ *//g'   get.txt>>new.txt

