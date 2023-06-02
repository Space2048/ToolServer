version=$1
platform=$2
packageName=$1"_"$2".zip"
jumpDir="/isekai2_upload/"

echo "sendFrom 124.156.139.110"
echo "[SENDPACKAGE] |"${packageName}"| DATE |"`date`"|" >> client_package.log
rsync --progress -e 'ssh  -oStrictHostKeyChecking=no -i ~/.ssh/id_rsa' ${packageName} root@35.194.91.23:${jumpDir};
ssh root@35.194.91.23 "cd ${jumpDir}; sh sendPackage.sh $1 $2"
