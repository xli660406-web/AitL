 
"""AitL - Agent 基类"""
from datetime import datetime

class BaseAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.log = []

    def think(self, prompt):
        # TODO: 接入MiMo API后替换
        response = f"[{self.name}] 收到指令，正在基于角色「{self.role}」进行推理..."
        self.log.append({
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "response": response
        })
        return response