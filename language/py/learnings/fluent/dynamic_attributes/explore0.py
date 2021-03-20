
from frozenjson import FrozenJSON
from oscon_feed import load

if __name__ == "__main__":

    raw_feed = load()

    feed = FrozenJSON(raw_feed)
    print(len(feed.Schedule.speakers))
    print(len(raw_feed['Schedule']['speakers']))

    for key, value in sorted(feed.Schedule.items()):
        print('{:3} {}'.format(len(value), key))

    print(feed.Schedule.items())

    talk = feed.Schedule.events[40]
    print(type(talk))
    print(talk.name)
    print(talk)

    print(talk.speakers)