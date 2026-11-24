🌐 [English](README.md) | **Português (BR)**

# Plataforma de Análise de Dados

Plataforma de análise educacional construída com Python, Flask, Pandas, NumPy e scikit-learn.

## Funcionalidades

- Ingestão e validação de CSV.
- Limpeza e normalização de dados.
- KPIs de vendas e resumos de séries temporais.
- Rankings de produtos e regiões.
- Previsão de vendas de referência com regressão linear.
- API REST em Flask.
- Dashboard leve no navegador.
- Testes unitários para ETL, métricas, previsão e comportamento da API.

## Executar localmente

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -e ".[dev]"
python -m analytics_platform
```

Abra `http://localhost:5000`.

## API

- `GET /health`
- `GET /api/summary`
- `GET /api/sales?region=Southeast`
- `GET /api/forecast?days=7`

## Exemplo

```bash
curl http://localhost:5000/api/summary
curl "http://localhost:5000/api/forecast?days=7"
```

## Arquitetura

- `etl.py`: carga, validação, limpeza e transformação.
- `metrics.py`: KPIs e análises agrupadas.
- `forecast.py`: modelo de previsão de referência.
- `app.py`: aplicação Flask e rotas da API.
- `templates/`: apresentação do dashboard.

Este é um projeto educacional. As previsões são ilustrativas e não devem ser usadas como aconselhamento empresarial ou financeiro.

## Histórico de desenvolvimento

Este projeto foi desenvolvido localmente entre 26/11/2025 e 18/09/2026. O histórico de commits foi criado depois, e as datas dos commits foram ajustadas para corresponder ao período em que o trabalho foi realmente feito.
