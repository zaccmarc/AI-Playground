import requests
import json
import os
from pathlib import Path

OLLAMA_API_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "meu-coder"

def generate_documentation(file_path):

    print(f"🔍 Lendo o arquivo de código '{file_path}'...")
    if not os.path.exists(file_path):
        return f"ERRO: O arquivo '{file_path}' não foi encontrado."

    with open(file_path, 'r', encoding='utf-8') as f:
        code_content = f.read()

    prompt_template = f"""
    Sua tarefa é atuar como um desenvolvedor Python sênior e gerar documentação completa para o código fornecido.
    Adicione docstrings no padrão Google Python Style para o módulo e para cada função.

    A docstring de cada função deve incluir:
    - Uma breve descrição do que a função faz.
    - Uma seção `Args:` para descrever cada argumento.
    - Uma seção `Returns:` para descrever o valor de retorno.

    IMPORTANTE: Sua resposta deve ser SOMENTE o código Python completo com as docstrings adicionadas.
    Não inclua nenhuma outra palavra, explicação ou cabeçalho antes ou depois do bloco de código.

    Aqui está o código original:
    ```python
    {code_content}
    ```
    """

    print("🤖 Solicitando a geração de docstrings para o Dev-Assistant...")
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt_template}],
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        response_data = response.json()
        documented_code = response_data['message']['content']
        
        
        if documented_code.strip().startswith("```python"):
            documented_code = documented_code.strip()[9:].strip() # Remove ```python
            if documented_code.endswith("```"):
                documented_code = documented_code[:-3].strip() # Remove ``` no final

        original_path = Path(file_path)
        new_file_path = original_path.with_name(f"{original_path.stem}_doc.py")
        
        print(f"💾 Salvando o código documentado em '{new_file_path}'...")
        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(documented_code)

        return f"✅ Documentação gerada com sucesso e salva em '{new_file_path}'!"

    except requests.exceptions.RequestException as e:
        return f"ERRO ao conectar com o Ollama: {e}"

# Loop principal da ferramenta
print("=================================================")
print("📄   Auto-Documentador de Código Python   📄")
print("Use o comando: documentar <nome_do_arquivo.py>")
print("Exemplo: documentar processador.py")
print("Digite 'sair' para terminar.")
print("=================================================")

while True:
    user_input = input("\nComando> ")
    
    if user_input.lower() == 'sair':
        break
    
    if user_input.lower().startswith("documentar "):
        file_to_document = user_input.split(" ", 1)[1]
        result_message = generate_documentation(file_to_document)
        print(f"\n{result_message}")
    else:
        print("Comando inválido. Use 'documentar <nome_do_arquivo.py>' ou 'sair'.")