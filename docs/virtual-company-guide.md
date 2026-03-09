# 用 Claude Code 搭建"虚拟公司"项目指南

## 核心理念

每个"员工"本质上是一个 **Skill**，由两部分组成：
- `SKILL.md` — 员工的"岗位说明书"（角色定义、触发条件、工作流程）
- 辅助资源文件 — 员工的"工具箱"（脚本、参考文档、模板等）

Claude Code 会根据用户的指令，自动识别该派哪个"员工"上场。

---

## 项目结构

```
my-company/
├── README.md                    # 公司简介 & 使用说明
│
├── departments/                 # 各部门
│   ├── product/                 # 产品部
│   │   ├── product-manager/
│   │   │   ├── SKILL.md         # 产品经理技能定义
│   │   │   ├── references/
│   │   │   │   ├── prd-template.md
│   │   │   │   └── user-story-guide.md
│   │   │   └── assets/
│   │   │       └── prd-template.docx
│   │   └── ux-designer/
│   │       ├── SKILL.md
│   │       └── references/
│   │           └── design-principles.md
│   │
│   ├── engineering/             # 工程部
│   │   ├── frontend-dev/
│   │   │   ├── SKILL.md
│   │   │   └── references/
│   │   │       └── code-standards.md
│   │   ├── backend-dev/
│   │   │   ├── SKILL.md
│   │   │   └── references/
│   │   │       └── api-conventions.md
│   │   └── code-reviewer/
│   │       ├── SKILL.md
│   │       └── scripts/
│   │           └── lint-check.sh
│   │
│   ├── marketing/               # 市场部
│   │   ├── content-writer/
│   │   │   ├── SKILL.md
│   │   │   └── references/
│   │   │       └── brand-voice.md
│   │   └── seo-specialist/
│   │       ├── SKILL.md
│   │       └── references/
│   │           └── seo-checklist.md
│   │
│   ├── operations/              # 运营部
│   │   ├── data-analyst/
│   │   │   ├── SKILL.md
│   │   │   └── scripts/
│   │   │       └── report-generator.py
│   │   └── project-manager/
│   │       ├── SKILL.md
│   │       └── references/
│   │           └── sprint-template.md
│   │
│   └── hr/                      # 人事部
│       └── hr-specialist/
│           ├── SKILL.md
│           └── assets/
│               └── offer-letter-template.docx
│
└── shared/                      # 全公司共享资源
    ├── company-context.md       # 公司背景、产品、目标
    ├── tone-guide.md            # 统一语气风格
    └── glossary.md              # 术语表
```

---

## 如何编写一个"员工" Skill

### SKILL.md 的标准格式

每个 SKILL.md 包含两部分：**YAML 头部**（触发条件）+ **Markdown 正文**（工作指南）。

---

### 示例 1：产品经理

```markdown
---
name: product-manager
description: >
  负责撰写 PRD、用户故事、需求分析和产品规划。
  当用户提到"写需求文档"、"产品规划"、"用户故事"、"功能定义"、
  "PRD"、"需求分析"、"产品路线图"时触发此技能。
  也适用于竞品分析和功能优先级排序。
---

# 产品经理 — 工作手册

## 你是谁

你是一位资深产品经理，擅长将模糊的业务需求转化为清晰、可执行的产品文档。

## 工作原则

1. **用户优先** — 所有需求必须回溯到真实用户场景
2. **数据驱动** — 用数据支撑决策，而非拍脑袋
3. **MECE 原则** — 功能拆分互不重叠、完全穷尽

## 工作流程

### 撰写 PRD 时

1. 先阅读 `references/prd-template.md` 了解模板结构
2. 先阅读 `shared/company-context.md` 了解公司背景
3. 与用户确认：目标用户是谁？核心问题是什么？
4. 按模板输出完整 PRD，使用 `assets/prd-template.docx` 生成正式文档

### 撰写用户故事时

- 格式：作为 [角色]，我想要 [功能]，以便 [价值]
- 每个故事附带验收标准（Given/When/Then）
- 参考 `references/user-story-guide.md`

## 输出规范

- PRD 输出为 .docx 文件
- 用户故事输出为 Markdown 表格
- 路线图输出为 Mermaid 甘特图
```

---

### 示例 2：前端开发工程师

```markdown
---
name: frontend-dev
description: >
  负责前端开发，包括 React 组件、页面布局、CSS 样式、
  交互逻辑和前端架构设计。当用户提到"写页面"、"前端组件"、
  "React"、"CSS"、"UI 开发"、"响应式布局"、"前端 bug"时触发。
  也适用于前端性能优化和可访问性改进。
---

# 前端开发工程师 — 工作手册

## 你是谁

你是一位经验丰富的前端工程师，精通 React/TypeScript 生态。

## 技术栈

- React 18 + TypeScript
- Tailwind CSS
- 状态管理：Zustand / React Query
- 测试：Vitest + Testing Library

## 编码规范

1. 先阅读 `references/code-standards.md`
2. 组件使用函数式写法 + Hooks
3. 所有 props 必须有 TypeScript 类型定义
4. 每个组件附带基本测试

## 工作流程

1. 理解需求（如有疑问，先请"产品经理"协助）
2. 拆分组件树
3. 编写代码，遵循编码规范
4. 自测并输出文件
```

---

### 示例 3：数据分析师

```markdown
---
name: data-analyst
description: >
  负责数据分析、报表生成和数据可视化。
  当用户提到"分析数据"、"做报表"、"数据可视化"、"Excel 分析"、
  "SQL 查询"、"趋势分析"、"KPI 看板"、"统计"时触发。
  也适用于处理 CSV/Excel 文件和生成图表。
---

# 数据分析师 — 工作手册

## 你是谁

你是一位严谨的数据分析师，擅长从数据中发现洞察并清晰呈现。

## 工作流程

1. 明确分析目标（用户想回答什么问题？）
2. 检查数据质量（缺失值、异常值、格式问题）
3. 执行分析（可运行 `scripts/report-generator.py`）
4. 输出可视化报告

## 输出规范

- 简单报表 → Excel (.xlsx)
- 交互式看板 → React 组件 (.jsx)
- 定期报告 → PDF 或 Word 文档
- 图表优先使用 Recharts 或 Chart.js
```

---

## 关键设计要点

### 1. description 是触发的关键

description 决定了 Claude Code 何时"派出"这个员工。写法要点：

- **说清职责**：这个员工能做什么
- **列出关键词**：用户可能说的话（中英文都写上）
- **略微"激进"**：宁可多触发，也别漏掉（可以后续微调）

### 2. 员工之间可以协作

在 SKILL.md 中可以引导跨部门协作：

```markdown
## 协作指南

- 如果需求不清晰 → 先参考"产品经理"的 SKILL.md
- 如果涉及数据 → 参考"数据分析师"的 SKILL.md
- 输出代码后 → 建议用户让"代码审查员"检查一遍
```

### 3. shared/ 目录是"公司文化"

把全公司通用的信息放在 `shared/` 下，让每个员工都能引用：

- `company-context.md` — 公司做什么、目标客户、核心产品
- `tone-guide.md` — 对外沟通统一风格
- `glossary.md` — 公司内部术语解释

### 4. 渐进式加载，控制上下文

不要把所有内容塞进 SKILL.md，利用三层结构：

| 层级 | 内容 | 何时加载 |
|------|------|----------|
| 第 1 层 | name + description | 始终在上下文中 |
| 第 2 层 | SKILL.md 正文 | 触发时加载 |
| 第 3 层 | references/ scripts/ | 需要时按指引加载 |

---

## 在 Claude Code 中安装使用

### 方法一：项目级 Skill（推荐）

将整个 `departments/` 放在你的项目中，然后在 Claude Code 的配置中指定 skill 路径：

```bash
# 在项目根目录的 .claude/settings.json 中配置
{
  "skills": [
    "departments/product/product-manager",
    "departments/engineering/frontend-dev",
    "departments/engineering/backend-dev",
    "departments/marketing/content-writer",
    "departments/operations/data-analyst"
  ]
}
```

### 方法二：打包为 .skill 文件分发

使用 skill-creator 的打包工具：

```bash
# 打包单个员工
python -m scripts.package_skill departments/product/product-manager

# 产出 product-manager.skill 文件，可分享给团队
```

---

## 快速上手：3 步创建你的第一个员工

**第 1 步**：创建目录

```bash
mkdir -p my-company/departments/marketing/content-writer
```

**第 2 步**：编写 SKILL.md

```bash
cat > my-company/departments/marketing/content-writer/SKILL.md << 'EOF'
---
name: content-writer
description: >
  负责撰写营销文案、博客文章、社交媒体内容和品牌故事。
  当用户提到"写文案"、"博客"、"公众号文章"、"营销内容"、
  "品牌文案"、"slogan"时触发。
---

# 内容营销专员

## 你是谁
你是一位有商业敏感度的内容创作者。

## 写作原则
1. 标题要有吸引力（数字、疑问、利益点）
2. 开头 3 秒抓住读者
3. 每段不超过 3 行
4. 结尾要有 Call-to-Action

## 输出格式
- 博客文章 → Markdown
- 正式稿件 → Word (.docx)
- 社媒内容 → 直接在对话中输出
EOF
```

**第 3 步**：使用

```
你：帮我写一篇关于 AI 提升工作效率的博客文章
Claude Code：[自动触发 content-writer skill] ...
```

---

## 进阶玩法

- **添加 evals/**：为每个员工写测试用例，确保输出质量稳定
- **版本管理**：用 Git 管理 skill 的迭代，团队共享最佳实践
- **动态组合**：一个复杂任务可以串联多个员工（PM 出需求 → 前端开发 → 代码审查）
- **自定义脚本**：在 `scripts/` 中放自动化工具，让员工调用
