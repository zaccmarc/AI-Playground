class Aluno(Pessoa): # Classe herdada de Pessoa, que é a classe pai do objeto aluno (Aluno)
    """Classe para representar um aluno. Esta classe extende da classe 'Pessoa'.""" 
    
    def __init__(self, nome: str, idade: int, sexo: str, experiencia: float, login:str , totAssistido:int): # Método construtor que inicializa os atributos do objeto aluno. Todos os parâmetros são obrigatórios
        """Método construtor da classe Aluno.""" 
        
        super().__init__(nome, idade, sexo, experiencia) # Chamada ao método construtor da classe Pessoa para inicializar os atributos herdados. Todos os parâmetros são obrigatórios também (Pessoa: nome, idade, sexo e experiência).
        
        self._login = login # Atributo privado que armazena o valor do campo 'login' 
        """Atributo privado para armazenar a informação de Login."""  
      
        self.totAssistido= totAssistido# Atributos da classe Aluno, todos são inicializados com um dos valores passados como argumento (10 por padrão)  # Todos os parâmetros não obrigatórios e iniciaisizado em zero
        """Atributo privada para armazenar a informaçãp de Total Assistido."""  
    
    def viuMaisUm(self):# Método que incrementa o total assistido do aluno por um ponto e ganha experiência. Todos os parâmetros são obrigatórios  # Nenhum retorno, apenas atualiza a variável de instancia
        """Método que incrementa o total assistido do aluno por um ponto e ganha experiência."""  
        
    @property# Decorator para obter os valores dos atributos privados  # Não tem retorno, apenas permite acessar as variáveis de instância com o nome da propriedade (login) sem necessidade de chamar um método get.  
    def login(self):# Método que obtém e define os valores do atributos privado 'login'  # Não tem retorno, apenas permite acessar/modificar o valor atualizando (get_login) sem necessidade de chamar um método set.
        """Método para obter ou definir o login."""  
        
    @property# Decorator para obter os valores dos atributos privados  # Não tem retorno, apenas permite acessar as variáveis de instância com nome da propriedade (totAssistido) sem necessidade de chamar um método get.  
    def totAssistido(self):# Método que obtém e define os valores do atributos privado 'total assistido'  # Não tem retorno, apenas permite acessar/modificar o valor atualizando (get_totassistido) sem necessidade de chamar um método set.
        """Método para obter ou definir totalAssistido."""  
    
    def _setLogin(self, login:str):# Método que define os valores do atributo privado 'login'  # Não tem retorno e só pode ser chamada internamente. Todos parâmetros obrigatórios (nome)  
        """Método para definir o login."""   
    
    def _setTotAssistido(self, totassistido:int):# Método que define os valores do atributo privado 'total assistido'  # Não tem retorno e só pode ser chamada internamente. Todos parâmetros obrigatórios (valor)  
        """Método para definir o totalAssistido."""   
    
```     
Este é um exemplo de como você poderia fazer isso usando a docstring do Python, que serve pra documentar os módulos e funções em seu código. A ideia principal é deixar claro para quem vai ler o código (ou mesmo você) qual era sua intenção de usar aquele método ou classe naquela situação atual, assim como faz com a documentacao do projeto em si que foi feito.
````