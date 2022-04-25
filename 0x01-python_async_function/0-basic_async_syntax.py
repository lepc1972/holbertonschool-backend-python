#!/usr/bin/env python3
'''Asynch basics'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''takes in an argument, wait for delay, returns the delay.'''
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
