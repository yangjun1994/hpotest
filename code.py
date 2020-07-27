import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--p1',
        default=1,
        type=int
    )
    parser.add_argument(
        '--p2',
        default=2,
        type=int
    )
    parser.add_argument(
        '--p3',
        default=3,
        type=int
    )
    args = parser.parse_args()
    arguments = args.__dict__
    p1 = arguments.pop('p1')
    p2 = arguments.pop('p2')
    p3 = arguments.pop('p3')
    print('loss=%d'%(p1+p2+p3))
