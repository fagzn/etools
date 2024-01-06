# alfred-tik-wolai
任务计数器. 通过 alfred 链接 wolai 数据表格使用,可以记录事项的执行次数. 使用该工具可以很方便的计算自己每件事每天做了几次，比如,喝水记录,运动记录等等, 数据流转到wolai表格中，可以很方便地进行各种维度的分析统计。


## 目录介绍
```text
.
├── LICENSE
├── README.md
├── Tik-Alfred-Wolai.alfredworkflow      //  alfred 安装文件
└── src                                  //  脚本
    ├── tik-alfred-wolai-read.py         //  读取 wolai 数据表格信息脚本
    └── tik-alfred-wolai.py              //  添加 wolai 数据表格信息脚本

```

## quickstart
1. 本应用是链接 alfred 和 wolai 两个工具实现的任务计数器, 相信大家是带着需求找到本项目的,所以应该都有这两个工具
1. 创建 wolai 应用和申请 token 请查看 wolai [官方文档](https://www.wolai.com/wolai/7FB9PLeqZ1ni9FfD11WuUi).获取 token 后备用
2. 创建 wolai 数据表格, 需要保持数据表格字段和[标准表格](https://www.wolai.com/fagzn/rjqSQXQc9tgVHPsqbQY5ta)保持一致.然后获取表格的 id 备用, [表格id获取办法](https://www.wolai.com/wolai/2kRSq4mVwxCUUcUhrgnQgp).
1. 将项目中根目录的`.alfredworkflow`后缀文件是安装文件,将它拖入 alfredworkflow 中安装.
2. 应用设置页面填入 `token` 和 `表格id` 即可使用.