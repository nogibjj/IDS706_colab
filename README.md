# IDS706_colab
![CI](https://github.com/nogibjj/IDS706_colab/actions/workflows/CICD.yml/badge.svg)
![CI](https://github.com/nogibjj/IDS706_colab/actions/workflows/format.yml/badge.svg)
![CI](https://github.com/nogibjj/IDS706_colab/actions/workflows/lint.yml/badge.svg)
![CI](https://github.com/nogibjj/IDS706_colab/actions/workflows/test.yml/badge.svg)

# Setup and configuration (20 points)

The Jupyter Notebook was hosted at Google Colab and here is the link to notebook: https://colab.research.google.com/drive/1mov_B0a0YykQbTdRctkjONheQe3ELZHi?usp=sharing

This notebook is downloaded locally [here](./main.ipynb) and test by using nbval plugin

Using `make install` to insatll necessary libs for this project

Using `make lint` to check the lint

Using run to run the same source code of the notebook in [src](./src/main.py)

Using `make test` to test the notebook and the source code.

# Data manipulation tasks (20 points)

This notebook download the [NBA_2021.csv](./NBA_2021.csv) from website. It will first load the dataset and show some basic info of the dataset plus the descriptive of the dataset.

Then it will do 2 tasks:

* Count the 10 players who have the highest efficiency value among those who have played more than 20 times then visualize the output
    ```python
    df["Efficiency_Rating"] = (
        df["PTS"]
        + df["TRB"]
        + df["AST"]
        + df["STL"]
        + df["BLK"]
        - (df["FGA"] - df["FG"])
        - (df["FTA"] - df["FT"])
        - df["TOV"]
    )
    top_efficiency_players = df[df["G"] > 20][["Player", "Efficiency_Rating"]].nlargest(
        10, "Efficiency_Rating"
    )
    print(top_efficiency_players)

    plt.figure(figsize=(12, 8))
    plt.bar(top_scorers_per_team["Player"], top_scorers_per_team["PTS"], color="skyblue")
    plt.xlabel("Player")
    plt.ylabel("Points (PTS)")
    plt.title("Top Scorers Per Team (Minimum 20 Games Played)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
    ```


* Count the 10 players who get the highest score value in one team among thosse who have played more than 20 times and then visualize the output
    ```python
    top_scorers_per_team = (
        df[df["G"] > 20]
        .sort_values(["Tm", "PTS"], ascending=[True, False])
        .groupby("Tm")
        .head(1)
        .reset_index(drop=True)
    ).sort_values("PTS", ascending=False)
    print(top_scorers_per_team[["Tm", "Player", "PTS"]])

    plt.barh(
    top_efficiency_players["Player"], top_efficiency_players["Efficiency_Rating"], color="salmon"
    )
    plt.xlabel("Efficiency Rating")
    plt.ylabel("Player")
    plt.title("Top 10 Players by Efficiency Rating (Minimum 20 Games Played)")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
    ```

