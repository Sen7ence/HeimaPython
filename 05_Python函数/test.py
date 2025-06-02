def connect(**options):
    host = options.get("host", "localhost")
    port = options.get("port", 3306)
    print(f"连接数据库：{host}:{port}")

connect(host="127.0.0.1", port=5432)
connect()  # 使用默认值
