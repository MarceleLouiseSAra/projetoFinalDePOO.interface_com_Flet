from flet import *

DEEPBLUE = '#432350'
MEDIUMBLUE = '#b476ff'
PINK = '#f4c9fd'
WHITE = '#ffffff'
LIGHTBLUE = '#B0C4DE'

page: Page

def view_log_in_page(page: Page) -> Container:

    log_in_page = Container(
        width = 400,
        height = 850,
        bgcolor = DEEPBLUE,
        border_radius = 20,
        margin = 10,
        padding = 10,
        alignment = alignment.center,

        content = Column(
            width = 400,
            controls = [
                Row([
                    Container(
                        Icon(icons.ARROW_BACK_IOS_NEW_ROUNDED, color = LIGHTBLUE),
                        margin = margin.only(left = 15, right = 10, top = 20),
                        on_click = lambda _: page.go('/'),
                    ),
                    Container(
                        width = 100,
                        margin = margin.only(left = 215, right = 10, top = 20),
                        content = TextButton(
                            "Criar conta",
                            style = ButtonStyle(
                                color = LIGHTBLUE,
                                bgcolor = DEEPBLUE
                            ),
                            on_click = lambda _: page.go('/sign_in_page'),
                        ),
                    )
                ]),
                Container(
                    width = 400,
                    margin = margin.only(left = 150, right = 10, top = 30),
                    content = Text(
                        "Log in",
                        size = 30,
                        color = LIGHTBLUE,
                        weight = 'w700'
                    )
                ),
                Container(
                    width = 400,
                    margin = margin.only(left = 10, right = 10, top = 30),
                    alignment = alignment.center,
                    content = Text(
                        "Por favor, preencha as informações a seguir:",
                        size = 16,
                        color = LIGHTBLUE,
                        text_align = "center"
                    )
                ),
                Container(
                    width = 400,
                    margin = margin.only(left = 20, right = 20, top = 30),
                    content = Column(
                        controls = [
                            TextField(
                                label = "Nome de usuário",
                                hint_text = "Insira aqui o seu nome de usuário: ",
                                border_color = MEDIUMBLUE,
                                text_style = TextStyle(
                                    color = MEDIUMBLUE
                                ),
                                focused_border_color = PINK
                            )
                        ]
                    )
                ),
                Container(
                    width = 400,
                    margin = margin.only(left = 20, right = 20, top = 15),
                    content = Column(
                        controls = [
                            TextField(
                                label = "Senha",
                                hint_text = "Insira a sua senha aqui: ",
                                password = True,
                                can_reveal_password = True,
                                border_color = MEDIUMBLUE,
                                text_style = TextStyle(
                                    color = MEDIUMBLUE
                                ),
                                focused_border_color = PINK
                            )
                        ]
                    )
                ),
                Container(
                    width = 200,
                    margin = margin.only(left = 90, right = 20, top = 15),
                    content = TextButton(
                        "Esqueceu a senha?"
                    )
                ),
                Container(
                    width = 100,
                    margin = margin.only(left = 140, right = 20, top = 10),
                    content = TextButton(
                        "Entrar",
                        style = ButtonStyle(
                            color = {
                                ControlState.HOVERED: LIGHTBLUE,
                                ControlState.FOCUSED: WHITE,
                                ControlState.DEFAULT: PINK,
                            },
                            bgcolor = MEDIUMBLUE
                        ),
                        on_click = lambda _: page.go('/home_page')
                    )
                )
            ]
        )
    )

    return (log_in_page)