# 贡献指南

感谢你对 StoryForge 的关注！我们欢迎任何形式的贡献。

## 如何贡献

### 1. 报告Bug

如果你发现了Bug，请创建一个Issue，包含：
- Bug描述
- 复现步骤
- 期望行为
- 实际行为
- 环境信息（Python版本、操作系统等）

### 2. 提交功能建议

如果有功能建议，请创建一个Issue，描述：
- 功能描述
- 使用场景
- 期望的实现方式

### 3. 提交代码

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建一个 Pull Request

## 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/your-username/storyforge.git
cd storyforge

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 配置
cp config.example.yaml config.yaml
# 编辑 config.yaml
```

## 代码规范

- 遵循 PEP 8 规范
- 使用类型注解
- 编写清晰的文档字符串
- 保持代码简洁

## 提交信息规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat:` 新功能
- `fix:` 修复Bug
- `docs:` 文档更新
- `style:` 代码格式（不影响功能）
- `refactor:` 重构
- `test:` 测试
- `chore:` 其他

## 许可证

贡献的代码将采用 MIT 许可证。
