import numpy as np
import os


# Función para leer el archivo de texto
def read_text_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# Función para dividir el texto en palabras
def split_into_words(text: str) -> list:
    return text.split()


# Función para dividir el texto en líneas según el ancho máximo especificado (inspirado en Word Wrap)
def word_wrap(text: str, maxWidth: int) -> list:
    words = text.split()
    n = len(words)
    dp = [float("inf")] * (n + 1)
    dp[0] = 0
    breaks = [0] * (n + 1)

    # Utilizando programación dinámica para calcular el mejor lugar para romper las líneas
    for i in range(1, n + 1):
        length = -1
        for j in range(i, 0, -1):
            length += len(words[j - 1]) + 1
            if length > maxWidth:
                break
            cost = dp[j - 1] + (maxWidth - length + 1) ** 2
            if cost < dp[i]:
                dp[i] = cost
                breaks[i] = j

    # Crear las líneas basadas en los cortes calculados
    lines = []
    i = n
    while i > 0:
        j = breaks[i]
        lines.insert(0, " ".join(words[j - 1 : i]))
        i = j - 1

    return lines


# Función para justificar el texto (inspirado en Longest Common Substring para encontrar las palabras más largas)
def justify_text(lines: list, maxWidth: int) -> list:
    justified_lines = []
    for line in lines:
        words = line.split()
        if len(words) == 1:
            justified_lines.append(words[0].ljust(maxWidth))
        else:
            total_spaces = maxWidth - sum(len(word) for word in words)
            spaces_between_words = len(words) - 1
            spaces = [" "] * spaces_between_words
            for i in range(total_spaces):
                spaces[i % spaces_between_words] += " "
            justified_line = "".join(
                word + space for word, space in zip(words, spaces + [""])
            )
            justified_lines.append(justified_line)
    return justified_lines


# Función principal para formatear el texto
def format_text(file_path: str, maxWidth: int) -> list:
    text = read_text_file(file_path)
    words = split_into_words(text)
    formatted_lines = word_wrap(" ".join(words), maxWidth)
    justified_lines = justify_text(formatted_lines, maxWidth)
    return justified_lines


# Función para guardar el texto formateado en un archivo
def save_to_file(file_path, text_lines):
    with open(file_path, "w", encoding="utf-8") as file:
        for line in text_lines:
            file.write(line + "\n")


# Función para crear un nuevo archivo
def create_file(file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("")


# Función para leer el contenido de un archivo
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        print(file.read())


# Función para actualizar un archivo existente
def update_file(file_path, maxWidth):
    formatted_text = format_text(file_path, maxWidth)
    save_to_file(file_path, formatted_text)


# Función para eliminar un archivo
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"El archivo {file_path} ha sido eliminado.")
    else:
        print(f"El archivo {file_path} no existe.")


# Interfaz de usuario para seleccionar las opciones y procesar el archivo
def main():
    print("Bienvenido al Justificador de Texto")
    print("Seleccione una opción:")
    print("1. Crear un nuevo archivo")
    print("2. Leer un archivo existente")
    print("3. Actualizar el archivo existente con el texto formateado")
    print("4. Eliminar un archivo existente")

    option = input("Ingrese el número de la opción deseada: ")
    file_path = input("Ingrese la ruta del archivo de texto: ")

    if option == "1":
        create_file(file_path)
        print(f"El archivo {file_path} ha sido creado.")
    elif option == "2":
        read_file(file_path)
    elif option == "3":
        maxWidth = int(input("Ingrese el ancho máximo de caracteres por línea: "))
        update_file(file_path, maxWidth)
        print(f"El archivo {file_path} ha sido actualizado con el texto formateado.")
    elif option == "4":
        delete_file(file_path)
    else:
        print("Opción no válida. Inténtelo de nuevo.")


if __name__ == "__main__":
    main()
