"""
StoryForge - AI内容创作工具
"""
import os
from pathlib import Path

__version__ = "0.1.0"
__author__ = "StoryForge Team"

# 项目根目录
ROOT_DIR = Path(__file__).parent.parent

# 配置文件路径
CONFIG_PATH = ROOT_DIR / "config.yaml"
CONFIG_EXAMPLE_PATH = ROOT_DIR / "config.example.yaml"

# 提示词目录
PROMPTS_DIR = ROOT_DIR / "prompts"

# 模板目录
TEMPLATES_DIR = ROOT_DIR / "templates"

# 输出目录
OUTPUT_DIR = ROOT_DIR / "output"

# 确保输出目录存在
OUTPUT_DIR.mkdir(exist_ok=True)
