class elementos:
    def __init__(self):
        pass

class materiais:
    def __init__(self, nome, fornecedor, estado_de_processamento, estado_fisico):
        self.nome = nome
        self.__fornecedor= fornecedor
        self.estado_de_processamento = materiais.verificação_de_estado_de_processamento(estado_de_processamento)
        self.estado_fisico = materiais.verificação_de_estado_de_fisico(estado_fisico)

    def verificação_de_estado_de_processamento(estado_de_processamento):
        estados_validos = ["processado", "não processado"]
        if estado_de_processamento in estados_validos:
            return estado_de_processamento
        else:
            return "Você inseriu um estado de processamento invalido"
        
    def verificação_de_estado_de_fisico(estado_fisico):
        estados_validos = ["plasma", "gasoso", "líquido", "sólido", "condensado de Bose-Einstein"]
        if estado_fisico in estados_validos:
            return estado_fisico
        else:
            return "Você inseriu um estado de processamento invalido"
        
    def apresentar_material(self):
        print(self.__class__.__name__)
        print(self.nome)
        print(self.estado_de_processamento)
        print(self.estado_fisico)
  
        pass

    def processar(self, tipo_de_material, processo, resultado):
        return  f"O {tipo_de_material}, {self.nome} foi processado através do processo de {processo} e adquiriu o formato do molde de {resultado}"
    
    def processabilidade(self, parametros_fisicos_aceitáveis):
        if self.estado_de_processamento == "não processado" and self.estado_fisico in parametros_fisicos_aceitáveis:
            pass
        else:
            return "O material não está em condições de processamento." 

class metal(materiais):
    def __init__ (self, nome, fornecedor, estado_de_processamento, estado_fisico, tipo_de_liga ):
        super().__init__(nome, fornecedor, estado_de_processamento, estado_fisico)
        self.tipo_de_liga = metal.verificação_de_tipo_de_liga(tipo_de_liga)

    def verificação_de_tipo_de_liga(tipo_de_liga):
        tipos_de_liga_validos = ["liga-ferrosa", "aço-carbono comum", "açoinoxidável", "liga-não-ferrosa"]
        if tipo_de_liga in tipos_de_liga_validos:
            return tipo_de_liga
        else: 
            return "Você inseriu uma liga inválida"
        
    def forjar(self, molde):
        materiais.processabilidade (self, ["líquido", "sólido"])
        self.estado_de_processamento = "processado"
        self.estado_fisico = "sólido"
        return materiais.processar(self, __class__.__name__, "forjar", molde)

    def laminar(self):
        materiais.processabilidade (self, ["sólido"])
        self.estado_de_processamento = "processado"
        self.estado_fisico = "sólido"
        return materiais.processar(self, __class__.__name__, "laminar", "chapa")

    def extrusar(self):
        materiais.processabilidade (self, ["sólido"])
        self.estado_de_processamento = "processado"
        self.estado_fisico = "líquido"
        return materiais.processar(self, __class__.__name__, "extrusar", "tubo")





aço = metal("aço 12000", "Guerdau", "não processado", "sólido", "açoinoxidável")
print(aço.apresentar_material())
print(aço.forjar("picareta"))
print(aço.__fornecedor)