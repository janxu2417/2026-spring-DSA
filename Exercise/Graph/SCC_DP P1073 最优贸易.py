import sys
from collections import deque

## -----tarjan_scc 手动栈---------
def tarjan_scc(graph):
    n = len(graph)
    dfn = [-1] * n
    low = [-1] * n
    in_stack = [False] * n
    stack = []
    sccs = []
    timer = 0
    # 核心：使用迭代器数组来保存每个节点的邻接表遍历进度
    iters = [None] * n
    # 初始节点入“模拟系统栈”
    dfn[1] = low[1] = timer
    timer += 1
    stack.append(1)  # 用于维护 SCC 集合的栈
    in_stack[1] = True
    iters[1] = iter(graph[1])

    call_stack = [1]  # 模拟系统调用的栈

    while call_stack:
        u = call_stack[-1]

        # 使用迭代器接着上一次中断的地方继续遍历邻接节点
        for v in iters[u]:
            if dfn[v] == -1:
                # 发现未访问节点，准备“向下递归”
                dfn[v] = low[v] = timer
                timer += 1
                stack.append(v)
                in_stack[v] = True
                iters[v] = iter(graph[v])

                # 将 v 压入模拟调用栈，并 break 暂停 u 的循环
                call_stack.append(v)
                break
            elif in_stack[v]:
                # 处理返祖边
                low[u] = min(low[u], dfn[v])
        else:
            # 只有当 for 循环正常结束（没有被 break 打断），才会执行 else 分支
            # 这意味着 u 的所有邻居都已经处理完毕，准备“向上回溯”
            call_stack.pop()

            # 用子树 u 的 low 值更新父节点 p 的 low 值
            if call_stack:
                p = call_stack[-1]
                low[p] = min(low[p], low[u])

            # 判断并提取一个强连通分量 (SCC)
            if low[u] == dfn[u]:
                scc = []
                while True:
                    v = stack.pop()
                    in_stack[v] = False
                    scc.append(v)
                    if u == v:
                        break
                sccs.append(scc)

    return sccs

def main():
    it = iter(sys.stdin.read().split())
    n, m = int(next(it)), int(next(it))
    prices = [-1]
    for _ in range(n):
        prices.append(int(next(it)))
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v ,tp = int(next(it)), int(next(it)), int(next(it))
        graph[u].append(v)
        if tp == 2:
            graph[v].append(u)

    sccs = tarjan_scc(graph)
    # -------build dag--------
    num_scc = len(sccs)
    mn_cost = [200] * num_scc
    mx_cost = [-1] * num_scc
    scc_id = [-1] * (n + 1)
    for i, scc in enumerate(sccs):
        for node in scc:
            scc_id[node] = i
            mn_cost[i] = min(mn_cost[i], prices[node])
            mx_cost[i] = max(mx_cost[i], prices[node])
    dag = [set() for _ in range(num_scc)]
    in_deg = [0] * num_scc
    for u in range(1, n + 1):
        uid = scc_id[u]
        if uid == -1: continue
        for v in graph[u]:
            vid = scc_id[v]
            if vid != -1 and uid != vid and vid not in dag[uid]:  # 去重判断
                dag[uid].add(vid)
                in_deg[vid] += 1
    # --------------------
    dp = [0] * num_scc
    q = deque([scc_id[1]])
    for i in range(num_scc):
        dp[i] = mx_cost[i] - mn_cost[i]
    while q:
        node = q.popleft()
        for v in list(dag[node]):
            in_deg[v] -= 1
            if mn_cost[v] > mn_cost[node]:
                mn_cost[v] = mn_cost[node]
            if dp[node] > dp[v]:
                dp[v] = dp[node]
            if dp[v] < mx_cost[v] - mn_cost[v]:
                dp[v] = mx_cost[v] - mn_cost[v]
            if in_deg[v] == 0:
                q.append(v)

    print(dp[scc_id[n]])

if __name__ == '__main__':
    main()