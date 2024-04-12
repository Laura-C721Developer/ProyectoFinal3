<?php
include ('../../app/config/config.php');
include ('../../app/config/conexion.php');

include('../../layout/admin/sesion.php');
include('../../layout/admin/datos_sesion_user.php');
?>

<?php include ('../../layout/admin/parte1.php');?>
<div class="content-wrapper">
    <div class="content-header">
        <div class="container-fluid">
            <div class="row mb-2">
                <div class="col-sm-6">
                    <h1 class="m-0">Registro de una nueva Cita</h1>
                </div><!-- /.col -->
            </div><!-- /.row -->

            <div class="card">
                <div class="card-header" style="background-color:#1E90FF ;color: #ffffff">
                    LLene la información con mucho cuidado
                </div>
                <div class="card-body">
                    <form action="controller_create.php" method="post">
                        <div class="row">
                            <div class="col-md-4">
                                <div class="form-group">
                                    <label for="">Codigo</label><!-- este esta bie -->
                                    <input type="text" name="codigo" class="form-control">
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="form-group">
                                    <label for="">Centro medico</label><span style="color:red"><b>*</b></span><!-- este esta bie -->
                                    <input type="text" name="titulo" class="form-control" placeholder="Solo texto..."required >
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="form-group">
                                    <label for="">Hora</label><span style="color:red"><b>*</b></span><!-- este esta bie -->
                                    <input type="text" name="autor" class="form-control" placeholder="Solo texto..." required >
                                </div>
                            </div>
                        
                        </div>
                        <div class="row">
                            <div class="col-md-4">
                                <div class="form-group">
                                    <label for="">Nombre Completo</label><span style="color:red"><b>*</b></span><!-- este esta bie -->
                                    <input type="text" name="campo" class="form-control" placeholder="campo de estudio..."required>
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="form-group">
                                    <label for="">Sexo</label><!-- este esta bie -->
                                    <input type="text" name="editorial" class="form-control" placeholder=" Femenino o Masculino...">
                                </div>
                            </div>
                            <div class="col-md-4">

                                <div class="form-group">
                                    <label for="">Cedula</label><span style="color:red"><b>*</b></span>;<!-- este esta bie -->
                                    <input type="number" name="ano_publicacion" class="form-control" placeholder="Solo numeros..."required>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-3">
                                <div class="form-group">
                                    <label for="">Peso</label><!-- este esta bie -->
                                    <input type="text" name="nro_edicion" class="form-control" placeholder="Solo texto...">
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="form-group">
                                    <label for="">Edad</label><span style="color:red"><b>*</b></span><!-- este esta bien no tocar -->
                                    <input type="text" name="paginas" class="form-control" placeholder="Edad..."required>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="form-group">
                                    <label for="">Razon</label><span style="color:red"><b>*</b></span>
                                    <input type="texto" name="formato" class="form-control" placeholder="Razon de la consulta..."required>

                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="form-group">
                                    <label for="">Costo</label>
                                    <input type="texto" name="ejemplares" class="form-control" placeholder="Enfermedades anteriores...">
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="">Seguro</label><span style="color:red"><b>*</b></span>
                                    <input type="text" name="observaciones" class="form-control" placeholder="Solo texto..." required>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label for="">Cobertura</label><span style="color:red"><b>*</b></span>
                                    <input type="text" name="codigo_barra" class="form-control" placeholder="Solo numeros..."required>
                                </div>
                            </div>
                        </div>
                        <hr>                        
                        <div class="row">
                            <div class="col-md-2"></div>
                            <div class="col-md-4">
                                <center>
                                    <a href="<?php echo $URL."/admin/";?>" class="btn btn-secondary btn-block">Cancelar</a>
                                </center>
                            </div>
                            <div class="col-md-4">
                               <center>
                                   <button type="submit" onclick="return confirmar('Asegurece de llenar la información correcta');" class="btn btn-primary btn-block">Guardar</button>
                               </center>
                            <div class="col-md-2"></div>
                        </div>
                    </form>
                </div>
            </div>
</div>
        </div><!-- /.container-fluid -->
    </div>
</div>
<?php include ('../../layout/admin/parte2.php');?>


<!-- Button trigger modal del area -->


<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>