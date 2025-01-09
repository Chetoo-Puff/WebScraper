import requests
from bs4 import BeautifulSoup
import pandas as pd  # For DataFrame and CSV export


def scrapeGame():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    url = 'https://www.espn.com/nba/boxscore/_/gameId/401716947'
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tables
    tables = soup.find_all('table', class_='Table')
    all_data = []

    # Loop through all tables
    for index, table in enumerate(tables):
        rows = []

        # Extract all rows
        for row in table.find_all('tr'):
            cells = [cell.text.strip() for cell in row.find_all(['th', 'td'])]
            if cells:
                rows.append(cells)

        # Use the first row as the header
        if rows:
            headers = rows[0]  # Take the first row as the header
            rows = rows[1:]  # Remaining rows are data
            all_data.append({"headers": headers, "rows": rows})
            print(f"Table {index + 1} Headers: {headers}")
            for row in rows:
                print(row)

    # Save all tables to CSV
    for index, table_data in enumerate(all_data):
        rows = table_data["rows"]
        headers = table_data["headers"]

        # Adjust row lengths to match header count
        adjusted_rows = [row + [''] * (len(headers) - len(row)) for row in rows]

        # Create DataFrame
        df = pd.DataFrame(adjusted_rows, columns=headers)
        filename = f"table_{index + 1}.csv"
        df.to_csv(filename, index=False)
        print(f"Saved Table {index + 1} as {filename}")


if __name__ == '__main__':
    scrapeGame()
