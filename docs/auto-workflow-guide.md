# 让虚拟员工"自发工作"— 编排与自动化指南

## 核心问题

搭建好 Skill 员工后，默认模式是"你说一句，它做一句"。
要让员工**自发工作**，需要解决三个层面的问题：

| 层面 | 问题 | 解法 |
|------|------|------|
| 谁来指挥 | 谁决定下一步做什么 | 编排者 Skill（项目经理 / CTO） |
| 怎么串联 | 一个员工的产出如何流转给下一个 | 工作流定义 + 文件约定 |
| 何时触发 | 什么条件下启动工作 | 入口指令 / 自动化脚本 |

---

## 方案一：编排者 Skill（最推荐）

创建一个"CTO"或"项目经理"级别的 Skill，它的职责不是干活，
而是**拆解任务、分配给其他员工、串联流程**。

### 目录结构

```
departments/
├── leadership/
│   └── cto/
│       ├── SKILL.md              # 编排者
│       └── references/
│           └── workflows.md      # 预定义的工作流
```

### CTO 的 SKILL.md

```markdown
---
name: cto
description: >
  公司技术总监和项目编排者。负责接收高层级任务，拆解为子任务，
  并按正确顺序调度各部门员工完成。当用户提出复杂任务、跨部门需求、
  "帮我做一个完整的XX"、"从头到尾搞定XX"、"启动XX项目"时触发。
  也适用于用户不确定该找谁时的任务分诊。
---

# CTO — 任务编排手册

## 你是谁

你是公司的 CTO，不直接写代码或写文案，
你的核心工作是**拆解、分配、串联、把控质量**。

## 工作流程

### 第 1 步：理解任务

收到用户的高层级需求后，先明确：
- 最终交付物是什么？（网站？文档？数据报告？）
- 涉及哪些部门的员工？
- 有没有依赖关系？（比如先出需求文档，再开发）

### 第 2 步：制定执行计划

把任务拆解为有序的步骤，明确每步由谁执行。
输出一个执行计划给用户确认：

**示例执行计划：**

```
任务：为新产品上线准备完整的营销方案

步骤 1 → 产品经理：梳理产品卖点和目标用户画像
步骤 2 → 内容营销：基于卖点撰写落地页文案
步骤 3 → 前端开发：将文案实现为落地页
步骤 4 → SEO 专员：优化落地页的 SEO
步骤 5 → 数据分析：设置 KPI 追踪方案
```

### 第 3 步：逐步执行

用户确认计划后，按顺序调用每个员工的 SKILL.md：

1. 阅读对应员工的 SKILL.md
2. 按其工作手册执行任务
3. 将产出保存到约定位置
4. 将产出作为输入传递给下一步

### 第 4 步：质量把关

每个步骤完成后，快速检查：
- 产出是否符合预期？
- 是否有遗漏或冲突？
- 是否需要返工？

## 预定义工作流

参考 `references/workflows.md` 中的常见工作流模板。

## 任务分诊表

当用户需求不明确时，用这张表判断派谁：

| 用户说的 | 派谁 |
|----------|------|
| "写个需求文档" | 产品经理 |
| "做个页面" | 前端开发 |
| "分析一下数据" | 数据分析师 |
| "写篇文章" | 内容营销 |
| "审查代码" | 代码审查员 |
| "做个完整的XX" | CTO 自己编排 |
```

### workflows.md（预定义工作流）

```markdown
# 预定义工作流

## 工作流 1：新功能上线

触发词：新功能、feature launch、功能上线

```
产品经理 → 撰写 PRD
    ↓
前端开发 → 实现 UI
    ↓ （同时）
后端开发 → 实现 API
    ↓
代码审查 → Review 代码
    ↓
数据分析 → 设置埋点方案
```

## 工作流 2：内容营销活动

触发词：营销活动、内容推广、campaign

```
产品经理 → 提炼核心卖点
    ↓
内容营销 → 撰写系列文案
    ↓
SEO 专员 → 优化关键词
    ↓
数据分析 → 设置效果追踪
```

## 工作流 3：数据驱动决策

触发词：季度复盘、数据分析、决策支持

```
数据分析 → 拉取并清洗数据
    ↓
数据分析 → 生成可视化报告
    ↓
产品经理 → 基于数据提出建议
    ↓
内容营销 → 撰写内部通报
```
```

---

## 方案二：CLAUDE.md 全局指令

在项目根目录放一个 `CLAUDE.md` 文件，Claude Code 启动时会自动读取。
这相当于给整个"公司"下达了常驻指令。

### CLAUDE.md 示例

```markdown
# 公司运作规则

## 身份

你是这家虚拟公司的 AI 运营系统。公司有多个部门的员工（Skill），
你负责理解用户需求并调度合适的员工完成任务。

## 核心规则

1. **复杂任务自动拆解**：当用户提出涉及多个职能的任务时，
   自动制定执行计划，列出步骤和负责人，确认后逐步执行。

2. **简单任务直接派发**：明确属于某个员工职责的任务，直接触发对应 Skill。

3. **产出流转**：每个步骤的产出自动作为下一步的输入。
   文件统一存放在 `outputs/` 目录，按任务名组织。

4. **主动补位**：如果发现某个步骤缺少信息，主动向用户提问，
   而不是跳过或猜测。

## 可用员工

- departments/product/product-manager — 产品经理
- departments/engineering/frontend-dev — 前端开发
- departments/engineering/backend-dev — 后端开发
- departments/engineering/code-reviewer — 代码审查
- departments/marketing/content-writer — 内容营销
- departments/marketing/seo-specialist — SEO 专员
- departments/operations/data-analyst — 数据分析
- departments/operations/project-manager — 项目经理

## 工作流触发

当用户说"启动XX项目"或提出跨部门需求时，
自动读取 `departments/leadership/cto/references/workflows.md`，
匹配最合适的工作流模板，制定计划后执行。
```

---

## 方案三：任务脚本驱动（自动化程度最高）

用脚本定义完整流水线，一条命令启动，所有员工依次工作。

### run-workflow.sh

```bash
#!/bin/bash
# 用法：./run-workflow.sh "为AI健身App设计MVP"

TASK="$1"
WORKSPACE="outputs/$(date +%Y%m%d-%H%M%S)"
mkdir -p "$WORKSPACE"

echo "🏢 启动工作流：$TASK"
echo "📁 工作目录：$WORKSPACE"

# 第 1 步：产品经理出 PRD
echo "👤 步骤 1/4：产品经理 → 撰写 PRD..."
claude -p "
你是产品经理。请阅读 departments/product/product-manager/SKILL.md 的工作手册，
为以下需求撰写一份 PRD：

$TASK

将 PRD 保存到 $WORKSPACE/01-prd.md
" --allowedTools "Edit,Write,Read"

# 第 2 步：前端开发写页面
echo "👤 步骤 2/4：前端开发 → 实现原型..."
claude -p "
你是前端开发工程师。请阅读 departments/engineering/frontend-dev/SKILL.md 的工作手册。
基于以下 PRD 实现一个 React 原型页面：

$(cat $WORKSPACE/01-prd.md)

将代码保存到 $WORKSPACE/02-prototype.jsx
" --allowedTools "Edit,Write,Read"

# 第 3 步：代码审查
echo "👤 步骤 3/4：代码审查 → Review..."
claude -p "
你是代码审查员。请阅读 departments/engineering/code-reviewer/SKILL.md 的工作手册。
审查以下代码并给出改进建议：

$(cat $WORKSPACE/02-prototype.jsx)

将审查报告保存到 $WORKSPACE/03-review.md
" --allowedTools "Edit,Write,Read"

# 第 4 步：内容营销写文案
echo "👤 步骤 4/4：内容营销 → 撰写上线文案..."
claude -p "
你是内容营销专员。请阅读 departments/marketing/content-writer/SKILL.md 的工作手册。
基于以下 PRD 为产品撰写一篇上线推广文章：

$(cat $WORKSPACE/01-prd.md)

将文章保存到 $WORKSPACE/04-launch-post.md
" --allowedTools "Edit,Write,Read"

echo "✅ 工作流完成！所有产出在 $WORKSPACE/"
ls -la "$WORKSPACE/"
```

### 使用方式

```bash
chmod +x run-workflow.sh
./run-workflow.sh "设计一个面向大学生的二手教材交易平台"
```

一条命令，4 个员工依次工作，最终在 `outputs/` 下得到：
- PRD 文档
- React 原型
- 代码审查报告
- 上线推广文案

---

## 三种方案对比

| | 编排者 Skill | CLAUDE.md | 脚本驱动 |
|---|---|---|---|
| **启动方式** | 对话中说"启动XX" | 任何对话自动生效 | 命令行执行 |
| **灵活性** | ⭐⭐⭐ 可动态调整 | ⭐⭐ 规则固定 | ⭐ 流程固定 |
| **自动化** | ⭐⭐ 需确认关键节点 | ⭐⭐ 需确认关键节点 | ⭐⭐⭐ 全自动 |
| **适合场景** | 探索性项目 | 日常工作 | 重复性流水线 |
| **推荐组合** | ✅ 搭配 CLAUDE.md | ✅ 搭配编排者 Skill | 独立使用 |

## 最佳实践：组合使用

```
CLAUDE.md          → 定义公司规则和员工清单（常驻）
  +
CTO Skill          → 处理复杂的跨部门任务（按需触发）
  +
workflows.md       → 预定义常见流程模板（CTO 参考）
  +
run-workflow.sh    → 成熟流程一键执行（完全自动化）
```

这样你就有了一个从"对话式协作"到"一键自动化"的完整梯度，
根据任务的成熟度选择合适的驱动方式。
