# -*- coding: utf-8 -*-

import orm
import asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='root', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))

print('插入成功')
