
if [ "$1" == "" ] || [ $# -gt 1 ]; then
        echo "You did not pass the parameter for the container"
        echo "Please pass name of the container as command line parameter"
        exit 0

fi
echo "packaging container..."
docker build -t $1:latest .

echo "Running container..."
docker run $1:latest