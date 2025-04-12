# System Patterns

## Kiến trúc hệ thống
Dự án sẽ tuân theo một cấu trúc đơn giản:

-   Thư mục gốc: Chứa `README.md`, `pyproject.toml` và các file cấu hình khác.
-   Thư mục `src`: Chứa code nguồn Python.
-   Thư mục `src/games`: Chứa code cho từng game cổ điển.
-   Thư mục `memory-bank`: Chứa các file Memory Bank.

## Các quyết định kỹ thuật chính
-   Sử dụng Pygame để phát triển game.
-   Sử dụng Poetry để quản lý dependencies.
-   Sử dụng docstring theo chuẩn reStructuredText.
-   Sử dụng type annotation.

## Design Patterns
-   Có thể sử dụng State Pattern cho logic của game.

## Mối quan hệ giữa các component
-   Mỗi game sẽ là một module độc lập trong thư mục `src/games`.
-   Các module của game Pong:
    -   `constants.py`: Chứa các hằng số.
    -   `paddle.py`: Chứa class `Paddle`.
    -   `ball.py`: Chứa class `Ball`.
    -   `game.py`: Chứa logic chính của game.
    -   `main.py`: File chạy chính, import và gọi `run_game` từ `game.py`.
