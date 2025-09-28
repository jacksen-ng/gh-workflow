# gh-workflow

## 概要
- こちらのレポジトリは、GitHub Workflowの勉強用サンプルです。Dockerを使ってコードを動かし、GitHub Actionsで自動化する流れをまとめています。

## 使用技術
- フレームワーク：FastAPI / Uvicorn
- プログラミング言語：Python 3.13
- 自動化：GitHub Actions / Docker / MakeFile
- Lintチェック：Ruff

##　Quick Start
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