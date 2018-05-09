'testing code'

import orm, uuid
from models import User, Blog, Comment
import asyncio


async def test():
    # 创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
    await orm.create_pool(loop=loop, host='192.168.147.129', user='root', password='mysql', db='awesome')

    # 没有设置默认值的一个都不能少
    u = User(name='dflhuang', email=uuid.uuid4().hex + '@qq.com', passwd='0123', image='about:blank')

    await u.save()


async def findAll():
    await orm.create_pool(loop=loop, host='192.168.147.129', user='root', password='mysql', db='awesome')
    print("------------")
    users = await User.findAll(limit=(0, 10))
    for user in users:
        print(user)


# 获取EventLoop:
loop = asyncio.get_event_loop()

# for i in range(10):
#     # 把协程丢到EventLoop中执行
#     loop.run_until_complete(test())


loop.run_until_complete(findAll())
