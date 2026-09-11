# EvoCode

EvoCode 是使用 Python 实现的终端 Coding Agent，也是一个以理解设计、逐步实现和可验证交付为目标的学习型项目。

## 当前状态

当前仅完成 Repository Bootstrap：目录、文档体系、Python 包骨架和 Git 基线。尚未实现 Runtime、Harness 或 SkillOpt 业务功能，也没有可运行的 CLI。

## 路线与文档

| 阶段 | 目标 | 设计与验收 |
| --- | --- | --- |
| 01-core-runtime | 最小可运行 Runtime：Model、Agent Loop、Tool Calling、Tool Registry、CLI | [spec](docs/01-core-runtime/spec.md) · [tasks](docs/01-core-runtime/tasks.md) · [checklist](docs/01-core-runtime/checklist.md) |
| 02-harness | Context、Permission、MCP、Skill、Hook | [spec](docs/02-harness/spec.md) · [tasks](docs/02-harness/tasks.md) · [checklist](docs/02-harness/checklist.md) |
| 03-skillopt | Trace、Benchmark、Evaluation、Failure Analysis、Skill Optimization、Validation | [spec](docs/03-skillopt/spec.md) · [tasks](docs/03-skillopt/tasks.md) · [checklist](docs/03-skillopt/checklist.md) |

这些能力是阶段方向，不表示已确认设计或已实现。SkillOpt 必须在用户明确宣布进入该阶段后启动。

## 目录

```text
EvoCode/
├── README.md
├── AGENTS.md
├── pyproject.toml
├── .gitignore
├── docs/
│   ├── 01-core-runtime/  # spec.md / tasks.md / checklist.md
│   ├── 02-harness/       # spec.md / tasks.md / checklist.md
│   └── 03-skillopt/      # spec.md / tasks.md / checklist.md
├── src/
│   └── evocode/
│       └── __init__.py
└── tests/
    └── .gitkeep
```

## 协作流程

Idea → Clarification → Spec → Tasks → Checklist → Implementation → Test → End-to-End Verification。

详细规则见 [AGENTS.md](AGENTS.md)。三份文档按阶段维护在 `docs/`，根目录不另建重复版本；阶段内按 Feature 组织内容。功能开始前先澄清并更新文档，用户确认后才编码。

MewCode 是 Runtime / Harness 的参考实现；参考时先解释设计和取舍，不机械复制。参考仓库地址及版本待确认。

## Python 工程

采用 `src` 布局，工程 Python 下限暂设为 3.11，无运行时依赖。包版本 `0.0.0` 仅表示初始骨架。

后续开发可创建虚拟环境并以可编辑方式安装：

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

上述安装需要可用的构建依赖。当前没有业务测试、测试框架配置或命令行入口；测试工具与相关模块一起确定，不将空测试目录视为功能验收通过。
