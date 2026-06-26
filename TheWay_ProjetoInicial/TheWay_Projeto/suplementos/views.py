from django.http import HttpResponse

def recomendacao_view(request):
    # Isso envia o HTML direto do Python para o navegador
    cor_ceub = "#3d0a44"
    rosa_ceub = "#e5007d"
    
    html = f"""
    <body style="font-family: sans-serif; background: #f4f4f4; text-align: center; padding-top: 50px;">
        <h1 style="color: {cor_ceub};">TheWay - Suplementação</h1>
        <div style="background: white; display: inline-block; padding: 30px; border-radius: 10px; border-top: 5px solid {rosa_ceub}; shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <form method="POST">
                <input type="text" name="nome" placeholder="Seu Nome" style="padding: 10px; margin: 5px;"><br>
                <input type="number" name="peso" placeholder="Peso (kg)" style="padding: 10px; margin: 5px;"><br>
                <input type="number" step="0.01" name="altura" placeholder="Altura (ex: 1.75)" style="padding: 10px; margin: 5px;"><br>
                <button type="submit" style="background: {cor_ceub}; color: white; border: none; padding: 10px 20px; cursor: pointer; border-radius: 5px;">Gerar Recomendação</button>
            </form>
        </div>
    </body>
    """
    return HttpResponse(html)