from datetime import date
from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field

class Gabinete(BaseModel):
    nome: Optional[str] = Field(default=None, allow_none=True)
    predio: Optional[str] = Field(default=None, allow_none=True)
    sala: Optional[str] = Field(default=None, allow_none=True)
    andar: Optional[str] = Field(default=None, allow_none=True)
    telefone: Optional[str] = Field(default=None, allow_none=True)
    email: Optional[str]= Field(default=None, allow_none=True)

class UltimoStatus(BaseModel):
    id: int
    uri: HttpUrl
    nome: Optional[str] = Field(default=None, allow_none=True)
    siglaPartido: Optional[str] = Field(default=None, allow_none=True)
    uriPartido: Optional[HttpUrl] = Field(default=None, allow_none=True)
    siglaUf: Optional[str] = Field(default=None, allow_none=True)
    idLegislatura: int
    urlFoto: HttpUrl
    email: Optional[str] = Field(default=None, allow_none=True)
    data: Optional[date] = Field(default=None, allow_none=True)
    nomeEleitoral: str
    gabinete: Gabinete
    situacao: Optional[str] = Field(default=None, allow_none=True)
    condicaoEleitoral: Optional[str] = Field(default=None, allow_none=True)
    
    descricaoStatus: Optional[str] = Field(default=None, allow_none=True)

class Dados(BaseModel):
    id: int
    uri: HttpUrl
    nomeCivil: Optional[str] = Field(default=None, allow_none=True)
    ultimoStatus: UltimoStatus
    cpf: Optional[str] = Field(default=None, allow_none=True)
    sexo: Optional[str] = Field(default=None, allow_none=True)
    urlWebsite: Optional[str] = Field(default=None, allow_none=True)
    redeSocial: List[str]
    dataNascimento: Optional[date] = Field(default=None, allow_none=True)
    dataFalecimento: Optional[date] = Field(default=None, allow_none=True)
    ufNascimento: Optional[str] = Field(default=None, allow_none=True)
    municipioNascimento: Optional[str] = Field(default=None, allow_none=True)
    escolaridade: Optional[str] = Field(default=None, allow_none=True)

class Link(BaseModel):
    rel: Optional[str] = Field(default=None, allow_none=True)
    href: Optional[HttpUrl] = Field(default=None, allow_none=True)

class DeputadoUri(BaseModel):
    dados: Dados
    links: List[Link]
