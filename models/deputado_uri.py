from datetime import date
from typing import List, Optional
from pydantic import BaseModel, HttpUrl

class Gabinete(BaseModel):
    nome: Optional[str]
    predio: Optional[str]
    sala: Optional[str]
    andar: Optional[str]
    telefone: Optional[str]
    email: Optional[str]

class UltimoStatus(BaseModel):
    id: int
    uri: HttpUrl
    nome: str
    siglaPartido: str
    uriPartido: Optional[HttpUrl]
    siglaUf: str
    idLegislatura: int
    urlFoto: HttpUrl
    email: Optional[str]
    data: date 
    nomeEleitoral: str
    gabinete: Gabinete
    situacao: str
    condicaoEleitoral: str
    descricaoStatus: str

class Dados(BaseModel):
    id: int
    uri: HttpUrl
    nomeCivil: str
    ultimoStatus: UltimoStatus
    cpf: str
    sexo: str
    urlWebsite: Optional[HttpUrl]
    redeSocial: List[str]
    dataNascimento: date
    dataFalecimento: Optional[date] 
    ufNascimento: str
    municipioNascimento: str
    escolaridade: str

class Link(BaseModel):
    rel: str
    href: HttpUrl

class DeputadoUri(BaseModel):
    dados: Dados
    links: List[Link]
