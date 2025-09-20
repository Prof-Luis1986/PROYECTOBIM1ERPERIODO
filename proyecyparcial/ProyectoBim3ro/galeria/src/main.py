import flet as ft


def main(page: ft.Page):
    page.title="Galeria"
    page.bgcolor=ft.Colors.BLACK45
    
    pinturas = [
        {
            "titulo": "La gioconda",
            "autor": "Leonardo Davinci.",
            "año": 1503,
            "descripcion": "famoso por la enigmática sonrisa de la retratada, probablemente Lisa Gherardini",
            "imagen": "https://raw.githubusercontent.com/Prof-Luis1986/PROYECTOBIM1ERPERIODO/refs/heads/main/GIOCONDA.jpeg"
        },
        {
            "titulo": "La Noche Estrellada",
            "autor": "Vincent van Gogh.",
            "año": 1889,
            "descripcion": "Cielo nocturno vibrante con remolinos y estrellas brillantes.",
            "imagen": "https://raw.githubusercontent.com/Prof-Luis1986/PROYECTOBIM1ERPERIODO/refs/heads/main/LA%20NOCHE%20ESTRELLADA.jpg"
        },
        {
            "titulo": "La Persistencia De La Memoria",
            "autor": "Salvador Dalí",
            "año": 1931 ,
            "descripcion": "Relojes blandos que desafían el tiempo en un paisaje onírico.",
            "imagen": "https://raw.githubusercontent.com/Prof-Luis1986/PROYECTOBIM1ERPERIODO/refs/heads/main/LA%20PERSISTENCIA%20DE%20LA%20MEMORIA.webp"
        },    
    ]
    
    indice_actual=[0]
    
    contenedor=ft.Container(
        content=ft.Column([]),
        width=400,
        height=500,
        bgcolor=ft.Colors.BLUE_400,
        alignment=ft.alignment.center,
        padding=20
    )
    
    boton_siguiente=ft.ElevatedButton(text="Siguiente Pintura")
    
    def mostrar_pintura():
        pintura=pinturas[indice_actual[0]]
        contenedor.content=ft.Column([
            ft.Image(src=pintura["imagen"],width=300,height=300,fit=ft.ImageFit.CONTAIN),
            ft.Text(pintura["titulo"],size=20,weight=ft.FontWeight.BOLD),
            ft.Text(f"Autor: {pintura['autor']}",size=16),
            ft.Text(f"Año: {pintura['año']}",size=16),
            ft.Text(pintura["descripcion"],size=14,italic=True)
        ],alignment=ft.MainAxisAlignment.CENTER)
        
        if indice_actual[0]==len(pinturas)-1:
            boton_siguiente.text="Volver al inicio"
        else:
            boton_siguiente.text="Siguiente pintura"
        page.update()
        
    def siguiente_click(e):
        indice_actual[0]=(indice_actual[0]+1)%len(pinturas)
        mostrar_pintura()    
    boton_siguiente.on_click=siguiente_click
    
    
    
    page.add(
        ft.Container(
            content=ft.Column([
                contenedor,
                boton_siguiente
            ],alignment=ft.MainAxisAlignment.CENTER,
              horizontal_alignment=ft.CrossAxisAlignment.CENTER,
              spacing=20                
        ),
            alignment=ft.alignment.center,
            expand=True
        )
    )
    mostrar_pintura()


ft.app(main)