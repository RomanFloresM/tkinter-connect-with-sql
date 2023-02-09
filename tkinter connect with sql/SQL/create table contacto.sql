create TABLE contacto (
 id INT not null identity(1000,1),
 RegistroFecha DATE,
 Telefono varchar(10),
 UsuarioId int
);

 ALTER TABLE contacto 
ADD CONSTRAINT PK_contacto_Id
PRIMARY KEY CLUSTERED (Id)

 ALTER TABLE contacto 
ADD CONSTRAINT FK_contacto_UsuarioId
FOREIGN KEY(UsuarioId)
REFERENCES usuario (Id)

 ALTER TABLE contacto 
  ADD CONSTRAINT contacto_RegistroFecha
    DEFAULT GETDATE() FOR RegistroFecha


	select * from examusuario2