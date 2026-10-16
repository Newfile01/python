from p1 import coco


def banane():
    print("banane")


def main():
    print(__name__)
    print(coco.__module__)
    coco()


if __name__ == "__main__":
    main()