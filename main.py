from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

def main():
    # 1. 初始化模型
    # model 参数需与你 ollama list 中的名称一致
    llm = ChatOllama(
        model="qwen3:8b",
        temperature=0.8,
        # 如果你的 Ollama 不在默认端口，可以指定 base_url
        # base_url="http://localhost:11434"
    )

    # 2. 简单的对话示例
    print("--- 正在请求本地 Ollama 模型 ---")
    
    question = "请用三句话解释什么是 LangChain？"
    
    # 使用 invoke 方法调用
    response = llm.invoke([
        HumanMessage(content=question)
    ])

    # 3. 打印结果
    print("\nAI 的回答：")
    print(response.content)

if __name__ == "__main__":
    main()