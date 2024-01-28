# alfred-task-tik
通过 alfred 动态记录每个任务的耗时情况,随时开始,暂停,结束.并讲数据记录在 wolai 文档中


## 使用方法
`tasktime {task-name}`: 
- 如果任务存在,则会展示任务状态, 回车是开启或暂停计时
- 如果task-name 不存在, 回车可以创建一个任务并开始计时

`tasktime `: 展示所有任务

`⌘`: 复制指定任务信息

`⇧+⌘`: 删除指定任务

`tasktime clean`: 清理所有任务




## TODOLIST
- [ ] fix:修复文件已经清空,但是缓存还有的问题
- [ ] doc: readme 补全