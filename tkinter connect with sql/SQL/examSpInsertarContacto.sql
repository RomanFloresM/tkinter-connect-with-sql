IF OBJECT_ID('dbo.examSpInsertarContacto') > 0
  DROP PROCEDURE dbo.examSpInsertarContacto
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

CREATE PROCEDURE [dbo].[examSpInsertarContacto] @telefono bigint, @usuario int
AS
BEGIN


	insert into contacto (Telefono, usuarioid)
	values(@telefono, @usuario)

END