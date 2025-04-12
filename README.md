# Classic Games POC

## Mô tả
Dự án này là một proof-of-concept (POC) cho một số game cổ điển được viết bằng Python và Pygame.

## Các game
-   Pong
-   Snake
-   Tetris

## Hướng dẫn cài đặt
1.  Cài đặt Python 3.x.
2.  Cài đặt Poetry.
3.  Clone repository.
4.  Chạy `poetry install` để cài đặt dependencies.

## Hướng dẫn chạy
1.  Chạy `poetry run python src/games/[tên game]/main.py` để chạy một game cụ thể.

## Cấu trúc dự án
```
.
├── README.md
├── pyproject.toml
├── src
│   └── games
│       ├── pong
│   │   │   └── main.py
│       ├── snake
│   │   │   └── main.py
│       └── tetris
│   │   │   └── main.py
└── memory-bank
    ├── projectbrief.md
    ├── productContext.md
    ├── activeContext.md
    ├── systemPatterns.md
    ├── techContext.md
    └── progress.md
