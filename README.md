# gh-workflow

## 概要
- こちらのレポジトリは、GitHub Workflowの勉強用サンプルです。Dockerを使ってコードを動かし、GitHub Actionsで自動化する流れをまとめています。

## 対象
- DockerやGitHubActionsをこれから学びたい初心者
- 「とりあえず触ってみたい」という人向けのサンプル

## 使用技術
- フレームワーク：FastAPI / Uvicorn
- プログラミング言語：Python 3.13
- 自動化：GitHub Actions / Docker / MakeFile
- Lintチェック：Ruff

## Quick Start
>[!NOTE]
>MacOSを対象

- リポをクロン
```bash
git clone https://github.com/jacksen-ng/gh-workflow.git
```

- Dockerを起動した後に
```bash
make up
```
アクセス：http://localhost:8000

- Lintだけ実行
```bash
make lint
```

## プロジェクト構成
```
gh-workflow/
├── .github/
│   ├── workflows/
│   │    ├──backend-lint.yml
│   ├──pull_request_template.md
├── backend/
│   ├── main.py              
│   ├── pyproject.toml       
│   ├── uv.lock
│   ├── .python-version         
│   ├── Dockerfile         
│   └── .dockerignore      
├── Makefile                
└── README.md   
```

## 資料説明
- [GitHub WorkFlowとDocker開発について](https://docs.google.com/presentation/d/1dKcBYzYtlVj2aJtbFXlSOzT1Ur6JWX0fcRJwsaPlGZI/edit?usp=sharing)

