from app import app              # importa o objeto Flask do app.py


def test_health():
    cliente = app.test_client()          # 1. Preparar: um "navegador falso" do Flask
    resposta = cliente.get("/health")      # 2. Agir: faz a requisição na rota

    assert resposta.status_code == 200   # 3. Verificar: respondeu com sucesso?
    assert resposta.get_json() == {"status": "ok"}   # e o conteúdo é o esperado?

def test_version_padrao(monkeypatch):
    monkeypatch.delenv("APP_VERSION", raising=False)
    cliente = app.test_client()          # 1. Preparar: um "navegador falso" do Flask
    resposta = cliente.get("/version")

    assert resposta.status_code == 200   # 3. Verificar: respondeu com sucesso?
    assert resposta.get_json() == {"version": "dev"}

def test_version_com_variavel(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "1.0.0")  # Define a variável de ambiente para o teste
    cliente = app.test_client()          # 1. Preparar: um "navegador falso" do Flask
    resposta = cliente.get("/version")   # 2. Agir: faz a requisição na rota

    assert resposta.status_code == 200   # 3. Verificar: respondeu com sucesso?
    assert resposta.get_json() == {"version": "1.0.0"}   # e o conteúdo é o esperado?