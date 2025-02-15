import redis

# 替换为你的Redis密码
#redis_password = "your_redis_password"
redis_password = 12345678

try:
    # 创建Redis连接，指定主机、端口和密码
    r = redis.Redis(host='localhost', port=6379, password=redis_password, decode_responses=True)

    print("成功连接到 Redis 服务器: localhost:6379")

    # 写入数据
    r.set('key3', 'value3')
    print("写入数据成功")

    # 读取数据
    value = r.get('key3')
    print(f"读取数据成功: {value}")
except redis.AuthenticationError:
    print("写入数据失败: Authentication required.")
except Exception as e:
    print(f"发生其他错误: {e}")
