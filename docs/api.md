# StoryForge API 文档

## 核心类

### ScriptGenerator

脚本生成器核心类，负责加载配置、生成提示词、保存脚本。

#### 初始化

```python
from src.generator import ScriptGenerator

gen = ScriptGenerator(config_path="config.yaml")
```

#### 方法

##### generate_prompt

生成完整的提示词。

```python
prompt = gen.generate_prompt(
    prompt_type="comic",  # comic / drama
    theme="校园日常",       # 主题
    style="日常轻松",       # 风格（可选）
    pages=4                # 页数（可选）
)
```

**参数:**
- `prompt_type` (str): 提示词类型，`comic` 或 `drama`
- `theme` (str): 主题
- `style` (str, 可选): 风格
- `pages` (int, 可选): 页数/集数

**返回:** str - 格式化后的提示词

##### save_script

保存生成的脚本。

```python
filepath = gen.save_script(
    script="生成的脚本内容",
    theme="校园日常",
    script_type="comic",
    output_format="markdown"
)
```

**参数:**
- `script` (str): 脚本内容
- `theme` (str): 主题
- `script_type` (str): 脚本类型
- `output_format` (str): 输出格式

**返回:** str - 保存的文件路径

## 配置管理

### config.yaml

主配置文件，包含模型、生成、输出等配置。

```yaml
model:
  provider: "openai"
  api_key: "your-api-key"
  base_url: "https://api.openai.com/v1"
  model_name: "gpt-3.5-turbo"

generation:
  max_tokens: 2000
  temperature: 0.8
  language: "zh"
```

### prompts/*.yaml

提示词配置文件，定义了脚本生成的模板和参数。

## 扩展

### 添加新的提示词类型

1. 在 `prompts/` 目录创建新的 YAML 文件
2. 按照现有格式定义模板和参数
3. 在 `config.yaml` 中配置默认提示词

### 添加新的模板

1. 在 `templates/` 目录创建新的 Markdown 文件
2. 定义模板内容
3. 在 `config.yaml` 中注册模板
