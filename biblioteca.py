import os
import flet as ft

# Listas globais para armazenar os dados
emprestimos = []
avaliacoesLivros = []
avaliacoesBiblioteca = []

def main(page: ft.Page):
    page.title = "Gerenciamento de Biblioteca"
    page.window_width = 600
    page.window_height = 400

    def cadastrar_emprestimo(page):
        def salvar_emprestimo(e):
            emprestimos.append({
                "livro": livro.value,
                "aluno": aluno.value,
                "data": data.value
            })
            page.snack_bar = ft.SnackBar(ft.Text("Empréstimo cadastrado com sucesso!"))
            page.snack_bar.open()
            page.go("/")

        livro = ft.TextField(label="Nome do Livro")
        aluno = ft.TextField(label="Nome do Aluno")
        data = ft.TextField(label="Data do Empréstimo")

        form = ft.Column([
            livro,
            aluno,
            data,
            ft.ElevatedButton("Salvar", on_click=salvar_emprestimo)
        ])

        page.clean()
        page.add(form)

    def avaliar_livro(page):
        def salvar_avaliacao(e):
            usuario = nome.value
            livro_avaliado = livro.value
            nota = avaliacao.value
            comentario = comentarios.value

            for emp in emprestimos:
                if emp["livro"] == livro_avaliado and emp["aluno"] == usuario:
                    avaliacoesLivros.append({
                        "usuario": usuario,
                        "livro": livro_avaliado,
                        "nota": nota,
                        "comentario": comentario
                    })
                    page.snack_bar = ft.SnackBar(ft.Text("Avaliação cadastrada com sucesso!"))
                    page.snack_bar.open()
                    page.go("/")
                    return

            page.snack_bar = ft.SnackBar(ft.Text("Erro: Livro não encontrado para o usuário!"))
            page.snack_bar.open()

        nome = ft.TextField(label="Nome do Usuário")
        livro = ft.TextField(label="Livro")
        avaliacao = ft.TextField(label="Nota (0-5)")
        comentarios = ft.TextField(label="Comentários")

        form = ft.Column([
            nome,
            livro,
            avaliacao,
            comentarios,
            ft.ElevatedButton("Salvar", on_click=salvar_avaliacao)
        ])

        page.clean()
        page.add(form)

    def avaliar_atendimento(page):
        def salvar_atendimento(e):
            avaliacoesBiblioteca.append({
                "usuario": nome.value,
                "nota": nota.value,
                "comentario": comentario.value
            })
            page.snack_bar = ft.SnackBar(ft.Text("Avaliação cadastrada com sucesso!"))
            page.snack_bar.open()
            page.go("/")

        nome = ft.TextField(label="Nome do Usuário")
        nota = ft.TextField(label="Nota (0-10)")
        comentario = ft.TextField(label="Comentários")

        form = ft.Column([
            nome,
            nota,
            comentario,
            ft.ElevatedButton("Salvar", on_click=salvar_atendimento)
        ])

        page.clean()
        page.add(form)

    def gerar_relatorio(page):
        relatorio_emprestimos = ft.Column([
            ft.Text(f"{i+1}. Livro: {emp['livro']}, Aluno: {emp['aluno']}, Data: {emp['data']}\n") for i, emp in enumerate(emprestimos)
        ])

        relatorio_avaliacoes = ft.Column([
            ft.Text(f"{i+1}. Livro: {av['livro']}, Usuário: {av['usuario']}, Nota: {av['nota']}, Comentário: {av['comentario']}\n") for i, av in enumerate(avaliacoesLivros)
        ])

        relatorio_atendimento = ft.Column([
            ft.Text(f"{i+1}. Usuário: {av['usuario']}, Nota: {av['nota']}, Comentário: {av['comentario']}\n") for i, av in enumerate(avaliacoesBiblioteca)
        ])

        page.clean()
        page.add(
            ft.Text("Relatório de Empréstimos", size=20), relatorio_emprestimos,
            ft.Text("Avaliações de Livros", size=20), relatorio_avaliacoes,
            ft.Text("Avaliações de Atendimento", size=20), relatorio_atendimento
        )

    menu = ft.Column([
        ft.ElevatedButton("Cadastrar Empréstimo", on_click=lambda _: cadastrar_emprestimo(page)),
        ft.ElevatedButton("Avaliar Livro", on_click=lambda _: avaliar_livro(page)),
        ft.ElevatedButton("Avaliar Atendimento", on_click=lambda _: avaliar_atendimento(page)),
        ft.ElevatedButton("Gerar Relatório", on_click=lambda _: gerar_relatorio(page))
    ])

    page.add(menu)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    ft.app(target=main, port=port)
