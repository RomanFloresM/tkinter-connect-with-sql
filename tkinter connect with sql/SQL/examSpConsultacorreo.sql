IF OBJECT_ID('dbo.examSpConsultacorreo') > 0
  DROP PROCEDURE dbo.examSpConsultacorreo
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

CREATE PROCEDURE [dbo].[examSpConsultacorreo] @correo varchar(250), @pass varchar(max)
AS
BEGIN

	declare @hash varchar(max)

	select @hash = HASHBYTES('SHA2_256',CONVERT(NVARCHAR(32), @pass))


	select COUNT(*) from examusuario2 with(nolock)
	where Correo = @correo
	and pass = @hash
	and Estatus = 1

END