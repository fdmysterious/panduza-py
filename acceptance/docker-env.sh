

docker build -t pza_test .


docker run \
    -v $PWD:/panduza-py \
    --user $(id -u):$(id -g)\
    -it pza_test bash

