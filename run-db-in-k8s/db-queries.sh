#!/bin/bash

kubectl run mysql-client --image=mysql:5.7 -i --rm --restart=Never --\
  mysql -h mysql-0.mysql <<EOF
CREATE DATABASE hello;
CREATE TABLE hello.messages (message VARCHAR(250));
INSERT INTO hello.messages VALUES ('hello world!');
EOF

kubectl run mysql-client --image=mysql:5.7 -i -t --rm --restart=Never --\
  mysql -h mysql-read -e "SELECT * FROM hello.messages"
