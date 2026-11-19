# 相机测光：EV、亮度与百分位

HDR 相机自动曝光忽明忽暗、点测光不居中：EV 没有按 2 的幂，亮度权重错，百分位没有累计到目标，中心权重没有按半径衰减，平滑没有按速度，空直方图崩，批量测光只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
render/__init__.py
render/exposure.py
tests/test_exposure.py
```

## 当前状态

`render/exposure.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_exposure.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. EV 按 2 的幂
2. 亮度权重
3. 百分位累计
4. 中心权重衰减
5. 平滑按速度
6. 空直方图兜底

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `render/exposure.py`
后 15 条用例应全部通过。
