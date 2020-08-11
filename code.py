import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--p1',
        default=1,
        type=float
    )
    parser.add_argument(
        '--p2',
        default=2,
        type=float
    )
    parser.add_argument(
        '--p3',
        default=3,
        type=float
    )
    args = parser.parse_args()
    arguments = args.__dict__
    p1 = arguments.pop('p1')
    p2 = arguments.pop('p2')
    p3 = arguments.pop('p3')
    print('loss=%f'%(p1))
    #print('loss=%f'%(p2))
    #print('loss=%f'%(p3))
