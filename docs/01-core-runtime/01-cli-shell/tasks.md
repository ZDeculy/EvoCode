# Feature 01 — CLI Shell Tasks

## 当前收尾状态

已按用户最新要求完成极简文字界面。Task 1～6 在调整后的范围内完成：启动入口已接入，8 项测试通过，实际终端验证见 checklist。历史视觉验收不再作为完成门槛。下一 Feature 尚未开始。

以下保留历史任务记录，旧视觉待办已由本次范围调整取消。


状态：Task 1～5 完成；Task 6 自动化与 PTY 验证完成，人工视觉验收待完成。

已确认技术方案：Rich 负责静态展示，标准库负责参数解析、单行输入和测试；不采用全屏框架。

## Task 1 — 工程依赖与测试基础

- 状态：完成。uv sync 成功，包元数据测试 1 项通过（初次空测试发现返回 5，补充实际测试后通过）。
- 目标：工程依赖与测试基础。
- 影响文件：pyproject.toml、uv.lock、tests/test_cli.py。
- 依赖：无。
- 大致变更：使用 uv add rich 添加唯一新增运行时依赖；使用标准库 unittest，避免额外测试依赖；由 uv 生成锁文件。保持现有构建配置和 Python 下限。
- 参考位置：pyproject.toml 已有 setuptools 配置；tests/ 目前仅占位。
- 验证：uv sync 成功，uv run python -m unittest discover -s tests -v 可执行。

## Task 2 — 品牌与启动信息展示

- 状态：完成。100/60/40 列、长路径、字面标记及无颜色输出测试通过；视觉终端检查在 Task 6 执行。
- 目标：品牌与启动信息展示。
- 影响文件：src/evocode/ui.py、tests/test_ui.py。
- 依赖：Task 1。
- 大致变更：以 Rich 输出蓝灰与暖橙字符 Logo、小机器人和版本/模型/路径。宽度不足时简化，长路径换行，禁用用户文本标记解析，不强制背景色。
- 参考位置：src/evocode/__init__.py 为空；当前无展示实现。
- 验证：检查不同宽度、长路径、标记字符和无颜色输出；人工对照参考图。

## Task 3 — 单行交互与基础命令

- 状态：完成。连续输入、命令、空白输入及中断测试通过。
- 目标：单行交互与基础命令。
- 影响文件：src/evocode/cli.py、tests/test_cli.py。
- 依赖：Task 2。
- 大致变更：用标准库输入与参数解析实现循环、空白输入、普通文本提示、/help、/exit、未知命令、Ctrl+C 和 EOF；不调用网络或工具。
- 参考位置：当前无 CLI 实现；展示调用 Task 2。
- 验证：验证多轮输入后可退出；每条命令、空白输入和中断路径均有可观察结果。

## Task 4 — 启动参数与元信息

- 状态：完成。启动参数、实际包版本和工作目录测试通过。
- 目标：启动参数与元信息。
- 影响文件：src/evocode/cli.py、tests/test_cli.py。
- 依赖：Task 3。
- 大致变更：通过包元数据读取版本，通过当前工作目录读取 Path；添加 --help 与 --version，直接返回且不启动交互。
- 参考位置：pyproject.toml 的项目元数据；Task 3 的 CLI 模块。
- 验证：元数据一致；不同目录启动显示对应目录；参数不等待输入。

## Task 5 — 接入主流程

- 状态：完成。uv sync 和 8 项测试通过，覆盖已安装入口、外部工作目录与有限输入 EOF。
- 目标：接入主流程。
- 影响文件：pyproject.toml、src/evocode/cli.py、tests/test_cli.py。
- 依赖：Task 4。
- 大致变更：配置 evocode CLI entry point，连接启动展示和交互循环；保留用户文档改动，不重写 README 或 AGENTS。
- 参考位置：现有 pyproject.toml；Task 2～4 的模块。
- 验证：uv sync 后 uv run evocode 从真实入口启动；测试通过已安装入口执行而非仅调用内部函数。

## Task 6 — 端到端验证

- 状态：自动化与 PTY 验证完成；真实图形终端的配色、字体及不同宽度视觉检查待完成，不能标记全面验收。
- 目标：端到端验证。
- 影响文件：docs/01-core-runtime/01-cli-shell/checklist.md、必要的 CLI/UI 修复文件。
- 依赖：Task 5。
- 大致变更：运行自动化验证，在真实终端核对视觉、目录、连续交互和退出；记录已测试/已集成/已验收状态及限制。
- 参考位置：本 Feature checklist.md；Task 1～5 的实现。
- 验证：完成清单中的自动化与人工 E2E；未执行项不勾选。

