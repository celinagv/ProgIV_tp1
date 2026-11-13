from fastapi import APIRouter, HTTPException, status
from models.productos import (
     Producto, 
     UpdateProductoRequest, 
     GetProductosResponse,
     DeleteProductoResponse,
     CreateProductoResponse,
     PatchProductoRequest,
)
     

router = APIRouter()

productos: list[Producto] = [
    Producto(id=1, nombre="teclado", precio=25000.0, stock=10, categoria="perifericos"),
    Producto(id=2, nombre="monitor", precio=180000.0, stock=4, categoria="pantallas"),
]


@router.delete("/product/{id}")
def delete_producto(id: int) -> DeleteProductoResponse:
    for product in productos:
        if product.id == id:
            productos.remove(product)
            return DeleteProductoResponse(message="Producto borrado")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Producto no encontrado"
    )


@router.get("/product/{id}")
def get_producto(id: int) -> Producto:
    for product in productos:
        if product.id == id:
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Producto no encontrado"
    )


@router.get("/product")
def get_products(categoria: str | None = None) -> GetProductosResponse:
    if categoria is None:
        return GetProductosResponse(products=productos)

    filtrados = [p for p in productos if p.categoria.lower() == categoria.lower()]
    return GetProductosResponse(products=filtrados)



@router.put("/product/{id}")
def update_producto(id: int, datos: UpdateProductoRequest) -> Producto:
    for product in productos:
        if product.id == id:
            product.nombre = datos.nombre
            product.categoria = datos.categoria
            product.precio = datos.precio      
            product.stock = datos.stock       
            return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Producto no encontrado"
    )

@router.post("/product", status_code=status.HTTP_201_CREATED)
def create_producto(producto: Producto) -> CreateProductoResponse:
    for existente in productos:
        if existente.id == producto.id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Ya existe un producto con ese id"
            )

    productos.append(producto)
    return CreateProductoResponse(message="producto creado")

@router.patch("/product/{id}")
def patch_producto(id: int, datos: PatchProductoRequest) -> Producto:
    
    cambios = datos.model_dump(exclude_none=True)

    for product in productos:
        if product.id == id:
            for campo, valor in cambios.items():
                setattr(product, campo, valor)   
            return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Producto no encontrado",
    )