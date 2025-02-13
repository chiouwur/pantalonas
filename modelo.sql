BEGIN;

-- Create table 'tiendita_categoria'
CREATE TABLE tiendita_categoria (
    id_cat INTEGER PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    creado DATE NOT NULL,
    editado DATE NOT NULL
);

-- Create table 'tiendita_producto'
CREATE TABLE tiendita_producto (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(1000) NOT NULL,
    imagen VARCHAR(100),
    precio INTEGER NOT NULL,
    disponibilidad BOOLEAN NOT NULL,
    creado DATE NOT NULL,
    editado DATE NOT NULL,
    categorias_id INTEGER NOT NULL,
    FOREIGN KEY (categorias_id) REFERENCES tiendita_categoria(id_cat)
        DEFERRABLE INITIALLY DEFERRED
);

-- Index for foreign key 'categorias_id' in 'tiendita_producto'
CREATE INDEX tiendita_producto_categorias_id_index ON tiendita_producto (categorias_id);

COMMIT;
