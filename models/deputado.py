from dataclasses import dataclass

@dataclass
class Deputado:
    id: int
    uri: str
    nome: str
    siglaPartido: str
    uriPartido: str
    siglaUf: str
    idLegislatura: int
    urlFoto: str
    email: str
