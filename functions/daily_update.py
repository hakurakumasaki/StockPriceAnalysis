import get_historical_price_data
import update_DB


def main():
    get_historical_price_data.main()
    update_DB.main()


if __name__ == '__main__':
    main()