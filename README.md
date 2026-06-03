<div align="center">

# 🎬 StoryForge

### AI驱动的内容创作工具 — 一键生成漫画脚本、漫剧短剧脚本

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/Version-0.1.0-blue.svg)](https://github.com/your-username/storyforge/releases)
[![OpenAI Compatible](https://img.shields.io/badge/OpenAI-Compatible-green.svg)](https://platform.openai.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](https://github.com/your-username/storyforge/pulls)
[![Issues](https://img.shields.io/github/issues/your-username/storyforge.svg)](https://github.com/your-username/storyforge/issues)
[![Stars](https://img.shields.io/github/stars/your-username/storyforge.svg)](https://github.com/your-username/storyforge/stargazers)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-blue.svg)](https://peps.python.org/pep-0008/)

<p>
  <strong>用 AI 释放你的创作灵感，让故事从想象变为文字。</strong>
</p>

[快速开始](#-快速开始) · [功能特性](#-核心特性) · [示例输出](#-示例输出) · [文档](#-文档) · [贡献指南](#-贡献指南) · [常见问题](#-常见问题) · [路线图](#-路线图)

</div>

---

## 📖 目录

- [项目简介](#-项目简介)
- [核心特性](#-核心特性)
- [快速开始](#-快速开始)
- [项目架构](#-项目架构)
- [命令行用法](#-命令行用法)
- [示例输出](#-示例输出)
- [配置详解](#-配置详解)
- [提示词自定义](#-提示词自定义)
- [项目结构](#-项目结构)
- [文档](#-文档)
- [贡献指南](#-贡献指南)
- [常见问题](#-常见问题)
- [路线图](#-路线图)
- [相关链接](#-相关链接)
- [Star 历史](#-star-历史)
- [License](#-license)

---

## 📖 项目简介

StoryForge 是一个基于 AI 的内容创作工具，旨在帮助创作者快速生成高质量的漫画脚本和短剧剧本。无论是个人创作者还是团队协作，StoryForge 都能大幅降低剧本创作的门槛，让你专注于故事本身的构思。

**支持的 AI 模型：**

| 提供商 | 推荐模型 | 说明 |
|--------|---------|------|
| OpenAI | `gpt-3.5-turbo` / `gpt-4` | 综合能力强，多语言支持好 |
| 智谱AI | `glm-4.5-air` / `glm-4.7` | 中文理解优秀，价格实惠 |
| MiMo | `mimo-v2.5` | 小米自研模型，高性能 |
| DeepSeek | `deepseek-chat` | 性价比高，代码能力强 |

## ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🎨 **漫画脚本生成** | 一键生成分镜脚本、角色设定、对话内容，每页 3-5 个分镜 |
| 🎬 **漫剧/短剧脚本生成** | 生成完整的短剧剧本，包含场景、对白、动作指导 |
| 🤖 **多模型支持** | 支持 OpenAI、智谱AI、MiMo、DeepSeek 等多种 AI 模型 |
| ⚙️ **自定义提示词** | YAML 格式的提示词模板，精确控制输出风格和方向 |
| 📦 **多种模板** | 内置校园日常、都市爱情、奇幻冒险等多种内容模板 |
| 📤 **多格式导出** | 支持 Markdown、JSON、PDF 等格式导出 |
| 🖥️ **CLI 工具** | 基于 Click 的命令行界面，操作简便直观 |
| 🔧 **高度可配置** | 通过 YAML 配置文件灵活调整生成参数 |

## 🚀 快速开始

### 环境要求

- Python 3.8 或更高版本
- 有效的 AI 模型 API 密钥

### 安装

```bash
# 1. 克隆仓库
git clone https://github.com/your-username/storyforge.git
cd storyforge

# 2. 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux / macOS
# venv\Scripts\activate   # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置 API 密钥
cp config.example.yaml config.yaml
```

编辑 `config.yaml`，填入你的 API 密钥：

```yaml
model:
  provider: "openai"
  api_key: "sk-your-api-key-here"
  base_url: "https://api.openai.com/v1"
  model_name: "gpt-3.5-turbo"
```

### 首次运行

```bash
# 生成漫画脚本
python -m src generate --type comic --theme "校园日常"

# 生成短剧脚本
python -m src generate --type drama --theme "都市爱情"
```

## 🏗️ 项目架构

```
┌─────────────────────────────────────────────────────────┐
│                      CLI Layer                           │
│              (click-based command interface)              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐  │
│  │ generate │  │  custom  │  │ templates│  │ prompts│  │
│  │ command  │  │ command  │  │   list   │  │  list  │  │
│  └────┬─────┘  └────┬─────┘  └──────────┘  └────────┘  │
│       │              │                                    │
├───────┴──────────────┴────────────────────────────────────┤
│                    Core Engine                            │
│  ┌────────────────────────────────────────────────────┐  │
│  │              ScriptGenerator                        │  │
│  │  ┌──────────┐  ┌──────────┐  ┌───────────────┐   │  │
│  │  │  Config   │  │  Prompt  │  │   Template    │   │  │
│  │  │  Loader   │  │  Engine  │  │    Engine     │   │  │
│  │  └──────────┘  └────┬─────┘  └───────────────┘   │  │
│  │                      │                              │  │
│  │              ┌───────┴───────┐                      │  │
│  │              │  API Client   │                      │  │
│  │              │ (OpenAI SDK)  │                      │  │
│  │              └───────┬───────┘                      │  │
│  └──────────────────────┼─────────────────────────────┘  │
├─────────────────────────┼────────────────────────────────┤
│                    Data Layer                             │
│  ┌──────────┐  ┌──────────┐  ┌───────────────────┐     │
│  │ prompts/ │  │templates/│  │     output/        │     │
│  │  *.yaml  │  │   *.md   │  │ generated scripts  │     │
│  └──────────┘  └──────────┘  └───────────────────┘     │
└─────────────────────────────────────────────────────────┘
```

## 💻 命令行用法

StoryForge 提供了以下 CLI 命令：

### `generate` — 生成脚本

```bash
# 生成漫画脚本（指定主题）
python -m src generate --type comic --theme "校园日常"

# 生成短剧脚本（指定主题和风格）
python -m src generate --type drama --theme "都市爱情" --style "温情"

# 指定页数和输出文件
python -m src generate --type comic --theme "奇幻冒险" --pages 6 --output output.md
```

**参数说明：**

| 参数 | 缩写 | 说明 | 默认值 |
|------|------|------|--------|
| `--type` | `-t` | 脚本类型：`comic` / `drama` | `comic` |
| `--theme` | `-m` | 主题（必填） | — |
| `--style` | `-s` | 风格 | 无（使用默认） |
| `--pages` | `-p` | 页数/集数 | `4` |
| `--output` | `-o` | 输出文件路径 | 打印到终端 |

### `custom` — 自定义提示词生成

```bash
python -m src custom --prompt prompts/comic_basic.yaml --theme "都市爱情"
```

### `list-templates` — 列出可用模板

```bash
python -m src list-templates
# 📋 可用模板:
#   - school_life
#   - urban_romance
#   - fantasy_adventure
```

### `list-prompts` — 列出可用提示词

```bash
python -m src list-prompts
# 📋 可用提示词:
#   - comic_basic
#   - drama_basic
```

## 📝 示例输出

### 漫画脚本示例

输入：`python -m src generate --type comic --theme "校园日常"`

```markdown
# 漫画脚本: 校园日常

## 角色设定
- **主角:** 小明 - 性格开朗，有点迷糊 - 短发，校服，总是背着书包
- **配角:** 小红 - 性格温柔，学习好 - 长发，戴眼镜，文静

## 故事梗概
小明在图书馆不小心撞到了小红，发现她正在看一本神秘的书。
两人因此结缘，开始了一段有趣的校园冒险。

---

## 第1页

### 分镜1
- **场景:** 学校图书馆，阳光透过窗户洒进来
- **角色:** 小明
- **动作:** 匆忙跑进图书馆，差点撞到书架
- **表情:** 焦急，四处张望
- **对话:**
  - 小明: "完了完了，要迟到了！"

### 分镜2
- **场景:** 图书馆书架间
- **角色:** 小明，小红
- **动作:** 小明转身时撞到了正在看书的小红
- **对话:**
  - 小明: "啊！对不起对不起！"
  - 小红: "没...没关系..."
```

### 短剧脚本示例

输入：`python -m src generate --type drama --theme "都市爱情"`

```markdown
# 短剧脚本: 都市爱情

## 基本信息
- **剧名:** 《遇见》
- **类型:** 都市情感
- **集数:** 5集
- **每集时长:** 3分钟

## 角色设定
- **林小夏:** 女 - 25岁 - 平面设计师 - 性格独立，有点内向
- **陈阳:** 男 - 27岁 - 程序员 - 性格温和，有点木讷

---

## 第1集: 偶遇

### 场景1: 咖啡馆 - 白天

**林小夏** (坐在窗边，对着电脑发呆):
> "又是周末...不知道该做什么..."

**[门铃响]**

**陈阳** (走进咖啡馆，四处张望):
> "请问...还有位置吗？"

**[画外音]:** 两个陌生人的对话，就这样开始了...
```

## ⚙️ 配置详解

`config.yaml` 支持以下配置项：

```yaml
# AI模型配置
model:
  provider: "openai"          # 支持: openai / zhipu / mimo / deepseek
  api_key: "your-key"         # API 密钥
  base_url: "https://api.openai.com/v1"
  model_name: "gpt-3.5-turbo"

# 生成参数
generation:
  max_tokens: 2000            # 最大 token 数
  temperature: 0.8            # 创造性 (0.0-1.0，越高越有创意)
  language: "zh"              # 输出语言: zh(中文) / en(英文)
  default_type: "comic"       # 默认脚本类型: comic / drama

# 输出配置
output:
  format: "markdown"          # 输出格式: markdown / json / pdf
  save_path: "./output"       # 输出目录
  filename_pattern: "{theme}_{type}_{date}"

# 提示词配置
prompts:
  directory: "./prompts"
  default_comic: "comic_basic.yaml"
  default_drama: "drama_basic.yaml"

# 模板配置
templates:
  directory: "./templates"
  builtin:
    - "school_life"
    - "urban_romance"
    - "fantasy_adventure"
```

**参数调优建议：**

| 参数 | 低值效果 | 高值效果 | 推荐值 |
|------|---------|---------|--------|
| `temperature` | 输出更稳定、保守 | 输出更有创意、多样 | 0.7 ~ 0.9 |
| `max_tokens` | 输出较短 | 输出较长、更详细 | 1500 ~ 3000 |

## 🔧 提示词自定义

StoryForge 使用 YAML 格式的提示词模板，结构如下：

```yaml
name: "自定义漫画提示词"
type: comic
version: "1.0"

# 提示词模板 — 使用 {变量名} 占位
template: |
  你是一个专业的漫画脚本作家。请根据以下信息生成一个漫画脚本。

  主题: {theme}
  风格: {style}
  目标读者: {audience}
  页数: {pages}

  请按以下格式输出：
  ## 第X页
  ### 分镜1
  - **场景:** [画面描述]
  - **角色:** [出现的角色]
  - **对话:** [角色A]: "对话内容"

  要求：
  - 每页 3-5 个分镜
  - 对话简洁有力
  - 画面描述详细生动

# 预设参数（不指定时使用默认值）
defaults:
  style: "日常轻松"
  audience: "青少年"
  pages: 4

# 可选风格列表
styles:
  - "日常轻松"
  - "热血战斗"
  - "悬疑推理"
  - "浪漫爱情"
  - "奇幻冒险"
  - "搞笑幽默"
```

使用自定义提示词：

```bash
python -m src custom --prompt prompts/my_custom.yaml --theme "赛博朋克都市"
```

## 📁 项目结构

```
storyforge/
├── src/                          # 核心代码
│   ├── __init__.py               # 包初始化，版本信息
│   ├── __main__.py               # 入口点
│   ├── cli.py                    # CLI 命令定义 (Click)
│   ├── generator.py              # 脚本生成器核心类
│   ├── parser.py                 # 内容解析器
│   ├── exporter.py               # 格式导出器
│   └── config.py                 # 配置管理
├── prompts/                      # 提示词模板 (YAML)
│   ├── comic_basic.yaml          # 漫画基础提示词
│   ├── drama_basic.yaml          # 短剧基础提示词
│   └── custom.yaml               # 自定义提示词
├── templates/                    # 内容模板 (Markdown)
│   ├── school_life.md            # 校园日常
│   ├── urban_romance.md          # 都市爱情
│   └── fantasy_adventure.md      # 奇幻冒险
├── docs/                         # 文档
│   ├── api.md                    # API 文档
│   └── prompts_guide.md          # 提示词编写指南
├── examples/                     # 生成示例
│   ├── comic_example.md          # 漫画脚本示例
│   └── drama_example.md          # 短剧脚本示例
├── tests/                        # 测试
│   └── test_generator.py         # 生成器测试
├── config.example.yaml           # 配置文件模板
├── requirements.txt              # Python 依赖
├── CONTRIBUTING.md               # 贡献指南
├── LICENSE                       # MIT 许可证
└── README.md                     # 本文件
```

## 📚 文档

| 文档 | 说明 |
|------|------|
| [API 文档](docs/api.md) | ScriptGenerator 类 API 详细说明 |
| [提示词编写指南](docs/prompts_guide.md) | 如何编写和自定义提示词模板 |
| [贡献指南](CONTRIBUTING.md) | 如何参与项目开发 |

## 🤝 贡献指南

我们欢迎任何形式的贡献！无论是提交 Bug、建议功能，还是贡献代码。

### 快速开始

1. **Fork** 本仓库
2. **克隆** 你的 Fork：
   ```bash
   git clone https://github.com/your-username/storyforge.git
   cd storyforge
   ```
3. **创建特性分支**：
   ```bash
   git checkout -b feature/your-amazing-feature
   ```
4. **开发 & 测试**
5. **提交**（遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范）：
   ```bash
   git commit -m "feat: 添加 xxx 功能"
   ```
6. **推送 & 创建 PR**

### 提交信息规范

| 前缀 | 用途 | 示例 |
|------|------|------|
| `feat:` | 新功能 | `feat: 添加 PDF 导出功能` |
| `fix:` | 修复 Bug | `fix: 修复提示词加载失败的问题` |
| `docs:` | 文档更新 | `docs: 更新 README 安装步骤` |
| `style:` | 代码格式（不影响功能） | `style: 统一缩进为 4 空格` |
| `refactor:` | 重构 | `refactor: 提取配置加载为独立模块` |
| `test:` | 测试 | `test: 添加生成器单元测试` |
| `chore:` | 其他 | `chore: 更新依赖版本` |

### 代码规范

- 遵循 [PEP 8](https://peps.python.org/pep-0008/) 规范
- 使用类型注解（Type Hints）
- 编写清晰的文档字符串（Docstrings）
- 保持代码简洁可读

详细信息请查看 [CONTRIBUTING.md](CONTRIBUTING.md)。

## ❓ 常见问题

<details>
<summary><strong>Q: 支持哪些 AI 模型？</strong></summary>

StoryForge 支持所有兼容 OpenAI API 格式的模型，包括：
- **OpenAI** — `gpt-3.5-turbo`、`gpt-4`、`gpt-4o`
- **智谱AI** — `glm-4.5-air`、`glm-4.7`
- **MiMo** — `mimo-v2.5`
- **DeepSeek** — `deepseek-chat`、`deepseek-coder`

只需在 `config.yaml` 中修改 `provider`、`base_url` 和 `model_name` 即可切换。
</details>

<details>
<summary><strong>Q: 如何提高生成质量？</strong></summary>

1. **调整 `temperature`**：值在 0.7-0.9 之间通常效果最佳
2. **使用更详细的提示词**：自定义提示词模板可以精确控制输出
3. **选择更强的模型**：如 `gpt-4` 比 `gpt-3.5-turbo` 质量更高
4. **增加 `max_tokens`**：让 AI 有更多空间展开故事
</details>

<details>
<summary><strong>Q: 输出的脚本如何保存为 PDF？</strong></summary>

在 `config.yaml` 中设置：
```yaml
output:
  format: "pdf"
```
或者使用 `--output` 参数指定 `.pdf` 后缀的文件名。
</details>

<details>
<summary><strong>Q: 可以离线使用吗？</strong></summary>

StoryForge 需要调用 AI 模型 API，因此需要网络连接。但生成后的脚本文件是本地保存的，可以离线查看和编辑。
</details>

<details>
<summary><strong>Q: 如何创建自己的提示词模板？</strong></summary>

在 `prompts/` 目录下创建一个新的 `.yaml` 文件，按照现有模板的格式编写。详细的编写指南请参考 [docs/prompts_guide.md](docs/prompts_guide.md)。
</details>

## 🗺️ 路线图

| 阶段 | 功能 | 状态 |
|------|------|------|
| **v0.1.0** | 🏁 基础框架搭建 | ✅ 已完成 |
| | 核心生成器 (ScriptGenerator) | ✅ 已完成 |
| | CLI 命令行界面 | ✅ 已完成 |
| | 漫画/短剧脚本生成 | ✅ 已完成 |
| | YAML 提示词模板系统 | ✅ 已完成 |
| **v0.2.0** | 📊 内容增强 | 🚧 进行中 |
| | 完善 API 调用与流式输出 | 🔜 计划中 |
| | PDF 格式导出 | 🔜 计划中 |
| | JSON 格式导出 | 🔜 计划中 |
| | 内置模板库扩充 | 🔜 计划中 |
| **v0.3.0** | 🎨 可视化与交互 | 🔜 计划中 |
| | Web 界面 (Gradio/Streamlit) | 🔜 计划中 |
| | 脚本内容可视化预览 | 🔜 计划中 |
| | 交互式编辑与调整 | 🔜 计划中 |
| **v1.0.0** | 🚀 生产就绪 | 🔜 计划中 |
| | 多语言支持 (中/英) | 🔜 计划中 |
| | 批量生成能力 | 🔜 计划中 |
| | 插件系统 | 🔜 计划中 |
| | 完整测试覆盖 | 🔜 计划中 |

## 🔗 相关链接

| 资源 | 链接 |
|------|------|
| OpenAI Platform | [platform.openai.com](https://platform.openai.com/) |
| 智谱AI Platform | [open.bigmodel.cn](https://open.bigmodel.cn) |
| MiMo Platform | [token-plan-cn.xiaomimimo.com](https://token-plan-cn.xiaomimimo.com) |
| DeepSeek Platform | [platform.deepseek.com](https://platform.deepseek.com/) |

## ⭐ Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=your-username/storyforge&type=Date)](https://star-history.com/#your-username/storyforge&Date)

---

## 📄 License

本项目采用 [MIT License](LICENSE) 开源许可证。

---

<div align="center">

**StoryForge** — 让 AI 成为你的创作伙伴 🚀

Made with ❤️ by StoryForge Team

[⬆ 回到顶部](#-storyforge-)

</div>
