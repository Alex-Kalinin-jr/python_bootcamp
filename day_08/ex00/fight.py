"""
Emulates asynchronous work in a fight between an agent and Neo.
"""
import asyncio
import enum
import random


class Action(enum.Enum):
    HIGHKICK = enum.auto()
    LOWKICK = enum.auto()
    HIGHBLOCK = enum.auto()
    LOWBLOCK = enum.auto()


acts_dict = {
    Action.HIGHKICK: {
        Action.HIGHBLOCK: (0, 0),
        Action.LOWBLOCK: (0, -1),
        Action.HIGHKICK: (-1, -1),
        Action.LOWKICK: (-1, -1),
    },
    Action.LOWKICK: {
        Action.HIGHBLOCK: (0, -1),
        Action.LOWBLOCK: (0, 0),
        Action.HIGHKICK: (-1, -1),
        Action.LOWKICK: (-1, -1),
    },
    Action.HIGHBLOCK: {
        Action.HIGHBLOCK: (0, 0),
        Action.LOWBLOCK: (0, 0),
        Action.HIGHKICK: (0, 0),
        Action.LOWKICK: (-1, 0),
    },
    Action.LOWBLOCK: {
        Action.HIGHBLOCK: (0, 0),
        Action.LOWBLOCK: (0, 0),
        Action.HIGHKICK: (-1, 0),
        Action.LOWKICK: (0, 0),
    },
}


class Agent:

    def __init__(self):
        self.health = 5
        self.actions = list(Action)

    def __aiter__(self):
        return self

    async def __anext__(self):
        return random.choice(self.actions)


async def fight(agent: Agent, neo):
    async for action in agent:
        neo_action = await neo.__anext__()
        print(
            f"Agent: {action}, Neo: {neo_action} \
Agent Health: {agent.health}, Neo Health: {neo.health}"
        )
        dmg_1, dmg_2 = acts_dict[action][neo_action]
        agent.health += dmg_1
        neo.health += dmg_2
        await asyncio.sleep(1)
        if agent.health <= 0 and neo.health <= 0:
            print("Agent and Neo are dead")
            break
        if agent.health <= 0:
            print("Agent is dead")
            break
        if neo.health <= 0:
            print("Neo is dead")
            break


async def main():
    await fight(Agent(), Agent().__aiter__())


if __name__ == "__main__":
    asyncio.run(main())
