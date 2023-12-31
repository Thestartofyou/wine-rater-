class Wine:
    def __init__(self, name, winery, vintage, rating=None):
        self.name = name
        self.winery = winery
        self.vintage = vintage
        self.rating = rating

    def rate_wine(self, rating):
        # Rate the wine
        self.rating = rating

    def __str__(self):
        return f"{self.name} ({self.winery} - {self.vintage}): {self.rating}/10"


def main():
    # Example list of wines from current restaurants
    wines = [
        Wine("Cabernet Sauvignon", "Chateau XYZ", 2015),
        Wine("Chardonnay", "Vineyard ABC", 2018),
        Wine("Merlot", "Winery PQR", 2017),
    ]

    # Rate the wines based on the likability of the general public
    for wine in wines:
        try:
            rating = float(input(f"How would you rate {wine.name} ({wine.winery} - {wine.vintage}) on a scale of 1 to 10? "))
            if 1 <= rating <= 10:
                wine.rate_wine(rating)
            else:
                print("Invalid rating. Please enter a rating between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a numeric rating.")

    # Display the rated wines
    print("\nRated Wines:")
    for wine in wines:
        print(wine)

if __name__ == "__main__":
    main()

