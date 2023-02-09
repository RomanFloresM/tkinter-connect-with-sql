IF OBJECT_ID('dbo.examSpConsultaUsuario') > 0
  DROP PROCEDURE dbo.examSpConsultaUsuario
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

CREATE PROCEDURE [dbo].[examSpConsultaUsuario] @Nick varchar(250)
AS
BEGIN

	select
	Nickname,
	Correo
	from examusuario2 a with(nolock)
	where (a.Nickname like  '%'+@Nick+'%'
		or a.Correo like '%'+@Nick+'%')



END