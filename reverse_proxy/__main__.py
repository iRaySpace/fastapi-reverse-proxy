import uvicorn
from reverse_proxy.app.config import init_config, get_config


def main() -> None:
    init_config()
    uvicorn.run(
        'reverse_proxy.app.boot:get_app',
        host='0.0.0.0',
        port=get_config('port') or 8000,
        reload=True,
    )


if __name__ == '__main__':
    main()
