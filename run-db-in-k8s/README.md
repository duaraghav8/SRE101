## Run a production Database in K8s

This is the code & commands I used in my video on running the MySQL cluster in K8s.

1. Spin up a new Linux VM
2. Install `minikube` & `kubectl`
3. Run `setup.sh`
4. Follow the video & apply the configurations. Or take the shortcut by running `run-mysql-cluster.sh`.
5. Play around! The `db-queries.sh` file has the read and write requests.
6. Optionally run `cleanup.sh` to get a clean slate
