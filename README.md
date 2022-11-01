# measurements-service

How to install GO
```
wget https://dl.google.com/go/go1.19.2.linux-amd64.tar.gz
sudo tar -xvf go1.19.2.linux-amd64.tar.gz
sudo mv go /usr/local   → if you get "directory not empty", run the go directory with following commands "cd /usr/local" "rm -R go/" "cd" 
export GOROOT=/usr/local/go
export GOPATH=$HOME/Projects/Proj1
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
go version
```

Install IRTT
```
go install github.com/heistp/irtt/cmd/irtt@latest
```
Run IRTT
```
server: irtt server
client: irtt client -i 10ms -d 1m -l 172 --fill=rand --sfill=rand 10.0.1.1
```
