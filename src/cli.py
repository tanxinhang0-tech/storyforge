"""
StoryForge CLI - 命令行界面
"""
import click
import yaml
from pathlib import Path
from src.generator import ScriptGenerator


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """StoryForge - AI驱动的内容创作工具"""
    pass


@cli.command()
@click.option("--type", "-t", 
              type=click.Choice(["comic", "drama"]), 
              default="comic",
              help="脚本类型: comic(漫画) / drama(短剧)")
@click.option("--theme", "-m", 
              required=True,
              help="主题")
@click.option("--style", "-s", 
              default=None,
              help="风格")
@click.option("--pages", "-p", 
              default=4,
              help="页数/集数")
@click.option("--output", "-o", 
              default=None,
              help="输出文件路径")
def generate(type, theme, style, pages, output):
    """生成脚本"""
    click.echo(f"🎬 StoryForge - 生成{type}脚本")
    click.echo(f"📝 主题: {theme}")
    
    # 加载生成器
    try:
        gen = ScriptGenerator()
        
        # 构建参数
        params = {"theme": theme, "pages": pages}
        if style:
            params["style"] = style
        
        # 生成提示词
        prompt = gen.generate_prompt(type, **params)
        
        click.echo(f"✅ 提示词生成完成")
        click.echo(f"📊 提示词长度: {len(prompt)} 字符")
        
        # 这里实际会调用API生成脚本
        # 暂时只输出提示词
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(f"# 生成的提示词\n\n{prompt}\n")
            click.echo(f"💾 提示词已保存到: {output}")
        else:
            click.echo("\n--- 提示词预览 ---\n")
            click.echo(prompt[:500] + "..." if len(prompt) > 500 else prompt)
        
    except FileNotFoundError as e:
        click.echo(f"❌ 错误: {e}", err=True)
    except Exception as e:
        click.echo(f"❌ 生成失败: {e}", err=True)


@cli.command()
@click.option("--prompt", "-p", 
              required=True,
              help="提示词文件路径")
@click.option("--theme", "-m", 
              required=True,
              help="主题")
@click.option("--output", "-o", 
              default=None,
              help="输出文件路径")
def custom(prompt, theme, output):
    """使用自定义提示词生成"""
    click.echo(f"🎨 自定义提示词生成")
    click.echo(f"📝 主题: {theme}")
    
    try:
        # 加载自定义提示词
        prompt_file = Path(prompt)
        if not prompt_file.exists():
            click.echo(f"❌ 提示词文件不存在: {prompt}", err=True)
            return
        
        with open(prompt_file, "r", encoding="utf-8") as f:
            prompt_data = yaml.safe_load(f)
        
        # 格式化提示词
        template = prompt_data["template"]
        params = prompt_data.get("defaults", {})
        params["theme"] = theme
        
        formatted_prompt = template.format(**params)
        
        click.echo(f"✅ 自定义提示词生成完成")
        
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(f"# 自定义提示词生成\n\n{formatted_prompt}\n")
            click.echo(f"💾 提示词已保存到: {output}")
        else:
            click.echo("\n--- 提示词预览 ---\n")
            click.echo(formatted_prompt[:500] + "..." if len(formatted_prompt) > 500 else formatted_prompt)
        
    except Exception as e:
        click.echo(f"❌ 生成失败: {e}", err=True)


@cli.command()
def list_templates():
    """列出可用模板"""
    click.echo("📋 可用模板:\n")
    
    templates_dir = Path("templates")
    if not templates_dir.exists():
        click.echo("❌ 模板目录不存在")
        return
    
    for template_file in templates_dir.glob("*.md"):
        click.echo(f"  - {template_file.stem}")


@cli.command()
def list_prompts():
    """列出可用提示词"""
    click.echo("📋 可用提示词:\n")
    
    prompts_dir = Path("prompts")
    if not prompts_dir.exists():
        click.echo("❌ 提示词目录不存在")
        return
    
    for prompt_file in prompts_dir.glob("*.yaml"):
        click.echo(f"  - {prompt_file.stem}")


if __name__ == "__main__":
    cli()
