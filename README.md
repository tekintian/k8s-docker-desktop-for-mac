# `Docker Desktop for Mac` 开启并使用 `Kubernetes`



2种方式下载k8s镜像

第一种:  

~~~sh
sh k8s.sh  # k8s镜像

sh k8s-admin.sh  # web界面管理工具 镜像  不需要web管理界面可以不下载
~~~



第二种:

~~~sh
sh  load_images.sh
~~~



如果下载后Docker中的k8还是一直启动中, 可能原因是docker中的其他镜像有影响, 将DockerDesktop工具的 的 Troubleshoot --> Reset to factory defaults 将dockerdesktop重置为初始状态,然后重新执行上面的下载工具下载后在到设置中启用 Kubernetes 一般即可解决.





## Docker Engine加速配置

国内的最好设置一下这个加速,否则会非常慢!

~~~json
{
  "debug": true,
  "registry-mirrors": [
    "https://docker.mirrors.ustc.edu.cn",
    "https://registry.docker-cn.com",
    "https://dockerhub.azk8s.cn",
    "https://reg-mirror.qiniu.com",
    "https://hub-mirror.c.163.com"
  ],
  "features": {
    "buildkit": true
  },
  "experimental": false
}
~~~







说明:

- 当前在 `Docker Desktop (Mac) Version v20.10.5 Channel: edge (Kubernetes: v1.19.7)`上经过测试可用
  - [Docker Desktop for Mac Edge release notes](https://docs.docker.com/docker-for-mac/edge-release-notes/)
- 使用 `Kubeadm` 在`Ubuntu`上安装 `Kubernetes` 请查看 [kubernetes-for-china](https://github.com/maguowei/kubernetes-for-china)



查看最新镜像版本

https://hub.docker.com/u/gotok8s



## 安装并启动

1. 下载安装 [Docker Desktop (Mac) Channel: edge](https://download.docker.com/mac/edge/Docker.dmg)

2. 设置 `Docker` 镜像加速, 这里使用 微软 `Azure` 的镜像服务，也可以选择其他的镜像加速服务。 [Azure Container Registry Proxy](https://github.com/Azure/container-service-for-azure-china/blob/master/aks/README.md#22-container-registry-proxy) ```https://dockerhub.azk8s.cn```

![mirror](./image/mirror.png)

3. 从 `Docker Hub` 的同步仓库中取回，并重新打上原始的`tag`.

```bash
./load_images.sh
```

4. 在`Docker for Mac` 设置中启用 `Kubernetes` 选项, 并等待一会儿，直到 `Kubernetes` 开始运行。

![k8s](./image/k8s.png)

5. 可选的步骤: 切换`Kubernetes`运行上下文至 `docker-desktop`

```bash
# 一般只有在之前用其他方式运行过Kubernetes才需要
$ kubectl config use-context docker-desktop
```

6. 验证 `Kubernetes` 集群状态

```bash
$ kubectl cluster-info
$ kubectl get nodes
$ kubectl describe node
```

## 参考

- [部署 Kubernetes Dashboard](https://github.com/maguowei/k8s-cookbook#%E9%83%A8%E7%BD%B2-kubernetes-dashboard)
- [Helm 的使用](https://github.com/maguowei/k8s-cookbook#helm)
