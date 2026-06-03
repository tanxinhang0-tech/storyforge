"""
StoryForge 脚本生成器
"""
import yaml
from pathlib import Path
from typing import Optional
from datetime import datetime


class ScriptGenerator:
    """脚本生成器核心类"""
    
    def __init__(self, config_path: str = "config.yaml"):
        """初始化生成器"""
        self.config = self._load_config(config_path)
        self.prompts_dir = Path(self.config.get("prompts", {}).get("directory", "./prompts"))
        self.templates_dir = Path(self.config.get("templates", {}).get("directory", "./templates"))
    
    def _load_config(self, config_path: str) -> dict:
        """加载配置文件"""
        config_file = Path(config_path)
        if not config_file.exists():
            raise FileNotFoundError(f"配置文件不存在: {config_path}")
        
        with open(config_file, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    
    def _load_prompt(self, prompt_type: str) -> dict:
        """加载提示词模板"""
        prompt_file = self.prompts_dir / f"{prompt_type}_basic.yaml"
        if not prompt_file.exists():
            raise FileNotFoundError(f"提示词模板不存在: {prompt_file}")
        
        with open(prompt_file, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    
    def _load_template(self, template_name: str) -> str:
        """加载内容模板"""
        template_file = self.templates_dir / f"{template_name}.md"
        if not template_file.exists():
            raise FileNotFoundError(f"内容模板不存在: {template_file}")
        
        with open(template_file, "r", encoding="utf-8") as f:
            return f.read()
    
    def generate_prompt(self, 
                       prompt_type: str, 
                       theme: str, 
                       **kwargs) -> str:
        """生成完整的提示词"""
        prompt_data = self._load_prompt(prompt_type)
        template = prompt_data["template"]
        defaults = prompt_data.get("defaults", {})
        
        # 合并参数
        params = {**defaults, **kwargs, "theme": theme}
        
        # 格式化模板
        try:
            return template.format(**params)
        except KeyError as e:
            raise ValueError(f"提示词模板缺少参数: {e}")
    
    def save_script(self, 
                   script: str, 
                   theme: str, 
                   script_type: str,
                   output_format: str = "markdown") -> str:
        """保存生成的脚本"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{theme}_{script_type}_{timestamp}.{output_format}"
        output_path = Path(self.config.get("output", {}).get("save_path", "./output"))
        output_path.mkdir(exist_ok=True)
        
        filepath = output_path / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(script)
        
        return str(filepath)
