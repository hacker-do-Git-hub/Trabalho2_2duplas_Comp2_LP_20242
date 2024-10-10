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

class Docente(pesquisador):
    def __init__(self, nome, cpf, grau):
        super().__init__(nome, cpf)
        self.grau = pesquisador.verificação(grau, ["mestrado", "doutorado", "pós", "pós doutorado"])
        
#Só o docente vai poder acessar e alterar os fornnecedores


class Tecnico(pesquisador):
    def __init__(self, nome, cpf, especialidade):
        super().__init__(nome, cpf)
        self.especialidade = pesquisador.verificação(especialidade, ["cerâmicos", "metais", "polímeros"])
        pass
#Só o técnico será capaz de processar os materiais


class materiais:
    def __init__(self, nome, fornecedor, estado_de_processamento, estado_fisico):
        self.nome = nome
        self.__fornecedor= fornecedor
        self.estado_de_processamento = materiais.verificação(estado_de_processamento, ["processado", "não processado"])
        self.estado_fisico = materiais.verificação(estado_fisico, ["plasma", "gasoso", "líquido", "sólido", "condensado de Bose-Einstein"])
        
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
        
    def verificação(caso, possibilidades):
        if caso in possibilidades:
            return caso
        else: 
            return "opção inválida"

class metal(materiais):
    def __init__ (self, nome, fornecedor, estado_de_processamento, estado_fisico, tipo_de_liga):
        super().__init__(nome, fornecedor, estado_de_processamento, estado_fisico)
        self.tipo_de_liga = materiais.verificação(tipo_de_liga, ["liga-ferrosa", "aço-carbono comum", "açoinoxidável", "liga-não-ferrosa"])
        self.composicao = metal.definir_composição(tipo_de_liga)

   # def verificação_de_tipo_de_liga(tipo_de_liga):
       # return 
        
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

class polimero(materiais):
    def __init__(self, nome, fornecedor, estado_de_processamento, estado_fisico, disposição, propriedade_termica):
        super().__init__(nome, fornecedor, estado_de_processamento, estado_fisico)
        self.disposição = materiais.verificação(disposição, ["pellets", "fibra", "filme", "solução", "filamento", "objeto"])
        self.propriedade_termica = materiais.verificação(propriedade_termica, ["termoplástico", "termorígido"])

    def  extrusar(self):
        if materiais.processabilidade (self, ["sólido"]) and materiais.verificação(self.disposição,["fibra", "filme"]):
            self.estado_de_processamento = "processado"
            self.estado_fisico = "sólido"
            return materiais.processar(self, __class__.__name__, "extrusar", "bobina")
        
        elif materiais.processabilidade (self, ["sólido"]) and materiais.verificação(self.disposição, ["pellets"]):
            self.estado_de_processamento = "processado"
            self.estado_fisico = "sólido"
            self.disposição = "filamento"
            return materiais.processar(self, __class__.__name__, "extrusar", "filamento")
        
    def casting(self, matriz):
        materiais.processabilidade (self, ["líquido"]) and materiais.verificação(self.disposição, ["solução"])
        self.estado_de_processamento = "processado"
        self.estado_fisico = "sólido"
        return materiais.processar(self, __class__.__name__, "casting", matriz)
        
    def impressão_3D(self, modelo_digital):
        materiais.verificação(self.estado_fisico, ["sólido"]) and materiais.verificação(self.disposição, ["filamento"]) and materiais.verificação(self.propriedade_termica, ["termoplástico"])
        self.disposição = "objeto"
        return materiais.processar(self, __class__.__name__, "impressão 3D", modelo_digital)
    
class ceramico(materiais):
    def __init__(self, nome, fornecedor, estado_de_processamento, estado_fisico, disposição, tipo_de_aplicabilidade, temperatura_maxima, temperatura_minima):
        super().__init__(nome, fornecedor, estado_de_processamento, estado_fisico)
        self.disposição = materiais.verificação(disposição, ["pó", "lama", "arenoso", "fita", "lamina"])
        self.tipo_de_aplicabilidade = materiais.verificação(tipo_de_aplicabilidade, ["clássica", "avançada"])
        self.temperatura_maxima = int(temperatura_maxima)
        self.temperatura_minima = int(temperatura_minima)

    def slip_casting(self, molde):
        materiais.verificação(self.estado_fisico, ["sólido"]) and materiais.verificação(self.disposição, ["pó"])
        self.disposição = "objeto"
        return materiais.processar(self, __class__.__name__, "slip casting", molde)
        
    def tape_casting(self):
        if materiais.verificação(self.estado_fisico, ["sólido"]) and materiais.verificação(self.disposição, ["lama"]) and materiais.verificação(self.tipo_de_aplicabilidade, ["clássica"]):
            self.disposição = "lamina"
            return materiais.processar(self, __class__.__name__, "slip casting", "fita")
        elif materiais.verificação(self.estado_fisico, ["sólido"]) and materiais.verificação(self.disposição, ["lama"]) and materiais.verificação(self.tipo_de_aplicabilidade, ["avançada"]):
            self.disposição = "objeto"
            return materiais.processar(self, __class__.__name__, "slip casting", "capacitor")
    
    def sinterização(self, molde, temperatura_aplicada):
        materiais.verificação(self.estado_fisico, ["sólido"]) and materiais.verificação(self.disposição, ["arenoso"])
        self.disposição = "objeto"
        if self.temperatura_maxima <= temperatura_aplicada:
            condição_da_peça = "Excesso de calor a peça sofreu danos"
        elif self.temperatura_minima >= temperatura_aplicada:
            condição_da_peça = "Falta de calor aplicado, a peça não sinterizou devidamente"
        else:
            condição_da_peça = "Peça em boas condições"
        return materiais.processar(self, __class__.__name__, "sinterização", molde) , condição_da_peça
    
aço = metal("aço 12000", "Guerdau", "não processado", "sólido", "açoinoxidável")
print(aço.apresentar_material())
print(aço.forjar("picareta"))
print(aço.composicao[0].description)

PET = polimero("PET", "Eplast", "não processado", "sólido", "pellets", "termoplástico")
print(PET.propriedade_termica)
print(PET.extrusar())
print(PET.impressão_3D("troféu da Semana Metalmat"))

CdT = ceramico("Carboneto de Tugstênio", "Greystonealloys", "não processado", "sólido", "arenoso", "avançada", 280, 200)
print(CdT.sinterização("vaso", 250))