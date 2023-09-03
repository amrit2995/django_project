if grep -q '/docker/' /proc/1/cgroup || grep -q '/lxc/' /proc/1/cgroup; then
  echo "Inside a container"
else
  echo "Not inside a container"
fi