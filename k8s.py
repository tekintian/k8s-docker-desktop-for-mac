#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 使用方法  python k8s.py
import sys
import os

if(len(sys.argv)>1):
    k8s_version = sys.argv[1]
else:
    k8s_version = "v1.19.7"

# 定义需要下载的镜像数组
images=[
    "kube-apiserver:" + k8s_version,
    "kube-controller-manager:" + k8s_version,
    "kube-scheduler:" + k8s_version,
    "kube-proxy:" + k8s_version,
    "pause:3.2",
    "etcd:3.4.13-0",
    "coredns:1.7.0",
    "kubernetes-dashboard-amd64:v1.10.1",
]

# 循环下载镜像并主动更改tag后删除原来的镜像
for i in images:
    pullCMD = "docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/{}".format(i)
    print("run cmd '{}', please wait ...".format(pullCMD))
    os.system(pullCMD)
 
    tagCMD = "docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/{} k8s.gcr.io/{}".format(i, i)
    print("run cmd '{}', please wait ...".format(tagCMD ))
    os.system(tagCMD)
 
    rmiCMD = "docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/{}".format(i)
    print("run cmd '{}', please wait ...".format(rmiCMD ))
    os.system(rmiCMD)