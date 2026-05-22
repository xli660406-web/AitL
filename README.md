# AitL - Adversary-in-the-Loop

> 基于多Agent协作的自动化渗透测试框架

## 解决的痛点

现有自动扫描工具只能做规则匹配，发现不了逻辑漏洞和多步攻击链。专业渗透测试太贵，中小团队负担不起。AitL 利用多Agent协作和长链推理，自动完成从资产识别到漏洞验证的完整渗透测试流程。

## 核心架构

```

[目标URL/代码仓库]
↓
[资产识别Agent] → 提取API端点、参数、认证逻辑
↓
[红蓝对抗环]
├── Red Team Agent (攻击构思)
├── Blue Team Agent (防御验证)
└── Arbiter Agent (危害判定)
↓ (多轮迭代，串联低危漏洞为高危攻击链)
[渗透测试报告]

```

## 技术栈

- 编排框架: LangGraph / AutoGen
- LLM: MiMo (主力推理) + 本地模型 (辅助)
- 工具链: Python, Docker, OWASP ZAP API
- 目标漏洞类型: SQL注入、XSS、SSRF、JWT伪造、越权、业务逻辑漏洞

## 当前进度

- [x] Red Team / Blue Team 对话环路原型
- [x] 单Agent SQL注入检测验证
- [ ] 多步攻击链长链推理 (急需Token)
- [ ] 完整渗透测试报告自动生成
- [ ] 50+场景覆盖测试

## 快速开始

```bash
git clone https://github.com/他的用户名/AitL.git
cd AitL
pip install -r requirements.txt
python main.py
```

---

本项目全程开源，目标是让每个开发者都能免费获得专业级安全检查。

