# pairwise-aurora-volume-layer

## 领域

游戏、图形与多媒体

## 主题

极光体积层叠

## 说明

视线相关层厚、云量驱动强度、固定排序键。

初始状态下 `graphics/aurora_volume.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
