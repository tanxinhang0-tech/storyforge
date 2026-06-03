# StoryForge 🎬

> AI驱动的内容创作工具 — 一键生成漫画脚本、漫剧短剧脚本

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI Compatible](https://img.shields.io/badge/OpenAI-Compatible-green.svg)](https://platform.openai.com/)

## 📖 项目简介

StoryForge 是一个基于AI的内容创作工具，支持：

- 🎨 **漫画脚本生成** — 一键生成分镜脚本、角色设定、对话内容
- 🎬 **漫剧/短剧脚本生成** — 生成完整的短剧剧本，包含场景、对白、动作指导
- ⚙️ **自定义提示词** — 用户可配置AI提示词，精确控制输出风格
- 📝 **多种模板** — 内置多种内容模板，覆盖不同类型

## ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🤖 多模型支持 | 支持OpenAI、MiMo、智谱等多种AI模型 |
| 🎯 精确控制 | 自定义提示词，控制内容风格和方向 |
| 📦 一键生成 | 输入主题，自动生成完整脚本 |
| 🎨 可视化预览 | 支持脚本内容的可视化展示 |
| 💾 多格式导出 | 支持Markdown、JSON、PDF等格式导出 |

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/your-username/storyforge.git
cd storyforge

# 安装依赖
pip install -r requirements.txt

# 配置API密钥
cp config.example.yaml config.yaml
# 编辑 config.yaml 填入你的API密钥
```

### 使用

```bash
# 生成漫画脚本
python -m storyforge generate --type comic --theme "校园日常" --output output.md

# 生成短剧脚本
python -m storyforge generate --type drama --theme "都市爱情" --output output.md

# 使用自定义提示词
python -m storyforge generate --type comic --prompt prompts/custom_comic.yaml
```

## 📁 项目结构

```
storyforge/
├── src/                    # 核心代码
│   ├── generator.py        # 脚本生成器
│   ├── parser.py           # 内容解析器
│   ├── exporter.py         # 格式导出器
│   └── config.py           # 配置管理
├── prompts/                # 提示词模板
│   ├── comic_basic.yaml    # 漫画基础提示词
│   ├── drama_basic.yaml    # 短剧基础提示词
│   └── custom.yaml         # 自定义提示词
├── templates/              # 内容模板
│   ├── school_life.md      # 校园日常
│   ├── urban_romance.md    # 都市爱情
│   └── fantasy_adventure.md # 奇幻冒险
├── docs/                   # 文档
│   ├── api.md              # API文档
│   ├── prompts_guide.md    # 提示词指南
│   └── templates_guide.md  # 模板指南
├── examples/               # 示例
├── tests/                  # 测试
├── requirements.txt        # 依赖
├── config.example.yaml     # 配置示例
└── README.md               # 项目说明
```

## ⚙️ 配置

### config.yaml

```yaml
# AI模型配置
model:
  provider: openai  # openai / zhipu / mimo
  api_key: "your-api-key-here"
  base_url: "https://api.openai.com/v1"  # 或其他平台地址
  model_name: "gpt-3.5-turbo"  # 或 glm-4.5-air / mimo-v2.5

# 生成配置
generation:
  max_tokens: 2000
  temperature: 0.8
  language: "zh"  # zh / en

# 输出配置
output:
  format: markdown  # markdown / json / pdf
  save_path: "./output"
```

## 📝 提示词自定义

### 示例：漫画脚本提示词

```yaml
name: "自定义漫画提示词"
type: comic
template: |
  你是一个专业的漫画脚本作家。请根据以下主题生成一个4-6页的漫画脚本。
  
  主题: {theme}
  风格: {style}
  目标读者: {audience}
  
  请按以下格式输出：
  ## 第X页
  **场景描述:** [详细的画面描述]
  **角色:** [出现的角色]
  **对话:** [角色A]: "对话内容"
  **表情/动作:** [角色的表情或动作]
  **旁白:** [如有]
  
  要求：
  - 每页3-5个分镜
  - 对话简洁有力
  - 画面描述详细生动
```

## 🤝 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

## 📄 License

MIT License - 详见 [LICENSE](LICENSE)

## 🔗 相关链接

- [OpenAI Platform](https://platform.openai.com/)
- [MiMo Platform](https://token-plan-cn.xiaomimimo.com)
- [智谱AI Platform](https://open.bigmodel.cn)

---

**StoryForge** — 让AI成为你的创作伙伴 🚀
