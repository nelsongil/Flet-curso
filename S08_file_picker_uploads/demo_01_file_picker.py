import flet as ft



def main(page: ft.Page):
    # Pick files dialog
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    # Save file dialog
    def save_file_result(e: ft.FilePickerResultEvent):
        save_file_path.value = e.path if e.path else "Cancelled!"
        save_file_path.update()

    save_file_dialog = ft.FilePicker(on_result=save_file_result)
    save_file_path = ft.Text()

    # Open directory dialog
    def get_directory_result(e: ft.FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Cancelled!"
        directory_path.update()

    get_directory_dialog = ft.FilePicker(on_result=get_directory_result)
    directory_path = ft.Text()

    # hide all dialogs in overlay
    page.overlay.extend([pick_files_dialog, save_file_dialog, get_directory_dialog])

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ]
        ),
        ft.Row(
            [
                ft.ElevatedButton(
                    "Save file",
                    icon=ft.icons.SAVE,
                    on_click=lambda _: save_file_dialog.save_file(),
                    disabled=page.web,
                ),
                save_file_path,
            ]
        ),
        ft.Row(
            [
                ft.ElevatedButton(
                    "Open directory",
                    icon=ft.icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(),
                    disabled=page.web,
                ),
                directory_path,
            ]
        ),
    )


ft.app(target=main)