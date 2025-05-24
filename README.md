# Simple Text Editor

A basic text editor built using Python and Tkinter. This project serves as an example of creating a simple GUI application for text manipulation.

## Features

*   **File Operations:**
    *   New File (Ctrl+N)
    *   Open File... (Ctrl+O) - Supports .txt, .py, and all file types.
    *   Save File (Ctrl+S)
    *   Save File As... (Ctrl+Shift+S)
    *   Exit (with unsaved changes prompt)
*   **Editing Operations:**
    *   Undo (Ctrl+Z)
    *   Redo (Ctrl+Y)
    *   Cut (Ctrl+X)
    *   Copy (Ctrl+C)
    *   Paste (Ctrl+V)
    *   Select All (Ctrl+A)
*   **Basic UI:**
    *   Scrollable text area.
    *   Menu bar for easy access to features.
    *   Window title updates with the current filename.
    *   Prompts for unsaved changes before closing or opening new files.



## Requirements

*   Python 3.x
*   Tkinter (usually included with standard Python installations)

## How to Run

1.  **Clone the repository (or download the source code):**
    ```bash
   https://github.com/oneaarmdeveloper/texteditor/edit.git
    cd texteditor
    ```
2.  **Ensure you have Python 3 installed.**
3.  **Run the script:**
    ```bash
    python texteditor.py
    ```

## How to Build an Executable (Optional)

If you want to create a standalone executable (e.g., an `.exe` for Windows):

1.  **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```
2.  **Navigate to the project directory in your terminal.**
3.  **Run PyInstaller:**
    *   For a single executable file with no console window (recommended for GUI apps):
        ```bash
        pyinstaller --onefile --windowed --name "SimpleTextEditor" my_text_editor.py
        ```
    *   (Optional: Add `--icon="your_icon.ico"` if you have an icon file)
4.  The executable will be located in the `dist` folder.

## Structure

*   `texteditor`: Main application script containing the `TextEditorApp` class and Tkinter UI logic.
    
  

## Potential Future Enhancements

*   Search and Replace functionality.
*   Line numbers.
*   Syntax highlighting for common languages.
*   Tabs for multiple open files.
*   Customizable fonts and themes.
*   Status bar (for line/column count, encoding, etc.).

## Contributing

Feel free to fork this project, make improvements, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open source and available under the [MIT License](LICENSE.md).
(If you don't have a LICENSE.md file, you can create one with the standard MIT license text or choose another license).
