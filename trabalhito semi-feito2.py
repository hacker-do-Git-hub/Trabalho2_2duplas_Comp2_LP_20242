from mendeleev import element
class pesquisador:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf
    def verificação(caso, possibilidades):
        if caso in possibilidades:
            return caso
        else: 
            return "opção inválida"
    
    def __str__(self):
        return f'Olá, Me chamo {self.nome} e sou um(a) {self.__class__.__name__}'
class Docente(pesquisador):
    def __init__(self, nome, cpf, grau):
        super().__init__(nome, cpf)
        self.grau = pesquisador.verificação(grau, ["mestrado", "doutorado", "pós", "pós doutorado"])
        
    def acessar_fornecedores(self, material):
        return f'{self.nome} acessou que os fornecesores são {material.fornecedor} desse material.'
    
    def Alterar_fornecedor(self, material, novo_valor):
        material.fornecedor = novo_valor
        return f'{self.nome} alterou os fornecedores para serem os {material.fornecedor}'
    
    def __str__(self):
        return super().__str__() + f' com {self.grau}.'    
#Só o docente vai poder acessar e alterar os fornecedores
class Tecnico(pesquisador):
    def __init__(self, nome, cpf, especialidade):
        super().__init__(nome, cpf)
        self.especialidade = pesquisador.verificação(especialidade, ["cerâmicos", "metais", "polímeros"])
    
    def acessar_fornecedores(self,material):
        return 'Você não pode acessar os fornecedores, sendo Técnico(a)'
    def Alterar_fornecedor(self,):
        return 'Você não pode acessar os fornecedores, sendo Técnico(a)'

    def __str__(self):
        return super().__str__() + f'(a) com especialidade em {self.especialidade}.'
class Materiais:
    def __init__(self, nome, fornecedor, estado_de_processamento, estado_fisico):
        self.nome = nome
        self.__fornecedor= fornecedor
        self.estado_de_processamento = Materiais.verificação(estado_de_processamento, ["processado", "não processado"])
        self.estado_fisico = Materiais.verificação(estado_fisico, ["plasma", "gasoso", "líquido", "sólido", "condensado de Bose-Einstein"])
        
    def apresentar_material(self):
        return f'{self.__class__.__name__}\n{self.nome}\n{self.estado_de_processamento}\n{self.estado_fisico}'
    def processar(self, tipo_de_material, processo, resultado):
        return  f"O {tipo_de_material}, {self.nome} foi processado através do processo de {processo} e adquiriu o formato do molde de {resultado}"
    
    def processabilidade(self, parametros_fisicos_aceitáveis):
        if self.estado_de_processamento == "não processado" and self.estado_fisico in parametros_fisicos_aceitáveis:
            pass
        else:
            return "O material não está em condições de processamento." 
        
    def verificação(caso, possibilidades):
        if caso in possibilidades:
            return caso
        else: 
            return "opção inválida"
        
    @property
    def fornecedor(self):
        return self.__fornecedor
    @fornecedor.setter
    def fornecedor(self, novo_fornecedor):
        self.__fornecedor = novo_fornecedor
        return self.__fornecedor
    
class metal(Materiais):
    def __init__ (self, nome, fornecedor, estado_de_processamento, estado_fisico, tipo_de_liga):
        super().__init__(nome, fornecedor, estado_de_processamento, estado_fisico)
        self.tipo_de_liga = Materiais.verificação(tipo_de_liga, ["liga-ferrosa", "aço-carbono comum", "açoinoxidável", "liga-não-ferrosa"])
        self.composicao = metal.definir_composição(tipo_de_liga)
        
    def definir_composição(tipo_de_liga):
        carbono = element("C")
        níquel = element("Ni")
        ferro = element("Fe")
        if tipo_de_liga == "liga-ferrosa":
            return ferro
        elif tipo_de_liga == "aço-carbono comum":
            return [carbono, ferro]
        elif tipo_de_liga == "açoinoxidável":
            return [carbono, ferro, níquel]
        
        
    def forjar(self, molde):
        Materiais.processabilidade (self, ["líquido", "sólido"])
        self.estado_de_processamento = "processado"
        self.estado_fisico = "sólido"
        return Materiais.processar(self, __class__.__name__, "forjar", molde)
    def laminar(self):
        Materiais.processabilidade (self, ["sólido"])
        self.estado_de_processamento = "processado"
        self.estado_fisico = "sólido"
        return Materiais.processar(self, __class__.__name__, "laminar", "chapa")
    def extrusar(self):
        Materiais.processabilidade (self, ["sólido"])
        self.estado_de_processamento = "processado"
        self.estado_fisico = "líquido"
        return Materiais.processar(self, __class__.__name__, "extrusar", "tubo")
class polimero(Materiais):
    def __init__(self, nome, fornecedor, estado_de_processamento, estado_fisico, disposição, propriedade_termica):
        super().__init__(nome, fornecedor, estado_de_processamento, estado_fisico)
        self.disposição = Materiais.verificação(disposição, ["pellets", "fibra", "filme", "solução", "filamento", "objeto"])
        self.propriedade_termica = Materiais.verificação(propriedade_termica, ["termoplástico", "termorígido"])
    def  extrusar(self):
        if Materiais.processabilidade (self, ["sólido"]) and Materiais.verificação(self.disposição,["fibra", "filme"]):
            self.estado_de_processamento = "processado"
            self.estado_fisico = "sólido"
            return Materiais.processar(self, __class__.__name__, "extrusar", "bobina")
        
        elif Materiais.processabilidade (self, ["sólido"]) and Materiais.verificação(self.disposição, ["pellets"]):
            self.estado_de_processamento = "processado"
            self.estado_fisico = "sólido"
            self.disposição = "filamento"
            return Materiais.processar(self, __class__.__name__, "extrusar", "filamento")
        
    def casting(self, matriz):
        Materiais.processabilidade (self, ["líquido"]) and Materiais.verificação(self.disposição, ["solução"])
        self.estado_de_processamento = "processado"
        self.estado_fisico = "sólido"
        return Materiais.processar(self, __class__.__name__, "casting", matriz)
        
    def impressão_3D(self, modelo_digital):
        Materiais.verificação(self.estado_fisico, ["sólido"]) and Materiais.verificação(self.disposição, ["filamento"]) and Materiais.verificação(self.propriedade_termica, ["termoplástico"])
        self.disposição = "objeto"
        return Materiais.processar(self, __class__.__name__, "impressão 3D", modelo_digital)
    
class ceramico(Materiais):
    def __init__(self, nome, fornecedor, estado_de_processamento, estado_fisico, disposição, tipo_de_aplicabilidade, temperatura_maxima, temperatura_minima):
        super().__init__(nome, fornecedor, estado_de_processamento, estado_fisico)
        self.disposição = Materiais.verificação(disposição, ["pó", "lama", "arenoso", "fita", "lamina"])
        self.tipo_de_aplicabilidade = Materiais.verificação(tipo_de_aplicabilidade, ["clássica", "avançada"])
        self.temperatura_maxima = int(temperatura_maxima)
        self.temperatura_minima = int(temperatura_minima)
    def slip_casting(self, molde):
        Materiais.verificação(self.estado_fisico, ["sólido"]) and Materiais.verificação(self.disposição, ["pó"])
        self.disposição = "objeto"
        return Materiais.processar(self, __class__.__name__, "slip casting", molde)
        
    def tape_casting(self):
        if Materiais.verificação(self.estado_fisico, ["sólido"]) and Materiais.verificação(self.disposição, ["lama"]) and Materiais.verificação(self.tipo_de_aplicabilidade, ["clássica"]):
            self.disposição = "lamina"
            return Materiais.processar(self, __class__.__name__, "slip casting", "fita")
        elif Materiais.verificação(self.estado_fisico, ["sólido"]) and Materiais.verificação(self.disposição, ["lama"]) and Materiais.verificação(self.tipo_de_aplicabilidade, ["avançada"]):
            self.disposição = "objeto"
            return Materiais.processar(self, __class__.__name__, "slip casting", "capacitor")
    
    def sinterização(self, molde, temperatura_aplicada):
        Materiais.verificação(self.estado_fisico, ["sólido"]) and Materiais.verificação(self.disposição, ["arenoso"])
        self.disposição = "objeto"
        if self.temperatura_maxima <= temperatura_aplicada:
            condição_da_peça = "Excesso de calor a peça sofreu danos"
        elif self.temperatura_minima >= temperatura_aplicada:
            condição_da_peça = "Falta de calor aplicado, a peça não sinterizou devidamente"
        else:
            condição_da_peça = "Peça em boas condições"
        return Materiais.processar(self, __class__.__name__, "sinterização", molde) , condição_da_peça
    

PET = polimero("PET", "Eplast", "não processado", "sólido", "pellets", "termoplástico")
print(PET.propriedade_termica)
print(PET.extrusar())
print(PET.impressão_3D("troféu da Semana Metalmat"))
CdT = ceramico("Carboneto de Tugstênio", "Greystonealloys", "não processado", "sólido", "arenoso", "avançada", 280, 200)
print(CdT.sinterização("vaso", 250))
Marysilvia =Docente('Marysilvia', 123456,'mestrado')
Fernanda_Montenegro = Tecnico('Fernanda Montenegro', 1322321,'cerâmicos')
print(Fernanda_Montenegro)
print(Marysilvia)
print(PET.fornecedor)
print(Fernanda_Montenegro.acessar_fornecedores(PET))
print(Marysilvia.acessar_fornecedores(PET))
print(Marysilvia.Alterar_fornecedor(PET,'Petrobras'))
print(PET.fornecedor)