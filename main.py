import flet as ft
import random
from time import sleep

occupied_spaces = ["", "", "", "", "", "", "", "", ""]
available_spaces = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
player_letter = ""
player_name = ""
player_color = ""
ai_letter = ""
ai_name = ""
ai_color = ""
player_points = 0
ai_points = 0
ties_points = 0

def main(page: ft.Page):
    page.title = "Tic Tac Toe"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_height = 600
    page.window_width = 500
#***************** Functions ************************
    def check_if_win(letter):
        global occupied_spaces
        if occupied_spaces[0] == letter and occupied_spaces[1] == letter and occupied_spaces[2] == letter:
            body.controls[0].bgcolor="yellow"
            body.controls[1].bgcolor="yellow"
            body.controls[2].bgcolor="yellow"
            return True
        elif occupied_spaces[3] == letter and occupied_spaces[4] == letter and occupied_spaces[5] == letter:
            body.controls[3].bgcolor="yellow"
            body.controls[4].bgcolor="yellow"
            body.controls[5].bgcolor="yellow"
            return True
        elif occupied_spaces[6] == letter and occupied_spaces[7] == letter and occupied_spaces[8] == letter:
            body.controls[6].bgcolor="yellow"
            body.controls[7].bgcolor="yellow"
            body.controls[8].bgcolor="yellow"
            return True
        elif occupied_spaces[0] == letter and occupied_spaces[3] == letter and occupied_spaces[6] == letter:
            body.controls[0].bgcolor="yellow"
            body.controls[3].bgcolor="yellow"
            body.controls[6].bgcolor="yellow"
            return True
        elif occupied_spaces[1] == letter and occupied_spaces[4] == letter and occupied_spaces[7] == letter:
            body.controls[1].bgcolor="yellow"
            body.controls[4].bgcolor="yellow"
            body.controls[7].bgcolor="yellow"
            return True
        elif occupied_spaces[2] == letter and occupied_spaces[5] == letter and occupied_spaces[8] == letter:
            body.controls[2].bgcolor="yellow"
            body.controls[5].bgcolor="yellow"
            body.controls[8].bgcolor="yellow"
            return True
        elif occupied_spaces[0] == letter and occupied_spaces[4] == letter and occupied_spaces[8] == letter:
            body.controls[0].bgcolor="yellow"
            body.controls[4].bgcolor="yellow"
            body.controls[8].bgcolor="yellow"
            return True
        elif occupied_spaces[2] == letter and occupied_spaces[4] == letter and occupied_spaces[6] == letter:
            body.controls[2].bgcolor="yellow"
            body.controls[4].bgcolor="yellow"
            body.controls[6].bgcolor="yellow"
            return True
        else:
            return False

    def set_ai():
        global ai_letter
        global ai_name
        global ai_color
        global ai_points
        global ties_points

        player_turn.visible = False
        ai_turn.visible = True
        index = int(random.choice(available_spaces))
        available_spaces.remove(str(index))
        occupied_spaces[index] = ai_letter
        body.controls[index].content = ft.Icon(name=ai_name, color=ai_color, size=70)
        body.controls[index].bgcolor="WHITE"
        body.controls[index].disabled = True
        page.update()
        if check_if_win(ai_letter):
            page.dialog = dlg_endgame
            dlg_endgame.title.value = "Ai Wins!"
            dlg_endgame.open = True
            ai_points = ai_points + 1
            ai_score.value = ai_points
            header.color=ai_color
            page.update()
            return
        if len(available_spaces) == 0:
            page.dialog = dlg_endgame
            dlg_endgame.title.value = "Draw!"
            dlg_endgame.open = True
            ties_points = ties_points + 1
            ties_score.value = ties_points
            page.update()
            return
 
        sleep(0.5)
        player_turn.visible = True
        ai_turn.visible = False
        page.update()

    def set_player(e):
        global player_letter
        global player_name
        global player_color
        global player_points
        global ties_points

        player_turn.visible = True
        ai_turn.visible = False
        index = e.control.data
        available_spaces.remove(str(index))
        occupied_spaces[index] = player_letter
        body.controls[index].content = ft.Icon(
            name=player_name, color=player_color, size=70
        )
        body.controls[index].bgcolor="WHITE"
        body.controls[index].disabled = True
        page.update()
        if check_if_win(player_letter):
            page.dialog = dlg_endgame
            dlg_endgame.title.value = "Player Wins!"
            dlg_endgame.open = True
            player_points = player_points + 1
            player_score.value = player_points
            header.color=player_color
            page.update()
            return

        if len(available_spaces) == 0:
            page.dialog = dlg_endgame
            dlg_endgame.title.value = "Draw!"
            dlg_endgame.open = True
            ties_points = ties_points + 1
            ties_score.value = ties_points
            page.update()
            return
        sleep(0.5)
        set_ai()

    def start_game():
        global player_letter
        global player_name
        global player_color
        global ai_letter
        global ai_name
        global ai_color

        # Always Starts X
        starts = random.choice(["player", "ai"])

        if starts == "player":
            player_letter = "X"
            player_name = ft.icons.CLOSE
            player_color = ft.colors.RED
            ai_letter = "O"
            ai_name = ft.icons.CIRCLE_OUTLINED
            ai_color = ft.colors.BLUE
            player_icon.name = player_name
            player_icon.color = player_color
            player_turn.bgcolor = player_color
            ai_icon.name = ai_name
            ai_icon.color = ai_color
            ai_turn.bgcolor = ai_color
            page.dialog = dlg_startgame
            dlg_startgame.title.value = f"Starts {starts}"
            dlg_startgame.open = True
            page.update()
            sleep(1)
            dlg_startgame.open = False
            header.color=ft.colors.WHITE
            page.update()

        else:
            player_letter = "O"
            player_name = ft.icons.CIRCLE_OUTLINED
            player_color = ft.colors.BLUE
            ai_letter = "X"
            ai_name = ft.icons.CLOSE
            ai_color = ft.colors.RED
            player_icon.name = player_name
            player_icon.color = player_color
            player_turn.bgcolor = player_color
            ai_icon.name = ai_name
            ai_icon.color = ai_color
            ai_turn.bgcolor = ai_color
            page.dialog = dlg_startgame
            dlg_startgame.title.value = f"Starts {starts}"
            dlg_startgame.open = True
            page.update()
            sleep(1)
            dlg_startgame.open = False
            header.color=ft.colors.WHITE
            page.update()
            set_ai()

    def new_game(e):
        global occupied_spaces
        global available_spaces
        dlg_endgame.open = False
        header.color=ft.colors.WHITE70
        page.update()
        sleep(0.5)
        available_spaces.clear()
        for i in range(0, 9):
            occupied_spaces[i] = ""
            available_spaces.append(str(i))
            body.controls[i].disabled = False
            body.controls[i].content = ft.Icon()
            body.controls[i].bgcolor="WHITE70"
        page.update()
        start_game()

#**************** UI Game **********************
    player_score = ft.Text("0", size=25)
    player_icon = ft.Icon()
    player_turn = ft.Container(height=10, width=100,border_radius=3, visible=False)
    ties_score = ft.Text("0", size=25)
    ai_score = ft.Text("0", size=25)
    ai_icon = ft.Icon()
    ai_turn = ft.Container(height=10, width=100,border_radius=3, visible=False)

    dlg_startgame = ft.AlertDialog(
        title=ft.Text(value="", text_align=ft.TextAlign.CENTER),
    )
    dlg_endgame = ft.AlertDialog(
        modal=True,
        title=ft.Text(value="", text_align=ft.TextAlign.CENTER),
        actions=[
            ft.TextButton("New Game", on_click=new_game),
            ft.TextButton("Exit", on_click=lambda e: page.window_destroy()),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    header=ft.Text(
        value="Tic Tac Toe",
        size=40,
        color=ft.colors.WHITE70,
        text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD
    )
    body = ft.GridView(
        width=300,
        height=300,
        runs_count=3,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
        controls=[
            ft.Container(bgcolor=ft.colors.WHITE70,border_radius=3, on_click=set_player, data=0),
            ft.Container(bgcolor=ft.colors.WHITE70,border_radius=3, on_click=set_player, data=1),
            ft.Container(bgcolor=ft.colors.WHITE70,border_radius=3, on_click=set_player, data=2),
            ft.Container(bgcolor=ft.colors.WHITE70,border_radius=3, on_click=set_player, data=3),
            ft.Container(bgcolor=ft.colors.WHITE70,border_radius=3, on_click=set_player, data=4),
            ft.Container(bgcolor=ft.colors.WHITE70,border_radius=3, on_click=set_player, data=5),
            ft.Container(bgcolor=ft.colors.WHITE70,border_radius=3, on_click=set_player, data=6),
            ft.Container(bgcolor=ft.colors.WHITE70,border_radius=3, on_click=set_player, data=7),
            ft.Container(bgcolor=ft.colors.WHITE70,border_radius=3, on_click=set_player, data=8),
        ],
    )
   
    footer=ft.Row(
        controls=[ft.Column(
        controls=[
            player_score,
            ft.Row(
                [player_icon, ft.Text("PLAYER")], alignment=ft.MainAxisAlignment.CENTER
            ),
            player_turn,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    ), ft.Column(
        controls=[ties_score, ft.Text("TIES"), ft.Container(height=10, width=100)],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    ), ft.Column(
        controls=[
            ai_score,
            ft.Row([ai_icon, ft.Text("AI")], alignment=ft.MainAxisAlignment.CENTER),
            ai_turn,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )],
        spacing=0,
        width=300,
        height=100,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.add(
        ft.Column(
            [header, body, footer],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    start_game()

if __name__ == "__main__":
    ft.app(target=main)