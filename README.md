# Python-Editor-with-Kubernets


1. docker build -t pythonexecutor . --network host

2. docker run -p 5000:5000 -v $(pwd)/:/app pythonexecutor