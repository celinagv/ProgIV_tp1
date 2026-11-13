from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    stock: int
    categoria: str

class UpdateProductoRequest(BaseModel):   # sin id: el id va en la ruta
    nombre: str
    precio: float
    stock: int
    categoria: str

class GetProductosResponse(BaseModel):
    products: list[Producto]


class DeleteProductoResponse(BaseModel):
    message: str

class CreateProductoResponse(BaseModel):
    message: str

class PatchProductoRequest(BaseModel):
    nombre: str | None = None
    precio: float | None = None
    stock: int | None = None
    categoria: str | None = None