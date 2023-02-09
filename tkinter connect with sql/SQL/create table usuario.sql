create TABLE examusuario2 (
 Id int not null identity(1000,1),
 Nickname varchar(50),
 Correo varchar(50) unique,
 RegistroFecha DATE,
 pass  varchar(250) not null,
 estatus bit default 1
 );

 ALTER TABLE examusuario2 
ADD CONSTRAINT PK_usuario_Id
PRIMARY KEY CLUSTERED (Id)

 ALTER TABLE examusuario2 
  ADD CONSTRAINT usuario_RegistroFecha
    DEFAULT GETDATE() FOR RegistroFecha
