from dataclasses import dataclass
from typing import List


@dataclass
class Deputado:
    uri: str
    nome: str
    idLegislaturaInicial: int
    idLegislaturaFinal: int
    nomeCivil: str
    siglaSexo: str
    urlRedeSocial: List[str]
    urlWebsite: List[str]
    dataNascimento: str
    dataFalecimento: str
    ufNascimento: str
    municipioNascimento: str