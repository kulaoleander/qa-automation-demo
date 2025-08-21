# QA Automation Demo (Selenium + Pytest)

![CI](https://github.com/kulaoleander/qa-automation-demo/actions/workflows/ci.yml/badge.svg)

这是一个 **自动化测试示例项目**，用 Python + Selenium + Pytest 编写。  
特点：一键运行测试 ➜ 生成 HTML 报告 ➜ GitHub Actions 自动执行。

---

## 功能说明
- **UI 测试**  
  - Bing 搜索  
  - HerokuApp 登录（正确/错误场景）  
  - Saucedemo 电商加购  

- **技术点**  
  - Page Object Model (POM) 结构  
  - `pytest-html` 自动生成报告  
  - 日志与等待，提升稳定性  
  - GitHub Actions CI：push 代码后自动运行

---

## 本地运行

```bash
# 1) 创建虚拟环境（Windows）
python -m venv .venv
.venv\Scripts\activate

# 2) 安装依赖
pip install -r requirements.txt

# 3) 运行所有测试并生成报告
pytest -q --html=reports/report.html --self-contained-html
