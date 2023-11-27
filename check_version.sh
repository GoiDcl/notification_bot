source .env
while true
do
        rm log.log
        wget -O log.log http://webgit.krasrm.com/api/v4/projects/33/repository/files/log.log/raw?token=$GITLAB_TOKEN
        sleep 300
done