#!/bin/bash

echo "#########################################"
echo "Installing QtumJS"
npm install

echo "#########################################"
echo "fetching data of task id" $1
mkdir data
cd data
wget http://127.0.0.1:8000/files/$1.zip

echo "#########################################"
echo "unzipping file" $1.zip
unzip ./$1.zip
rm $1.zip
cd $1
filename="cmd.txt"

input="cmd.txt"
while IFS= read -r var
do
echo "#########################################"
echo "exectuing command - $var"
$var
done < "$input"

echo "#########################################"
cd ..
pwd
ls -la
zip -r $1.zip $1

echo "#########################################"
echo "Uploading results"
cp $1.zip ../../Api/results


echo "#########################################"
echo "initiating transaction"

cd ..
node compute.js $2

echo "#########################################"
echo "end "

rm -r data


