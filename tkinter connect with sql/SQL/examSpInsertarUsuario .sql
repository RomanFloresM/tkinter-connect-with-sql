IF OBJECT_ID('dbo.examSpInsertarUsuario') > 0
  DROP PROCEDURE dbo.examSpInsertarUsuario
GO

SET DATEFIRST 7
SET ANSI_NULLS ON
SET ANSI_WARNINGS ON
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET LOCK_TIMEOUT - 1
SET QUOTED_IDENTIFIER OFF
SET NOCOUNT ON
SET IMPLICIT_TRANSACTIONS OFF
GO

CREATE PROCEDURE [dbo].[examSpInsertarUsuario] @Nick varchar(250), @mail varchar(250), @pass varchar(max)
AS
BEGIN

	declare @hash varchar(max)

	select @hash = HASHBYTES('SHA2_256',CONVERT(NVARCHAR(32), @pass))

	insert into examusuario2 (Nickname, Correo, pass)
	values(@Nick, @mail, @hash)


END