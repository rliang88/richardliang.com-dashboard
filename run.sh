# !/bin/zsh
echo "CMD: "
read command

docker build -t dashboard_image .
docker run -p 5000:5000 --name dashboard_container dashboard_image:latest $command