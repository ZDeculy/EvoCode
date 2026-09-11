# EvoCode 协作规则

## 定位与边界

- EvoCode 是 Python 终端 Coding Agent，按 Core Runtime → Harness → SkillOpt 推进。
- 当前仅有工程初始化。不要因目录或路线已存在而视为功能实现授权。
- 用户明确说“现在开始 SkillOpt”之前，不实现 Skill Optimization 系统，也不提前引入其框架。
- 优先 Simple → Correct → Extensible，避免没有明确场景的抽象层。
- Model、Agent Loop、Tool、Tool Registry、Context、Permission、MCP、Skill、Hook、Trace / Evaluation 应保持清晰边界。

## 新 Feature 的流程

1. 先澄清：解决的问题、Runtime 中的位置、输入输出、现有模块交互、最小能力、不做的能力、边缘情况、MewCode 可参考设计。
2. 有架构选择时，解释方案差异和取舍，与用户共同确定。可以阅读代码，不提前大规模修改或实现。
3. 维护当前阶段的 spec.md、tasks.md、checklist.md。
4. 三份文档基本明确且用户确认开始实现后，才进入 Coding。用户明确授权的 Repository Bootstrap 不需要重复确认。
5. 按 tasks.md 顺序推进；每个 Task 完成后修改状态、运行相关测试、核对 checklist，并报告结果后继续下一项。
6. 接入主流程并完成端到端验证，区分已编写、已测试、已集成、已验收状态。

## 文档约定

文档唯一入口为 `docs/01-core-runtime/`、`docs/02-harness/`、`docs/03-skillopt/`。不在根目录重复维护三份文档。阶段内按 Feature 划分章节，保留已完成任务与验收证据，避免用下一 Feature 覆盖历史。

### spec.md：What / Why

描述 Background、Goal、Target User、Capabilities、Non-functional Requirements、High-level Design、Constraints、Out of Scope 和完成条件。一句话描述一个能力。

不要长期放置具体函数名、参数名、类名、SDK 类型名、行号、默认值、精确错误文本或临时实现细节。未知设计明确标记待澄清，不擅自补全复杂需求。

### tasks.md：实现顺序

每个 Feature 通常拆分为 5～15 个 Task，一个 Task 是一次相对独立 Coding Session 可完成的可验证增量。每项写明目标、影响文件、依赖、大致变更、已有代码参考位置；没有参考实现时明确注明。

每个 Feature 最后两项必须为“接入主流程”和“端到端验证”。初始化阶段不为了凑数量虚构功能任务。

### checklist.md：验收证据

每项必须可勾选、可执行、可观察并明确判断 Pass / Fail。具体命令、输入、输出、默认值、阈值和错误信息可以放在这里。每个 Feature 至少包含一项 End-to-End 验收。

没有执行的检查保持未勾选；阻塞、失败与未运行状态不得隐藏。不要使用“功能完整”“性能正常”等无法验证的验收表述。

## 参考 MewCode

说明其做法、设计理由、EvoCode 是否采用、以及采用后的实现方式。以实际读到的代码为依据，记录仓库和版本；未确认来源时不猜测。当前需求更简单时采用更小实现。

## 工程纪律

- 先检查已有文件与 Git 状态，保留用户已有改动，不擅自重写项目。
- 不提交密钥、环境文件、虚拟环境、缓存或构建产物。
- 测试与改动范围匹配；如未运行测试或存在限制，明确说明。
- 遇到明显设计问题、更简单方案或未来风险，在编码前直接指出。
