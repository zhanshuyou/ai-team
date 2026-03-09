# 在现有项目中集成 AI Company

## 核心思路

不需要独立建一个 AI Company 项目，而是把"员工"直接放进你现有项目里，
让他们了解你的代码、你的业务、你的规范，变成**真正懂你项目的团队成员**。

---

## 集成后的项目结构

假设你有一个典型的 Web 项目：

```
my-project/                         # 你的现有项目
├── src/                            # 你的源码
│   ├── components/
│   ├── pages/
│   ├── api/
│   └── utils/
├── docs/                           # 你的项目文档
├── tests/                          # 你的测试
├── package.json
│
├── .claude/                        # Claude Code 配置（新增）
│   └── settings.json
│
├── CLAUDE.md                       # 全局指令（新增）
│
└── .ai-team/                       # AI 员工团队（新增）
    ├── context/                    # 项目上下文（员工共享的"公司知识"）
    │   ├── project-overview.md     # 项目简介、技术栈、架构
    │   ├── coding-standards.md     # 编码规范
    │   ├── api-conventions.md      # API 约定
    │   ├── glossary.md             # 业务术语
    │   └── architecture.md         # 架构图 & 设计决策
    │
    ├── frontend-dev/               # 前端开发
    │   ├── SKILL.md
    │   └── references/
    │       └── component-guide.md  # 你项目的组件开发规范
    │
    ├── backend-dev/                # 后端开发
    │   ├── SKILL.md
    │   └── references/
    │       └── db-schema.md        # 你项目的数据库设计
    │
    ├── code-reviewer/              # 代码审查
    │   ├── SKILL.md
    │   └── references/
    │       └── review-checklist.md
    │
    ├── tech-writer/                # 技术文档
    │   ├── SKILL.md
    │   └── references/
    │       └── doc-template.md
    │
    ├── test-engineer/              # 测试工程师
    │   ├── SKILL.md
    │   └── references/
    │       └── test-patterns.md
    │
    └── cto/                        # 编排者
        ├── SKILL.md
        └── references/
            └── workflows.md
```

关键点：只新增了 3 样东西：`.ai-team/` 目录、`CLAUDE.md` 文件、`.claude/` 配置。
你现有的代码、文档、配置完全不需要改动。

---

## 第 1 步：创建 CLAUDE.md（公司章程）

这是整个集成的核心入口。Claude Code 启动时自动读取这个文件。

```markdown
# Project AI Team

## 项目简介

[用 2-3 句话描述你的项目是什么、做什么、给谁用]

## 技术栈

- 前端：React 18 + TypeScript + Tailwind CSS
- 后端：Node.js + Express + PostgreSQL
- 测试：Vitest + Playwright
- 部署：Docker + AWS

## AI 团队

本项目配备了一支 AI 团队，位于 `.ai-team/` 目录。
处理任务时，请根据需求调用对应的员工 Skill。

### 员工清单

| 员工 | 路径 | 职责 |
|------|------|------|
| 前端开发 | .ai-team/frontend-dev | 组件开发、页面实现、样式 |
| 后端开发 | .ai-team/backend-dev | API 开发、数据库、业务逻辑 |
| 代码审查 | .ai-team/code-reviewer | Code Review、质量把关 |
| 测试工程师 | .ai-team/test-engineer | 单元测试、E2E 测试 |
| 技术文档 | .ai-team/tech-writer | API 文档、README、注释 |
| CTO | .ai-team/cto | 复杂任务拆解与编排 |

## 工作规则

1. 修改代码前先阅读 `.ai-team/context/coding-standards.md`
2. 新增 API 遵循 `.ai-team/context/api-conventions.md`
3. 涉及多个模块的任务，先读 `.ai-team/cto/SKILL.md` 制定计划
4. 每次改动附带对应的测试
5. 产出文件放在项目的正确位置（不是单独的 outputs 目录）
```

---

## 第 2 步：编写项目上下文

这是让员工"懂你项目"的关键——把项目的核心信息沉淀下来。

### .ai-team/context/project-overview.md

```markdown
# 项目概述

## 产品

[产品名] 是一个 [做什么的] 平台，面向 [目标用户]。

## 核心功能

- 功能 A：[简述]
- 功能 B：[简述]
- 功能 C：[简述]

## 项目结构

```
src/
├── components/     # 可复用 UI 组件
│   ├── common/     # 通用组件（Button, Modal, Input...）
│   └── features/   # 业务组件（UserCard, OrderList...）
├── pages/          # 页面级组件，对应路由
├── api/            # 后端 API 路由
│   ├── routes/     # Express 路由定义
│   ├── services/   # 业务逻辑层
│   └── models/     # 数据库模型
├── utils/          # 工具函数
├── hooks/          # 自定义 React Hooks
├── types/          # TypeScript 类型定义
└── config/         # 配置文件
```

## 关键依赖

- 状态管理：Zustand（不用 Redux）
- 请求：React Query + Axios
- 表单：React Hook Form + Zod
- UI 库：自研组件库，基于 Tailwind
```

### .ai-team/context/coding-standards.md

```markdown
# 编码规范

## 命名

- 组件：PascalCase（UserProfile.tsx）
- 工具函数：camelCase（formatDate.ts）
- 常量：UPPER_SNAKE_CASE
- CSS 类：Tailwind 优先，自定义类用 kebab-case

## 组件规范

- 函数式组件 + Hooks，不用 class 组件
- Props 必须定义 TypeScript interface，以 Props 结尾
- 超过 100 行的组件要拆分
- 每个组件一个文件

## Git 规范

- 提交信息格式：type(scope): description
- type: feat / fix / docs / refactor / test / chore
- 分支命名：feature/xxx, fix/xxx, docs/xxx

## 错误处理

- API 层统一用 try-catch，返回标准错误格式
- 前端用 ErrorBoundary 兜底
- 所有 async 操作必须处理错误
```

---

## 第 3 步：编写与项目深度绑定的 Skill

员工的 SKILL.md 要引用你项目的真实结构和规范。

### .ai-team/frontend-dev/SKILL.md

```markdown
---
name: frontend-dev
description: >
  负责本项目的前端开发。包括 React 组件开发、页面实现、
  样式编写、状态管理和前端性能优化。当用户提到"写组件"、
  "做页面"、"前端"、"UI"、"样式"、"布局"时触发。
---

# 前端开发 — 本项目工作手册

## 开始前必读

1. 阅读 `.ai-team/context/project-overview.md` 了解项目结构
2. 阅读 `.ai-team/context/coding-standards.md` 了解编码规范
3. 查看 `src/components/common/` 了解现有通用组件，优先复用

## 技术栈（本项目）

- React 18 + TypeScript（严格模式）
- Tailwind CSS（不写自定义 CSS 文件）
- Zustand（状态管理）
- React Query（服务端状态）

## 开发流程

### 新增组件

1. 确定组件放在 `common/` 还是 `features/`
2. 创建文件：`src/components/[分类]/[ComponentName].tsx`
3. 定义 Props interface
4. 实现组件（复用现有 common 组件）
5. 在同目录创建测试：`[ComponentName].test.tsx`

### 新增页面

1. 在 `src/pages/` 下创建页面组件
2. 在路由配置中注册（查看 `src/config/routes.ts`）
3. 如需新 API 数据，先协调后端开发创建接口
4. 使用 React Query 的 useQuery 获取数据

## 代码模板

### 组件模板

```tsx
import { type FC } from 'react';

interface XxxProps {
  // ...
}

const Xxx: FC<XxxProps> = ({ ... }) => {
  return (
    <div className="...">
      {/* ... */}
    </div>
  );
};

export default Xxx;
```

## 注意事项

- 不要安装新依赖，除非和用户确认
- 不要修改 `src/config/` 下的文件，除非任务明确要求
- 样式只用 Tailwind，不创建 .css 文件
- 所有文本考虑 i18n（使用项目的 t() 函数）
```

### .ai-team/code-reviewer/SKILL.md

```markdown
---
name: code-reviewer
description: >
  负责代码审查和质量把关。当用户提到"review 代码"、
  "检查代码"、"代码审查"、"帮我看看这段代码"、
  "有没有问题"时触发。也适用于 PR review。
---

# 代码审查员 — 本项目工作手册

## 开始前必读

1. 阅读 `.ai-team/context/coding-standards.md`
2. 阅读 `.ai-team/code-reviewer/references/review-checklist.md`

## 审查维度

按优先级排序：

### P0：正确性
- 逻辑是否正确？边界条件是否处理？
- API 调用是否正确处理了错误？
- 类型定义是否准确？有没有 any？

### P1：安全性
- 有没有 XSS 风险？（dangerouslySetInnerHTML）
- 用户输入是否校验？
- 敏感信息是否泄露？

### P2：规范性
- 是否遵循 `.ai-team/context/coding-standards.md`？
- 命名是否清晰？
- 是否有重复代码可以抽取？

### P3：性能
- 是否有不必要的 re-render？
- 列表是否有 key？
- 大数据是否做了分页/虚拟滚动？

## 输出格式

```markdown
## Code Review 报告

**文件**：[文件路径]
**整体评价**：✅ 可合入 / ⚠️ 需修改 / ❌ 需重写

### 问题列表

1. **[P0] 第 XX 行**：[问题描述]
   建议：[修改建议]

2. **[P1] 第 XX 行**：[问题描述]
   建议：[修改建议]

### 亮点
- [值得肯定的地方]
```
```

### .ai-team/test-engineer/SKILL.md

```markdown
---
name: test-engineer
description: >
  负责编写和维护测试。包括单元测试、集成测试和 E2E 测试。
  当用户提到"写测试"、"加测试"、"测试覆盖"、"test"、
  "确保质量"时触发。也在代码审查发现缺少测试时触发。
---

# 测试工程师 — 本项目工作手册

## 开始前必读

1. 阅读 `.ai-team/context/project-overview.md` 了解项目结构
2. 查看 `tests/` 目录了解现有测试的风格和模式
3. 阅读 `.ai-team/test-engineer/references/test-patterns.md`

## 技术栈

- 单元测试：Vitest + Testing Library
- E2E 测试：Playwright
- Mock：msw（Mock Service Worker）

## 测试规范

### 文件位置

- 组件测试：与组件同目录，`ComponentName.test.tsx`
- API 测试：`tests/api/[routeName].test.ts`
- E2E 测试：`tests/e2e/[flowName].spec.ts`

### 命名规范

```typescript
describe('ComponentName', () => {
  it('should [预期行为] when [条件]', () => {
    // ...
  });
});
```

### 覆盖要求

- 新组件：至少覆盖 render + 主要交互
- 新 API：至少覆盖 成功 + 参数错误 + 权限错误
- 新工具函数：覆盖 正常输入 + 边界值 + 异常输入

## 工作流程

1. 了解要测试的代码做什么
2. 列出测试用例（先想再写）
3. 编写测试，运行确保通过
4. 检查是否覆盖了边界情况
```

---

## 第 4 步：配置 .claude/settings.json（可选）

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Edit",
      "Write",
      "Bash(npm test*)",
      "Bash(npx vitest*)",
      "Bash(npx tsc --noEmit)"
    ]
  }
}
```

---

## 实际使用场景

### 场景 1：日常开发

```
你：帮我写一个用户资料编辑页面

Claude Code 自动：
  → 触发前端开发 Skill
  → 读取项目结构和编码规范
  → 查看现有组件可以复用什么
  → 在 src/pages/ 下创建页面
  → 在 src/components/features/ 下创建业务组件
  → 附带测试文件
```

### 场景 2：代码审查

```
你：review 一下 src/components/features/UserCard.tsx

Claude Code 自动：
  → 触发代码审查 Skill
  → 对照编码规范逐项检查
  → 输出结构化的 Review 报告
```

### 场景 3：复杂任务

```
你：我们要加一个评论功能，从数据库到 UI 都做好

Claude Code 自动：
  → 触发 CTO Skill 进行编排
  → 制定计划：
      1. 后端开发：设计数据库 schema + API
      2. 前端开发：实现评论组件 + 页面集成
      3. 测试工程师：补充测试
      4. 代码审查：最终 Review
  → 用户确认后逐步执行
```

### 场景 4：文档维护

```
你：帮 src/api/routes/users.ts 补充 API 文档

Claude Code 自动：
  → 触发技术文档 Skill
  → 读取现有 API 代码
  → 按项目文档模板生成文档
  → 更新 docs/ 目录
```

---

## 注意事项

### 要做的

- **context/ 内容保持更新**：技术栈变了、架构调整了，及时同步
- **SKILL.md 引用真实路径**：用你项目的实际文件路径，不要用占位符
- **渐进式添加员工**：先从最常用的 2-3 个开始，别一次铺太多
- **版本控制**：`.ai-team/` 目录应该提交到 Git，团队共享

### 不要做的

- **不要让员工知道太多无关信息**：每个 Skill 只引用它需要的上下文
- **不要跳过 context/**：没有项目上下文，员工写出来的代码不会符合你的规范
- **不要把 .ai-team 搞太复杂**：从简单开始，遇到问题再迭代

### .gitignore 建议

```gitignore
# 不需要忽略 .ai-team，它应该被版本控制
# 但可以忽略一些临时文件
.ai-team/**/temp/
.ai-team/**/drafts/
```

---

## 快速启动清单

```
□ 1. 在项目根目录创建 CLAUDE.md
□ 2. 创建 .ai-team/context/，写好 project-overview.md 和 coding-standards.md
□ 3. 创建你最需要的 2-3 个员工 Skill
□ 4. 用一个小任务测试（比如"写一个按钮组件"）
□ 5. 根据效果迭代调整 SKILL.md
□ 6. 逐步添加更多员工
```
