# Networking with Docker

The official [`docker network` documentation](https://docs.docker.com/network/#docker-ee-networking-features)
provides very good introduction.

Quick tip: Default bridge networks are
[not the best](https://docs.docker.com/network/network-tutorial-standalone/)
for production systems. Instead, use user-defined bridge networks. It appears
that on user-defined networks, docker can resolve a container name to the IP
address; this is called __automatic service discovery__.

Excellent [tutorial](https://docs.docker.com/network/network-tutorial-standalone/) on docker
networking, which contains hands-on commands that you can try yourself. This is very useful.

## Links
These additional links might come in handy.
- [macos - Who is listening on a given TCP port on Mac OS X? - Stack Overflow](https://stackoverflow.com/questions/4421633/who-is-listening-on-a-given-tcp-port-on-mac-os-x)
