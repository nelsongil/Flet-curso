from flet import *
import mysql.connector

#CONEXIÓN A LA BD
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mainan",
)
 
cursor = mydb.cursor()

def main(page:Page):
    page.scroll = True
    nametxt = TextField(label="Nombre")
    agetxt = TextField(label="Edad")
    
    # CREAR LA ENTRADA DE EDICION
    edit_nametxt = TextField(label="Nombre")
    edit_agetxt = TextField(label="Edad")    
    edit_id = Text()
    
    mydt = DataTable(
        width=700,
        bgcolor=colors.GREY_200,
        border=border.all(2, colors.GREY_400),
        border_radius=10,
        divider_thickness=0,
        vertical_lines=border.BorderSide(1, colors.GREY_400),
        horizontal_lines=border.BorderSide(1, colors.GREY_400),
        heading_row_color=colors.BLACK12,
        heading_row_height=50,
        columns=[
            DataColumn(Text("id")),
            DataColumn(Text("Nombre")),
            DataColumn(Text("Edad")),
            DataColumn(Text("Acciones")),
        ]
    )
    
    
    # DELETE BUTTON
    def deletebtn(e):
        print("El id seleccionado es = ", e.control.data["id"])
        try:
            sql = "DELETE FROM mainan WHERE id = %s"
            val = (e.control.data['id'],)
            cursor.execute(sql,val)
            mydb.commit()
            print("Borrado !!!")
            mydt.rows.clear()
            load_data()
            
            # MOSTRAR SNACKBAR
            page.snack_bar = SnackBar(
                Text("Datos eliminados satisfactoriamente", size=30, bgcolor="red")
            )
            page.snack_bar.open = True
            page.update()
            
        except Exception as e:
            print(e)
            print("error you code for delete")



    # CREAR DIALOG SHOW CUANDO CLICKAS EN EN EL BOTON EDITAR
    def savedata(e):
        try:
            sql = "UPDATE mainan SET age = %s, name = %s WHERE id = %s"
            val = (edit_agetxt.value,edit_nametxt.value,edit_id.value)
            cursor.execute(sql,val)
            mydb.commit()
            print("Edición de datos satisfactoria")
            dialog.open = False
            page.update()
            
            # LIMPIAR CAMPOS
            edit_nametxt.value = ""
            edit_agetxt.value = ""
            edit_id.value = ""  
            page.update()
            
            #Y LIMPIAMOS COLUMNAS EN LA TABAL Y INSERTAMOS EN LA BASE DE DATOS DE NUEVO
            mydt.rows.clear()
            load_data()
            
            # MOSTRAR SNACKBAR
            page.snack_bar = SnackBar(
                Text("Datos editados satisfactoriamente", size=30, bgcolor="green")
            )
            page.snack_bar.open = True
            page.update()    
            
        except Exception as e:
            print(e)
            print("ERROR SAVE EDIT !!!!")
   
    
    dialog = AlertDialog(
        title=Text("Editar Datos"),
        content=Column([
            edit_nametxt,
            edit_agetxt,
        ]),
        actions=[
            TextButton("Guardar", on_click=savedata)
        ]
    )            
            
    # EDIT BUTTON
    def editbtn(e):
        edit_nametxt.value = e.control.data['name']
        edit_agetxt.value = e.control.data['age']
        edit_id.value = e.control.data['id']
        page.dialog = dialog 
        dialog.open = True
        page.update()
    
    
    def load_data():
        #TOMAR LOS DATOS DE LA TABLA Y METERLOS EN LA DATATABLE
        cursor.execute("SELECT * FROM mainan")
        result = cursor.fetchall()
        
        # E INSERTAMOS LOS DATOS AL DICT
        columns = [Column[0] for Column in cursor.description]
        rows = [dict(zip(columns,Row)) for Row in result]
        
        # LOOP E INSERTAR
        for row in rows:
            mydt.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(row['id'])),
                        DataCell(Text(row['name'])),
                        DataCell(Text(row['age'])),
                        DataCell(
                            Row([
                                IconButton("delete",icon_color="red",data=row,on_click=deletebtn),
                                IconButton("create",icon_color="green",data=row,on_click=editbtn),
                            ])
                        )
                    ]
                )
            )
    
    
    #Y LLAMAR A LA FUNCION CUANDO SE ABRE POR PRIMERA VEZSnackBarpage.snack_bar
    load_data()
    
    def addtodb(e):
        try:
            sql = "INSERT INTO mainan (name,age) VALUES(%s,%s)"
            val = (nametxt.value, agetxt.value)
            cursor.execute(sql,val)
            mydb.commit()
            print(cursor.rowcount,"REGISTRO INSERTADO !!!")
            
            #Y LIMPIAMOS COLUMNAS EN LA TABAL Y INSERTAMOS EN LA BASE DE DATOS DE NUEVO
            mydt.rows.clear()
            load_data()
            
            # MOSTRAR SNACKBAR
            page.snack_bar = SnackBar(
                content=Text("Datos agregados satisfactoriamente", size=30, style=TextStyle(color=colors.GREEN_50), bgcolor=colors.GREEN_400),
                action="Ok!",
                duration=1000,
                bgcolor=colors.GREEN_400,
            )
            page.snack_bar.open = True
            page.update()
        
        except Exception as e:
            print(e)
            print("error you CODE!!!!")
            
        # DESPUÉS DEL INSERTAR SATISFACTORIAMENTE EN LA bd LIMPIAMOS LOS TEXTINPUT
        nametxt.value = ""
        agetxt.value = ""
        page.update()
        
    
    page.add(Column([nametxt, agetxt, ElevatedButton("Agregar a la base de datos", on_click=addtodb), mydt]))
   
app(target=main)

